import sys

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
                            QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
                           QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
                           QRadialGradient)
from PySide2.QtWidgets import *

from variables import v, el_format
import yaml
import os


class Window(QWidget):
    def __init__(self, elem):
        super().__init__(None)

        self.elem = elem

        # self.title = 'Finestra'
        # self.left = 500
        # self.top = 200
        # self.width = 300
        # self.height = 250
        #
        # self.setWindowTitle(self.title)
        # self.setGeometry(self.left, self.top, self.width, self.height)

        self.mainWidget = QWidget()
        self.mainVBL = QVBoxLayout(self.mainWidget)
        self.mainVBL.setContentsMargins(5, 5, 5, 40)
        self.mainWidget.setMaximumWidth(200)    # Deve avere il valore della larghezza del settore scorrevole
        self.topWidget = QWidget()
        self.bottomWidget = QWidget()
        self.mainVBL.addWidget(self.topWidget)
        self.mainVBL.addWidget(self.bottomWidget, 0, Qt.AlignBottom)

        self.topGL = QGridLayout(self.topWidget)
        self.bottomHBL = QHBoxLayout(self.bottomWidget)

        self.cat = v[elem]['category']
        i = 0
        for par in el_format[self.cat]:
            self.__setattr__(par + '_LBL', QLabel(par))
            self.__setattr__(par + '_DSB', QDoubleSpinBox(None))
            self.__setattr__(par + '_unit_LBL', QLabel(el_format[self.cat][par]['unit']))

            self.topGL.addWidget(self.__getattribute__(par + '_LBL'), i, 0)
            self.topGL.addWidget(self.__getattribute__(par + '_DSB'), i, 1)
            self.topGL.addWidget(self.__getattribute__(par + '_unit_LBL'), i, 2)
            i += 1

            # formattazione e popolazione dei campi
            self.dsb_format(self.__getattribute__(par + '_DSB'), minimum=el_format[self.cat][par]['min'],
                            maximum=el_format[self.cat][par]['max'], decimals=el_format[self.cat][par]['decimal'])
            self.__getattribute__(par + '_DSB').setValue(v[elem]['par'][par])

            self.__getattribute__(par + '_LBL').setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        # creazione della parte dei profili, se previsto
        if self.cat in ['AC-Load', 'DC-Load', 'AC-Wind', 'DC-Wind', 'BESS', 'PV']:
            # distanziatore
            spacer1 = QSpacerItem(20, 20, QSizePolicy.Fixed)
            self.topGL.addItem(spacer1, i, 0)
            i += 1

            # -- creazione ed inserimento degli elementi ----
            self.scale_LBL = QLabel('Scala')
            self.scale_DSB = QDoubleSpinBox()
            self.scale_RB = QRadioButton('Costante')

            self.profile_RB = QRadioButton('Profilo')

            self.topGL.addWidget(self.scale_LBL, i, 0)
            self.topGL.addWidget(self.scale_DSB, i, 1)
            i += 1

            self.topGL.addWidget(self.scale_RB, i, 1)
            i += 1

            self.topGL.addWidget(self.profile_RB, i, 1)
            i += 1

            # formattazione e popolazione degli elementi del profilo
            self.dsb_format(self.scale_DSB, 0, 1, 4)
            self.scale_LBL.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
            if v[elem]['par']['profile']['name'] is None:
                self.scale_DSB.setValue(v[elem]['par']['profile']['curve'])
                self.scale_RB.setChecked(True)
            else:
                self.scale_DSB.setDisabled(True)
                self.profile_RB.setChecked(True)
            # -----------------------------------------------

        # distanziatore
        spacer1 = QSpacerItem(20, 20, QSizePolicy.Fixed)
        self.topGL.addItem(spacer1, i, 0)
        i += 1

        # casella Out-of-service
        self.out_of_service_LBL = QLabel('OutOfServ')
        self.out_of_service_CkB = QCheckBox()
        self.topGL.addWidget(self.out_of_service_LBL, i, 0)
        self.topGL.addWidget(self.out_of_service_CkB, i, 1)
        self.out_of_service_CkB.setChecked(v[elem]['par']['out-of-service'])
        i += 1

        # distanziatore necessario per riempire il vuoto tra i parametri e i pulsanti
        spacer_wgt = QWidget()
        self.topGL.addWidget(spacer_wgt, i, 0)
        i += 1

        # creazione dei pulsanti
        self.save_BTN = QPushButton('Salva')
        self.cancel_BTN = QPushButton('Annulla')
        self.pb_format(self.save_BTN, min_h=25)
        self.pb_format(self.cancel_BTN, min_h=25)
        self.save_BTN.clicked.connect(self.save_par)

        self.bottomHBL.addWidget(self.save_BTN)
        spacer2 = QSpacerItem(20, 20, QSizePolicy.Fixed)
        self.bottomHBL.addItem(spacer2)
        self.bottomHBL.addWidget(self.cancel_BTN)

        # creazione della scrollbar, se il settore fosse troppo lungo
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.mainWidget)
        self.scroll.setWidgetResizable(True)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.scroll)
        self.setLayout(self.layout)

    # salvataggio dei dati
    def save_par(self):
        for par in el_format[self.cat]:
            v[self.elem]['par'][par] = self.__getattribute__(par + '_DSB').value()
            print(par + ': ' + str(v[self.elem]['par'][par]))

        if self.cat in ['AC-Load', 'DC-Load', 'AC-Wind', 'DC-Wind', 'BESS', 'PV']:
            if self.scale_RB.isChecked():
                v[self.elem]['par']['profile']['name'] = None
                v[self.elem]['par']['profile']['curve'] = self.scale_DSB.value()
                print('scale' + ': ' + str(v[self.elem]['par']['profile']['curve']))
            else:
                pass
        v[self.elem]['par']['out-of-service'] = self.out_of_service_CkB.isChecked()

    # formattazione dei DoubleSPinBox
    def dsb_format(self, item, minimum=0, maximum=9999.99, decimals=2, step=0.1):
        item.setMinimum(minimum)
        item.setMaximum(maximum)
        item.setDecimals(decimals)
        item.setSingleStep(step)

        item.setButtonSymbols(QAbstractSpinBox.NoButtons)
        item.setStyleSheet(u"background-color: rgb(255, 255, 255);"
                           u"color: rgb(0, 0, 0);"
                           u"border: solid;"
                           u"border-width: 1px;"
                           u"border-color: rgb(223, 223, 223);")
        item.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

    # formattazione dei pushbutton
    def pb_format(self, item, min_w=0, min_h=0):
        item.setStyleSheet(u"QPushButton {"
                           u"background-color: rgb(0, 0, 0); border: solid;" # border-style: outset;"
                           u"border-width: 1px; border-radius: 10px; border-color: rgb(127, 127, 127)"
                           u"}"
                           u"QPushButton:pressed {"
                           u"background-color: rgb(64, 64, 64); border-style: inset"
                           u"}")
        item.setMinimumSize(QSize(min_w, min_h))


if __name__ == '__main__':
    v = yaml.safe_load(open('C:/Users/anton/PycharmProjects/ARStool/CityArea.yml'))

    App = QApplication()
    window = Window('rs_line')
    window.show()
    sys.exit(App.exec_())

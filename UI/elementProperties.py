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
        super().__init__()

        self.title = 'Finestra'
        self.left = 500
        self.top = 200
        self.width = 300
        self.height = 250

        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.formLayout = QGridLayout()
        # groupBox = QGroupBox('this is groupbox')
        # a = QLabel('a')
        # for i in range(3):
        #     self.formLayout.addWidget(a, 0, i)
        #
        self.mywidget = QWidget()

        # labelList = []
        # buttonList = []

        cat = v[elem]['category']
        i = 0
        for par in el_format[cat]:
            self.__setattr__(par + '_LBL', QLabel(par))
            self.__setattr__(par + '_DSB', QDoubleSpinBox())
            self.__setattr__(par + '_unit_LBL', QLabel(el_format[cat][par]['unit']))

            self.formLayout.addWidget(self.__getattribute__(par + '_LBL'), i, 0)
            # labelList.append(self.__getattribute__(par + '_LBL'))

            self.formLayout.addWidget(self.__getattribute__(par + '_DSB'), i, 1)

            self.formLayout.addWidget(self.__getattribute__(par + '_unit_LBL'), i, 2)

            i += 1

            # buttonList.append(self.__getattribute__(par + '_DSB'))

            # labelList.append(QLabel('Label'))
            # labelList.append(QLabel(name))
            # buttonList.append(QPushButton('Click Me'))

            # self.formLayout.addRow(self.__getattribute__(par + '_LBL'),
            #                        self.__getattribute__(par + '_DSB'),
            #                        self.__getattribute__(par + '_unit_LBL'))
            # QDoubleSpinBox.setMinimum(999.9999)
            self.__getattribute__(par + '_DSB').setMinimum(el_format[cat][par]['min'])
            self.__getattribute__(par + '_DSB').setMaximum(el_format[cat][par]['max'])
            self.__getattribute__(par + '_DSB').setDecimals(el_format[cat][par]['decimal'])

            self.__getattribute__(par + '_DSB').setButtonSymbols(QAbstractSpinBox.NoButtons)
            self.__getattribute__(par + '_DSB').setValue(v[elem]['par'][par])
            self.__getattribute__(par + '_DSB').setStyleSheet(u"background-color: rgb(255, 255, 255); "
                                                              u"color: rgb(0, 0, 0);"
                                                              u"border: solid;"
                                                              u"border-width: 1px;"
                                                              u"border-color: rgb(223, 223, 223);")
            self.__getattribute__(par + '_DSB').setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

            self.__getattribute__(par + '_LBL').setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        if cat in ['AC-Load', 'DC-Load', 'AC-Wind', 'DC-Wind', 'BESS']:
            self.scale_LBL = QLabel('Scala')
            self.scale_DSB = QDoubleSpinBox()
            self.scale_RB = QRadioButton('Costante')
            self.profile_RB = QRadioButton('Profilo')

            # self.spacer_LBL = QLabel('-')
            # for j in range(3):
            #     self.formLayout.addWidget(self.spacer_LBL, i, j)
            # i += 1

            self.formLayout.addWidget(self.scale_LBL, i, 0)
            self.formLayout.addWidget(self.scale_DSB, i, 1)
            self.formLayout.addWidget(self.scale_RB, i, 2)
            self.formLayout.addWidget(self.profile_RB, i+1, 2)

            self.scale_DSB.setMinimum(0)
            self.scale_DSB.setMaximum(1)
            self.scale_DSB.setDecimals(4)

            self.scale_DSB.setButtonSymbols(QAbstractSpinBox.NoButtons)
            self.scale_DSB.setStyleSheet(u"background-color: rgb(255, 255, 255);"
                                         u"color: rgb(0, 0, 0);"
                                         u"border: solid;"
                                         u"border-width: 1px;"
                                         u"border-color: rgb(223, 223, 223);")
            self.scale_DSB.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

            self.scale_LBL.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)


            if v[elem]['par']['profile']['name'] is None:
                self.scale_DSB.setValue(v[elem]['par']['profile']['curve'])
                self.scale_RB.setChecked(True)
            else:
                self.scale_DSB.setDisabled(True)
                self.profile_RB.setChecked(True)

        spacer = QWidget()
        self.formLayout.addWidget(spacer, i+2, 0)



        # groupBox.setLayout(formLayout)
        self.mywidget.setLayout(self.formLayout)
        self.scroll = QScrollArea()
        # scroll.setWidget(groupBox)
        self.scroll.setWidget(self.mywidget)
        self.scroll.setWidgetResizable(True)
        # self.scroll.setFixedHeight(100)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.scroll)

        self.setLayout(self.layout)

        # mywidget.setLayout(formLayout)
        # scroll = QScrollArea()
        # # scroll.setWidget(groupBox)
        # scroll.setWidget(mywidget)

        # self.show()


if __name__ == '__main__':
    v = yaml.safe_load(open('C:/Users/anton/PycharmProjects/OpenDSS/CityArea.yml'))

    App = QApplication(sys.argv)
    window = Window('rs_line')
    window.show()
    sys.exit(App.exec_())

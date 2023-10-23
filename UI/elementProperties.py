import sys

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

from variables import v
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

        self.formLayout = QFormLayout()
        # groupBox = QGroupBox('this is groupbox')

        self.mywidget = QWidget()

        # labelList = []
        # buttonList = []

        for par in v[elem]['par']:
            self.__setattr__(par + '_LBL', QLabel(par))
            # labelList.append(self.__getattribute__(par + '_LBL'))

            self.__setattr__(par + '_DSB', QDoubleSpinBox())

            # buttonList.append(self.__getattribute__(par + '_DSB'))

            # labelList.append(QLabel('Label'))
            # labelList.append(QLabel(name))
            # buttonList.append(QPushButton('Click Me'))
            self.formLayout.addRow(self.__getattribute__(par + '_LBL'),
                              self.__getattribute__(par + '_DSB'))
            # QDoubleSpinBox.setMinimum(999.9999)
            self.__getattribute__(par + '_DSB').setMaximum(9999.9999)
            self.__getattribute__(par + '_DSB').setButtonSymbols(QAbstractSpinBox.NoButtons)
            self.__getattribute__(par + '_DSB').setValue(v[elem]['par'][par])

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

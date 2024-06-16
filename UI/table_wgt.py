try:
    from .ui_table_wgt import *
except:
    from ui_table_wgt import *

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import sys


class Table(QMainWindow):
    def __init__(self, parent=None):
        super(Table, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.add_Btn.setStyleSheet(u"QPushButton {"
                                      u"color: rgb(255, 255, 255);"
                                      u"background-color: rgb(31, 31, 31); border: solid;" # border-style: outset;"
                                      u"border-width: 1px; border-radius: 10px; border-color: rgb(127, 127, 127)"
                                      u"}"
                                      u"QPushButton:pressed {"
                                      u"background-color: rgb(64, 64, 64); border-style: inset"
                                      u"}")

        self.ui.save_Btn.setStyleSheet(u"QPushButton {"
                                       u"color: rgb(255, 255, 255);"
                                       u"background-color: rgb(31, 31, 31); border: solid;" # border-style: outset;"
                                       u"border-width: 1px; border-radius: 10px; border-color: rgb(127, 127, 127)"
                                       u"}"
                                       u"QPushButton:pressed {"
                                       u"background-color: rgb(64, 64, 64); border-style: inset"
                                       u"}")

        self.ui.del_Btn.setStyleSheet(u"QPushButton {"
                                      u"color: rgb(255, 255, 255);"
                                      u"background-color: rgb(31, 31, 31); border: solid;" # border-style: outset;"
                                      u"border-width: 1px; border-radius: 10px; border-color: rgb(127, 127, 127)"
                                      u"}"
                                      u"QPushButton:pressed {"
                                      u"background-color: rgb(64, 64, 64); border-style: inset"
                                      u"}")
        self.ui.del_Btn.setVisible(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # mw = QMainWindow()
    window = Table()
    # window.ui.setupUi(mw)
    window.show()

    sys.exit(app.exec_())
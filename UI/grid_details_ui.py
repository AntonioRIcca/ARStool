try:
    from .ui_grid_details import *
except:
    from ui_grid_details import *

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *

import sys


class GridDetailsWGT(QMainWindow):
    def __init__(self, parent=None):
        super(GridDetailsWGT, self).__init__()
        self.ui = Ui_mainWgt()
        self.ui.setupUi(self)

        # self.ui.startWgt.setStyleSheet(u"QPushButton {"
        #                                u"text-align: left;"
        #                                u"padding: 10px 40px;"
        #                                u"color: rgb(255, 255, 255);"
        #                                u"background-color: rgb(31, 31, 31); border: solid;" # border-style: outset;"
        #                                u"border-width: 3px; border-radius: 30px; border-color: rgb(127, 127, 127)"
        #                                u"}"
        #                                u"QPushButton:pressed {"
        #                                u"background-color: rgb(64, 64, 64); border-style: inset"
        #                                u"}")
        #

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # mw = QMainWindow()
    window = GridDetailsWGT()
    # window.ui.setupUi(mw)
    window.show()

    sys.exit(app.exec_())
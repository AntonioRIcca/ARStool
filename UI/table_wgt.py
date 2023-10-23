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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # mw = QMainWindow()
    window = Table()
    # window.ui.setupUi(mw)
    window.show()

    sys.exit(app.exec_())
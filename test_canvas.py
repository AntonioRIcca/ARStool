from PySide2 import QtWidgets, QtCore, QtGui
from matplotlib.figure import Figure
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
from matplotlib.backends.backend_qt5agg import (FigureCanvasQTAgg as
FigureCanvas, NavigationToolbar2QT as NavigationToolbar)

class MyQtApp(main.Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super(MyQtApp, self).__init__()
        self.setupUi(self)

        self.graphBtn.clicked.connect(self.launchGraph)

        self.show()

    def launchGraph(self):
        if self.mycb.currrentText() == 'feature1':
            df1 = ... #data from a data source
        else: #== feature2)
            # df1 = ... #some other data
            pass

        self.mywidget.figure = Figure()
        self.mywidget.canvas = FigureCanvas(self.mywidget.figure)
        self.mywidget.toolbar = NavigationToolbar(self.mywidget.canvas, self)

        self.mywidget.graphLayout = QtWidgets.QVBoxLayout()
        self.mywidget.graphLayout.addWidget(self.mywidget.canvas)
        self.mywidget.graphLayout.addWidget(self.mywidget.toolbar)
        self.mywidget.setLayout(self.mywidget.graphLayout)

        ax = self.mywidget.figure.add_subplot(111)
        ax.clear()
        ax.plot(df1['x'], df1['y'])
        self.mywidget.canvas.draw()
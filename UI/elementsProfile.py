# from ui_elementsProfile_dlg import Ui_mainDlg
# from UI.ui_elementsProfile_dlg import Ui_mainDlg
import os
from UI.elementsProfile_Dlg import Ui_mainDlg

# from PySide2 import QtGui, QtCore, QtWidgets
from PyQt5 import QtWidgets, QtGui, QtCore

import PyQt5

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from variables import v


class ElementsProfile(QtWidgets.QDialog):
    def __init__(self, elem):
        super(ElementsProfile, self).__init__()
        self.ui = Ui_mainDlg()
        self.ui.setupUi(self)

        self.elem = elem

        self.ui.profileTW.setColumnWidth(0, 50)
        self.ui.profileTW.setColumnWidth(1, 100)

        self.plotVBL = QtWidgets.QVBoxLayout()
        self.ui.plotWgt.setLayout(self.plotVBL)

        self.canvas = FigureCanvas(plt.Figure(figsize=(3, 2), facecolor=(0, 0, 0)))

        with plt.rc_context({'axes.edgecolor': 'white', 'xtick.color': 'white', 'ytick.color': 'white',
                             'figure.facecolor': 'red'}):

            self.ax = self.canvas.figure.subplots()
        self.ax.tick_params(axis='x', colors='white', labelsize=10)
        self.ax.tick_params(axis='y', colors='white', labelsize=10)

        self.plotVBL.addWidget(self.canvas)

        self.table_fill()
        self.plot_profile()

        self.ui.profileTW.cellClicked.connect(self.tab_selected)
        self.ui.profileTW.itemChanged.connect(self.tab_value_changed)
        self.ui.importBtn.clicked.connect(self.data_import)
        self.ui.exportBtn.clicked.connect(self.data_export)

    def table_format(self):
        self.ui.profileTW.setShowGrid(False)
        self.ui.profileTW.setStyleSheet('QTableView::item {border-top: 1px solid #333333;}')
        self.ui.profileTW.verticalHeader().setVisible(False)

        stylesheet = ("QHeaderView::section{color:rgb(251,251,251); "
                      "Background-color:rgb(1,1,1); "
                      "border-radius: 14 px;}")
        self.ui.profileTW.horizontalHeader().setStyleSheet(stylesheet)

        for i in range(0, self.ui.profileTW.rowCount()):
            for j in range(0, self.ui.profileTW.columnCount()):
                self.ui.profileTW.item(i, j).setForeground(QtGui.QColor(255,255,255))
                self.ui.profileTW.item(i, j).setTextAlignment(QtCore.Qt.AlignCenter)

        self.ui.profileTW.setHorizontalHeaderLabels(['Tempo [h]', 'Prof. [p.u.]'])
        self.ui.profileTW.setColumnWidth(0, 75)
        self.ui.profileTW.setColumnWidth(1, 75)

    def table_fill(self):
        self.ui.profileTW.clearContents()
        self.ui.profileTW.model().removeRows(0, self.ui.profileTW.rowCount())

        for r in range (0, len(v[self.elem]['par']['profile']['curve'])):
            self.ui.profileTW.insertRow(r)
            x_item = QtWidgets.QTableWidgetItem(str(r*0.25))
            try:
                y_item = QtWidgets.QTableWidgetItem('%-5f' % v[self.elem]['par']['profile']['curve'][r])
            except:
                y_item = QtWidgets.QTableWidgetItem('')
            x_item.setTextAlignment(QtCore.Qt.AlignCenter)
            y_item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.ui.profileTW.setItem(r, 0, x_item)
            self.ui.profileTW.setItem(r, 1, y_item)
        self.table_format()

    def plot_profile(self):
        self.ax.cla()

        (x, y) = ([], [])
        for r in range(0, len(v[self.elem]['par']['profile']['curve'])):
            x.append(r * 0.25)
            y.append(v[self.elem]['par']['profile']['curve'][r])

        font = {
            'weight': 'normal',
            'size': 10
        }
        matplotlib.rc('font', **font)

        self.ax.set_ylim([0, 1.05])
        self.ax.set_xlim([0, 24])
        self.ax.set_xlabel('Tempo [h]', fontsize=10, color=(1, 1, 1))
        self.ax.set_ylabel('Profilo [p.u.]', fontsize=10, color=(1, 1, 1))

        self.ax.set_facecolor((0, 0, 0))

        self.line, = self.ax.plot(x, y)
        # self.plotVBL.addWidget(self.canvas)

        self.canvas.draw()
        self.canvas.flush_events()

    def tab_selected(self):
        try:
            self.old_value = self.ui.profileTW.currentItem().text()
        except:
            self.old_value = ''

    def tab_value_changed(self, q_item):
        c = self.ui.profileTW.currentIndex().column()
        if c == 0:
            q_item.setText(self.old_value)

    def data_import(self):
        try:
            self.ui.profileTW.cellClicked.disconnect()
            self.ui.profileTW.itemChanged.disconnect()
        except TypeError:
            pass

        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog

        filename, ext = QtWidgets.QFileDialog.getOpenFileName(caption="Apri profilo",
                                                              directory=str(os.path.join(os.environ['USERPROFILE'],
                                                                                         'Desktop')),
                                                              filter='*.txt')

        if filename:
            prof = []
            i = 1
            with open(filename, 'r') as f:
                try:
                    for line in f.readlines():
                        prof.append(float(line))
                        self.ui.profileTW.setItem(len(prof)-1, 1, QtWidgets.QTableWidgetItem('%.5f' % float(line)))
                        i += 1
                    v[self.elem]['par']['profile']['curve'] = prof
                    self.plot_profile()
                except:
                    QtWidgets.QMessageBox.warning(self, 'Attenzione!', 'File non valido')

    def data_export(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog

        filename, ext = QtWidgets.QFileDialog.getSaveFileName(caption="Apri profilo",
                                                              directory=str(os.path.join(os.environ['USERPROFILE'],
                                                                                         'Desktop')),
                                                              filter='*.txt')
        print(filename)

        if filename:
            with open(filename, 'w') as f:
                for item in v[self.elem]['par']['profile']['curve']:
                    f.write(str(item) + '\n')
        print('done')
        pass
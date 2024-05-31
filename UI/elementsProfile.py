# from ui_elementsProfile_dlg import Ui_mainDlg
# from UI.ui_elementsProfile_dlg import Ui_mainDlg
import os
from UI.elementsProfile_Dlg import Ui_mainDlg

# from PySide2 import QtGui, QtCore, QtWidgets
from PyQt5 import QtWidgets, QtGui, QtCore

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from variables import v
import copy


class ElementsProfile(QtWidgets.QDialog):
    def __init__(self, elem):
        super(ElementsProfile, self).__init__()
        self.ui = Ui_mainDlg()
        self.ui.setupUi(self)

        self.name = v[elem]['par']['profile']['name']
        self.elem = elem
        self.profile = copy.deepcopy(v[elem]['par']['profile']['curve'])
        self.ok_close = True
        self.line = []
        self.old_value = ''

        if not isinstance(self.profile, list):
            value = self.profile
            self.profile = []
            for i in range(96):
                self.profile.append(value)

        self.refresh = False

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
        self.ui.nameLbl.setText(self.name)

        self.ui.profileTW.cellClicked.connect(self.tab_selected)
        self.ui.profileTW.itemChanged.connect(self.tab_value_changed)
        self.ui.importBtn.clicked.connect(self.data_import)
        self.ui.exportBtn.clicked.connect(self.data_export)
        self.ui.saveBtn.clicked.connect(self.data_save)
        self.ui.cancelBtn.clicked.connect(self.cancel)
        self.ui.nameLbl.mouseDoubleClickEvent = self.rename

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
                self.ui.profileTW.item(i, j).setForeground(QtGui.QColor(255, 255, 255))
                self.ui.profileTW.item(i, j).setTextAlignment(QtCore.Qt.AlignCenter)

        self.ui.profileTW.setHorizontalHeaderLabels(['Tempo [h]', 'Prof. [p.u.]'])
        self.ui.profileTW.setColumnWidth(0, 75)
        self.ui.profileTW.setColumnWidth(1, 75)

    def table_fill(self):
        self.ui.profileTW.clearContents()
        self.ui.profileTW.model().removeRows(0, self.ui.profileTW.rowCount())

        for r in range(0, len(self.profile)):
            self.ui.profileTW.insertRow(r)
            x_item = QtWidgets.QTableWidgetItem(str(r*0.25))
            try:
                y_item = QtWidgets.QTableWidgetItem('%-5f' % self.profile[r])
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
        for r in range(0, len(self.profile)):
            x.append(r * 0.25)
            y.append(self.profile[r])

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
        r = self.ui.profileTW.currentIndex().row()

        try:
            value = float(q_item.text())
        except ValueError:
            value = -1

        if c == 0 or value < 0 or value > 1:
            q_item.setText(str(self.old_value))
        else:
            self.old_value = value
            self.profile[r] = value
            q_item.setText(str(value))
            self.plot_profile()

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
                    self.profile = prof
                    self.plot_profile()
                    self.name = filename.split('/')[len(filename.split('/')) - 1].removesuffix('.txt')
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
                for item in self.profile:
                    f.write(str(item) + '\n')
        print('done')
        pass

    def data_save(self):
        print('save clicked')
        if not self.name:
            ok = False
            name = ''
            while not ok or name == '':
                name, ok = QtWidgets.QInputDialog.getText(self,
                                                          "Nome profilo",
                                                          "inserisci il nome del profilo")
            self.name = name

        v[self.elem]['par']['profile']['name'] = self.name
        v[self.elem]['par']['profile']['curve'] = self.profile
        self.refresh = True
        self.ok_close = True
        self.close()

    def rename(self, event=None):
        name, ok = QtWidgets.QInputDialog.getText(self,
                                                  'Nome profilo',
                                                  'inserisci il nome del profilo',
                                                  text=self.name
                                                  )
        if ok and name != '':
            self.name = name
            self.ui.nameLbl.setText(name)

    def cancel(self):
        # self.closing_check()
        self.close()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key.Key_Escape:
            self.close()

    def closeEvent(self, a0):
        print('finesttra chiusa')
        # close = self.cancel()
        self.closing_check()

        if self.ok_close:
            a0.accept()
        else:
            a0.ignore()

    def closing_check(self):
        self.ok_close = True
        if self.profile != v[self.elem]['par']['profile']['curve']:
            warning = QtWidgets.QMessageBox()
            warning.setText('I dati non salvati andranno persi. \n Voler uscire comunque?')
            warning.setStandardButtons(QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

            x = warning.exec_()

            if x == QtWidgets.QMessageBox.Yes:
                # self.close()
                pass
            else:
                warning.close()
                self.ok_close = False
        else:
            # self.close()
            pass

    # TODO: Dare la possibilità di azzerare il profilo (magari inserendo di default il valore 1)
    # TODO: Il profilo nuovo deve avere solo il primo valore popolato, e deve calcolarsi in automatico gli altri valori
    #       Vedi ORATool
    # TODO: La lunghezza dell'array deve dipendere dalla lunghezza dell'intervallo e dal timestep, che devono essere
    #       parametri globali dello studio

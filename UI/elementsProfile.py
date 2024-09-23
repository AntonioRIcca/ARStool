# from ui_elementsProfile_dlg import Ui_mainDlg
# from UI.ui_elementsProfile_dlg import Ui_mainDlg
import os
from UI.elementsProfile_Dlg import Ui_mainDlg

# from PySide2 import QtGui, QtCore, QtWidgets
from PyQt5 import QtWidgets, QtGui, QtCore

import matplotlib
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt

from variables import *
import copy


class ElementsProfile(QtWidgets.QDialog):
    def __init__(self, elem, default=False, cat=None):
        super(ElementsProfile, self).__init__()
        self.ui = Ui_mainDlg()
        self.ui.setupUi(self)

        self.default = default
        self.elem = elem
        # self.prof_cat = None
        self.cat = cat
        #
        # for k in bench['profiles']:
        #     if cat == bench['profiles'][k]:
        #         self.prof_cat = k
        #         break

        self.timesteps = {
            15: {'jump': 1, 'unit': 'h', 'scale': 4},
            30: {'jump': 2, 'unit': 'h', 'scale': 2},
            60: {'jump': 4, 'unit': 'h', 'scale': 1},
            180: {'jump': 12, 'unit': 'day', 'scale': 8},
            360: {'jump': 24, 'unit': 'day', 'scale': 4},
            1440: {'jump': 96, 'unit': 'day', 'scale': 1},
        }

        # self.timesteps = [1, 5, 10, 15, 30, 60, 180, 360, 1440]

        if self.default:
            self.profile = 1
            self.name = None

            self.default_import()

        elif self.elem:
            self.profile = copy.deepcopy(v[elem]['par']['profile']['curve'])
            self.name = v[elem]['par']['profile']['name']
        else:
            self.profile = 1
            self.name = None

        self.ok_close = True
        self.line = []
        self.old_value = ''

        if not isinstance(self.profile, list):
            value = self.profile
            self.profile = []
            for i in range(grid['profile']['points']):
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
        self.ui.defaultBtn.clicked.connect(self.default_import)

        self.default_check()

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

        self.ui.profileTW.setHorizontalHeaderLabels(['Tempo [' + self.timesteps[grid['profile']['step']]['unit'] + ']',
                                                     'Prof. [p.u.]'])
        self.ui.profileTW.setColumnWidth(0, 75)
        self.ui.profileTW.setColumnWidth(1, 75)

    def table_fill(self):
        try:
            self.ui.profileTW.itemChanged.disconnect()
        except: pass

        self.ui.profileTW.clearContents()
        self.ui.profileTW.model().removeRows(0, self.ui.profileTW.rowCount())

        for r in range(0, len(self.profile)):
            self.ui.profileTW.insertRow(r)
            x_item = QtWidgets.QTableWidgetItem(str(r / self.timesteps[grid['profile']['step']]['scale']))
            try:
                y_item = QtWidgets.QTableWidgetItem('%-5f' % self.profile[r])
            except:
                y_item = QtWidgets.QTableWidgetItem('')
            x_item.setTextAlignment(QtCore.Qt.AlignCenter)
            y_item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.ui.profileTW.setItem(r, 0, x_item)
            self.ui.profileTW.setItem(r, 1, y_item)
        self.table_format()
        self.ui.profileTW.itemChanged.connect(self.tab_value_changed)

    def plot_profile(self):
        self.ax.cla()

        (x, y) = ([], [])
        for r in range(0, len(self.profile)):
            x.append(r / self.timesteps[grid['profile']['step']]['scale'])
            y.append(self.profile[r])

        font = {
            'weight': 'normal',
            'size': 10
        }
        matplotlib.rc('font', **font)

        self.ax.set_ylim([0, 1.05 * max(self.profile)])
        self.ax.set_xlim([0, len(self.profile) / self.timesteps[grid['profile']['step']]['scale']])
        self.ax.set_xlabel('Tempo [' + self.timesteps[grid['profile']['step']]['unit'] + ']',
                           fontsize=10, color=(1, 1, 1))  # TODO: da definire l'unità di misura
        self.ax.set_ylabel('Profilo [p.u.]', fontsize=10, color=(1, 1, 1))

        self.ax.set_facecolor((0, 0, 0))

        self.line, = self.ax.plot(x, y)
        # self.plotVBL.addWidget(self.canvas)

        self.canvas.draw()
        self.canvas.flush_events()

    def x_par(self):  # TODO: per il momento non serve
        s = grid['profile']['step']
        p = grid['profile']['points']

        if p < 60:
            unit = 'min'
        else:
            unit = 'h'

        while p > 10:
            if p < 60:
                s = s * s / 60
                p = 60
                unit = 'h'
            else:
                s = s * 5
                p = p / 5

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

    def default_import(self):
        import datetime
        # from UI.elemProfCat_Dlg import ElemProfCatDlg

        mcat = ''
        # Seleziona la categoria del profilo
        if v[self.elem]['category'] in mc['Load']:
            mcat = 'Load'
        elif v[self.elem]['category'] in mc['Load']:
            mcat = 'Gen'

        file = open(mainpath + '/_benchmark/_data/_profiles/' + mcat + '_year.txt')
        head = file.readline().removesuffix('\n').split('\t')

        if not self.cat:
            prof_cat = None
            from UI.elemProfCat_Dlg import ElemProfCatDlg
            dlg = ElemProfCatDlg()
            for pcat in bench['profiles']:
                dlg.ui.profCatCB.addItem(bench['profiles'][pcat])
            dlg.exec_()
            if dlg.ok:
                self.cat = dlg.ui.profCatCB.currentText()
            else:
                self.cat = None

        if self.cat:
            for k in bench['profiles']:
                if self.cat == bench['profiles'][k]:
                    prof_cat = k
                    break

            data = {
                'year': [],
                'month': [],
                'weekday': [],
                'day': [],
            }

            col = head.index(prof_cat) - 1
            for line in file.readlines():
                data['year'].append(float(line.split('\t')[col + 1]))

            for p in ['month', 'weekday', 'day']:
                file = open(mainpath + '/_benchmark/_data/_profiles/' + mcat + '_' + p + '.txt')
                line = file.readline()
                for line in file.readlines():
                    data[p].append(float(line.split('\t')[col]))

            # m, i = 0, 0
            # m = 0
            # file = open(mainpath + '/_benchmark/_data/_profiles/' + mcat + '_day.txt')
            # line = file.readline()
            # for line in file.readlines():
            #     m += float(line.split('\t')[col])
            #     i += 1
            #     if i == self.timesteps[grid['profile']['step']]['jump']:
            #         data['day'].append(m / self.timesteps[grid['profile']['step']]['jump'])
            #         m, i = 0, 0

            datastart = datetime.datetime(grid['profile']['start'][0], grid['profile']['start'][1],
                                          grid['profile']['start'][2], grid['profile']['start'][3],
                                          grid['profile']['start'][4])
            dataend = datetime.datetime(grid['profile']['end'][0], grid['profile']['end'][1],
                                        grid['profile']['end'][2], grid['profile']['end'][3],
                                        grid['profile']['end'][4])

            t = datastart
            self.profile = []
            m, i, j = 0, 0, 0
            while t <= dataend:
                m += (data['year'][t.year - 2010] * data['month'][t.month - 1] * data['weekday'][t.weekday()]
                      * data['day'][int(t.hour * 4 + t.minute / 15)])
                t = t + datetime.timedelta(minutes=15)
                i += 1
                if i == self.timesteps[grid['profile']['step']]['jump']:
                    self.profile.append(m / self.timesteps[grid['profile']['step']]['jump'])
                    m, i = 0, 0
            if i != 0:
                self.profile.append(m / i)

            print(self.name)
            print('righe', self.ui.profileTW.rowCount())
            if self.ui.profileTW.rowCount() > 0:
                print('agg')
                self.plot_profile()
                self.table_fill()
                self.cat = None

            self.name = self.elem + '_' + prof_cat

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
                        i += 1
                    print(len(prof))
                    print(grid['profile']['points'])
                    if len(prof) == grid['profile']['points']:
                        self.profile = prof
                        self.plot_profile()
                        self.table_fill()
                        self.name = filename.split('/')[len(filename.split('/')) - 1].removesuffix('.txt')
                    else:
                        s = 'Numero di punti non valido.\nCaricare file con ' + str(grid['profile']['points']) + ' punti'
                        QtWidgets.QMessageBox.warning(self, 'Attenzione!', s)
                        # QtWidgets.QMessageBox.warning(self, 'Attenzione!', 'Numero di punti non valido.')
                except:
                    QtWidgets.QMessageBox.warning(self, 'Attenzione!', 'File non valido')

    def data_export(self):
        options = QtWidgets.QFileDialog.Options()
        options |= QtWidgets.QFileDialog.DontUseNativeDialog

        filename, ext = QtWidgets.QFileDialog.getSaveFileName(caption="Apri profilo",
                                                              directory=str(os.path.join(os.environ['USERPROFILE'],
                                                                                         'Desktop')),
                                                              filter='*.txt')

        if filename:
            with open(filename, 'w') as f:
                for item in self.profile:
                    f.write(str(item) + '\n')

    def data_save(self):
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

    def default_check(self):
        y = []
        f = open(mainpath + '/_benchmark/_data/_profiles/Gen_year.txt')
        for line in f:
            try:
                y.append(int(line.split()[0]))
            except ValueError:
                pass

        self.ui.defaultBtn.setVisible(grid['profile']['start'][0] in y and grid['profile']['end'][0] in y)

    # TODO: Dare la possibilità di azzerare il profilo (magari inserendo di default il valore 1)
    # TODO: Il profilo nuovo deve avere solo il primo valore popolato, e deve calcolarsi in automatico gli altri valori
    #       Vedi ORATool
    # TODO: La lunghezza dell'array deve dipendere dalla lunghezza dell'intervallo e dal timestep, che devono essere
    #       parametri globali dello studio

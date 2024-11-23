import copy

# from PySide2 import QtGui, QtCore, QtWidgets
from PyQt5 import QtWidgets, QtGui, QtCore

from Functionalities.Reliability.YearProfile.yearprofileUI import Ui_Form
# from Functionalities.Reliability.YearProfile.ui_yearprofileUI import Ui_Form
# from Functionalities.Reliability.YearProfile.yearprofileUI import Ui_MainWindow
# from PyQt5 import QtWidgets, QtGui, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
import matplotlib
import yaml
import os
from functools import partial

from statistics import mean

from variables import grid, mainpath


class YearProfile(QtWidgets.QDialog):
    def __init__(self, name, profile):
        super(YearProfile, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        # print('nome profilo')
        # print(name)

        self.ui.profile_TW.setColumnWidth(0, 50)
        self.ui.profile_TW.setColumnWidth(1, 100)

        self.max = 50

        self.months = ['Gen', 'Feb', 'Mar', 'Apr', 'Mag', 'Giu', 'Lug', 'Ago', 'Set', 'Ott', 'Nov', 'Dic']

        self.name = name
        self.input_name = name
        self.input_profile = profile
        self.profile_set = False
        self.step = False
        self.confirmed = False

        self.void_profile = dict()
        self.graph_profile = []
        self.timeline = []
        self.month = None
        self.day = None

        self.prof_wizard = False

        for month in self.months:
            self.void_profile[month] = dict()
            self.void_profile[month]['av'] = 20
            self.void_profile[month]['prof'] = dict()

            if month in ['Apr', 'Giu', 'Set', 'Nov']:
                days = 30
            elif month == 'Feb':
                days = 28
            else:
                days = 31

            for day in range(1, days+1):
                self.void_profile[month]['prof'][day] = dict()
                self.void_profile[month]['prof'][day]['av'] = 20
                self.void_profile[month]['prof'][day]['prof'] = dict()

                for i in range(0, 24):
                    self.void_profile[month]['prof'][day]['prof'][i] = 20

        if profile is None:
            self.profile = copy.deepcopy(self.void_profile)
        else:
            self.profile = profile

        self.old_profile = copy.deepcopy(self.profile)

        self.line = None

        layout = QtWidgets.QVBoxLayout()
        self.ui.plt_WGT.setLayout(layout)

        self.canvas = FigureCanvas(plt.Figure(figsize=(15, 6)))
        self.ax = self.canvas.figure.subplots()

        layout.addWidget(self.canvas)     # TODO: da riattivare

        self.ui.profile_LBL.setText(name)
        self.gen_profile()
        self.table_fill(self.graph_profile)
        self.plot_init(self.graph_profile)

        self.refresh()

        self.ui.step_BTN.setVisible(False)

        self.ui.month_BTN.setVisible(False)
        self.ui.day_BTN.setVisible(False)
        self.ui.year_BTN.setEnabled(False)

        self.ui.profile_TW.cellClicked.connect(self.tab_selected)
        self.ui.profile_TW.cellDoubleClicked.connect(self.refresh_table)
        self.ui.profile_TW.itemChanged.connect(self.tab_value_changed)
        self.ui.new_BTN.clicked.connect(partial(self.new_profile, True))
        self.ui.save_BTN.clicked.connect(self.save)
        self.ui.load_BTN.clicked.connect(self.load)
        self.ui.reset_BTN.clicked.connect(self.reset_profile)
        self.ui.import_BTN.clicked.connect(self.import_profile)
        self.ui.year_BTN.clicked.connect(self.back_to_year)
        self.ui.month_BTN.clicked.connect(self.back_to_month)
        self.ui.clear_BTN.clicked.connect(self.erase_data)
        self.ui.confirm_BTN.clicked.connect(self.confirm_and_close)
        self.ui.exit_BTN.clicked.connect(self.close)

    #
    def erase_data(self):
        for m in self.profile:
            self.profile[m]['av'] = None
            for d in self.profile[m]['prof']:
                self.profile[m]['prof'][d]['av'] = None
                for h in self.profile[m]['prof'][d]['prof']:
                    self.profile[m]['prof'][d]['prof'][h] = None
        self.month = None
        self.refresh()
        self.step_year()

    #
    def refresh(self):
        try:
            self.ui.profile_TW.itemChanged.disconnect()
        except TypeError:
            pass

        self.gen_profile()
        self.table_fill(self.graph_profile)
        self.plot_graph(self.graph_profile)
        self.ui.profile_TW.itemChanged.connect(self.tab_value_changed)

    #
    def back_to_month(self):
        self.ui.day_BTN.setVisible(False)
        self.ui.month_BTN.setEnabled(False)
        self.day = None
        self.refresh()

    #
    def back_to_year(self):
        self.ui.day_BTN.setVisible(False)
        self.ui.month_BTN.setVisible(False)
        self.ui.year_BTN.setEnabled(False)

        self.day = None
        self.month = None
        self.refresh()

    #
    def calc_profile(self, ref):
        if self.day:
            self.hours_to_day_upd()
            self.day_to_month_upd()
        elif self.month:
            self.day_to_hours_upd(self.month, int(ref))
            self.day_to_month_upd()
        else:
            self.month_to_day(ref)
            for d in self.profile[ref]['prof']:
                self.day_to_hours_upd(ref, d)

    #
    def hours_to_day_upd(self):
        self.profile[self.month]['prof'][self.day]['av'] = \
            mean(list(self.profile[self.month]['prof'][self.day]['prof'].values()))

    #
    def day_to_month_upd(self):
        v = []
        for d in self.profile[self.month]['prof']:
            v.append(self.profile[self.month]['prof'][d]['av'])
        self.profile[self.month]['av'] = mean(v)

    #
    def day_to_hours_upd(self, month, day):
        new_av = self.profile[month]['prof'][day]['av']

        mylist = []
        for val in self.profile[month]['prof'][day]['prof'].values():
            if val:
                mylist.append(val)
            else:
                mylist.append(new_av)
        old_av = mean(mylist)

        for h in self.profile[month]['prof'][day]['prof']:
            if self.profile[month]['prof'][day]['prof'][h]:
                self.profile[month]['prof'][day]['prof'][h] = self.profile[month]['prof'][day]['prof'][h] * new_av / old_av
            else:
                self.profile[month]['prof'][day]['prof'][h] = new_av

    #
    def month_to_day(self, month):
        new_av = self.profile[month]['av']
        v = []
        for d in self.profile[month]['prof']:
            if self.profile[month]['prof'][d]['av']:
                v.append(self.profile[month]['prof'][d]['av'])
            else:
                v.append(new_av)
        old_av = mean(v)

        for d in self.profile[month]['prof']:
            if self.profile[month]['prof'][d]['av']:
                self.profile[month]['prof'][d]['av'] = self.profile[month]['prof'][d]['av'] * new_av / old_av
            else:
                self.profile[month]['prof'][d]['av'] = new_av

    #
    def day_average(self):
        t_mean = mean(list(self.profile[self.month]['prof'][self.day]['prof'].values()))

    #
    def refresh_table(self):
        r = self.ui.profile_TW.currentRow()
        if self.day:
            self.ui.day_BTN.setEnabled(True)
        elif self.month:
            self.day = int(float(self.ui.profile_TW.item(r, 0).text()))
            self.ui.day_BTN.setText('day ' + str(self.day))
            self.ui.day_BTN.setVisible(True)
            self.ui.day_BTN.setEnabled(False)
            self.ui.month_BTN.setEnabled(True)
        else:
            self.month = self.ui.profile_TW.item(r, 0).text()
            self.ui.month_BTN.setText(self.month)
            self.ui.month_BTN.setVisible(True)
            self.ui.month_BTN.setEnabled(False)
            self.ui.year_BTN.setEnabled(True)

        self.ui.profile_TW.clear()

        self.refresh()

    #
    def averages(self):
        for month in self.profile:
            av_days = []
            for day in self.profile[month]['prof']:
                av_day = mean(list(self.profile[month]['prof'][day]['prof'].values()))
                self.profile[month]['prof'][day]['av'] = av_day
                av_days.append(av_day)
            self.profile[month]['av'] = mean(av_days)

    #
    def plot_init(self, profile):
        font = {
            'weight': 'normal',
            'size': 10
        }
        matplotlib.rc('font', **font)

        self.ax.set_ylim([0, 40])
        self.ax.set_xlim([0, len(self.graph_profile)-1])
        self.ax.set_ylabel('T [°C]')

        self.line, = self.ax.plot(self.timeline, profile)

        self.ax.xaxis.set_tick_params(rotation=90, labelsize=8)

        self.canvas.draw()
        self.canvas.flush_events()

    #
    def plot_graph(self, y):
        if self.day:
            xfont = 6
            xtick = range(0, 25)
        elif self.month:
            xfont = 6
            xtick = self.timeline
        else:
            xfont = 8
            xtick = self.timeline

        font = {
            'weight': 'normal',
            'size': 10
        }
        matplotlib.rc('font', **font)
        self.line.set_xdata(self.timeline)
        self.line.set_ydata(y)

        try:
            max_y = max(y) * 1.05
        except:
            max_y = 1.0

        max_x = max(xtick)
        self.ax.set_xlim(1, max_x)
        self.ax.set_ylim(0, max(1, max_y))
        self.ax.set_xticks(xtick)
        self.ax.set_xticklabels(xtick)
        self.ax.xaxis.set_tick_params(rotation=90, labelsize=xfont)
        self.ax.set_ylabel('T [°C]')

        self.canvas.draw()
        self.canvas.flush_events()

    #
    def tab_value_changed(self, q_item):
        c = self.ui.profile_TW.currentIndex().column()
        r = self.ui.profile_TW.currentIndex().row()

        if c == 0:
            q_item.setText(self.old_value)
        else:
            try:
                if q_item.text() != '':
                    # test = float(q_item.text())
                    if float(q_item.text()) < 0 or float(q_item.text()) > self.max:
                        q_item.setText(self.old_value)
                    else:
                        q_item.setText("%.1f" % float(q_item.text()))

                        if not self.step:
                            self.create_profile()
                            self.calc_profile(self.ui.profile_TW.item(r, 0).text())
                            self.gen_profile()
                            self.plot_graph(self.graph_profile)
                        else:
                            self.plot_graph(self.create_profile())
            except ValueError:
                q_item.setText(self.old_value)

        prof_exists = False
        prof = []
        for i in range(0, self.ui.profile_TW.rowCount()):
            try:
                prof.append(float(self.ui.profile_TW.item(i, 1).text()))
                prof_exists = True
            except:
                prof.append(None)
        self.ui.step_BTN.setVisible(prof_exists and self.prof_wizard)

    #
    def tab_selected(self):
        try:
            self.old_value = self.ui.profile_TW.currentItem().text()
        except:
            self.old_value = ''

    #
    def create_profile(self):
        prof = []
        for i in range(0, self.ui.profile_TW.rowCount()):
            try:
                prof.append(float(self.ui.profile_TW.item(i, 1).text()))
            except:
                prof.append(None)

        k_none = []
        for i in range(0, len(prof)):
            if not prof[i]:
                k_none.append(i)
            else:
                for j in k_none:
                    prof[j] = prof[i]
                break
        prof.append(prof[0])

        x1 = 0
        for i in range(0, len(prof)):
            if prof[i] is None:
                x0 = i-1
                for j in range(i, len(prof)):
                    if prof[j] is not None:
                        x1 = j
                        break

                for k in range(x0, x1):
                    prof[k] = prof[x0] + (prof[x1]-prof[x0])/(x1-x0)*(k-x0)
                i = x1
        del prof[self.ui.profile_TW.rowCount()]

        if not self.month:
            for i in range(0, len(prof)):
                self.profile[self.months[i]]['av'] = prof[i]
        elif not self.day:
            g = list(self.profile[self.month]['prof'].keys())
            for i in range(0, len(prof)):
                self.profile[self.month]['prof'][g[i]]['av'] = prof[i]
        else:
            d = list(self.profile[self.month]['prof'][self.day]['prof'].keys())
            for i in range(0, len(prof)):
                self.profile[self.month]['prof'][self.day]['prof'][d[i]] = prof[i]

        return prof

    #
    def new_profile(self, erase=True):
        print(mainpath)
        chk = False
        error_string = ''
        profiles = [f for f in os.listdir(mainpath + '/_benchmark/T_profiles') if f.endswith('.yml')]
        name, confirmed = '', False
        while not chk:
            name, confirmed = QtWidgets.QInputDialog.getText(self, 'Scenario',
                                                             error_string + 'Inserisci il nome del Profilo',
                                                             QtWidgets.QLineEdit.Normal, '')
            error_string = ''
            if name + '.yml' in profiles and confirmed:
                testo = '"' + name + '" già presente nel database\nVuoi sovrascrivere?'
                msgbox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon(), 'Profilo già esistente', testo)
                yes = msgbox.addButton('Sì', QtWidgets.QMessageBox.YesRole)
                no = msgbox.addButton('No', QtWidgets.QMessageBox.NoRole)
                msgbox.exec_()
                if msgbox.clickedButton() != yes:
                    name = ''

            if not confirmed:
                chk = True
            elif name == '':
                chk = False
            else:
                chk = True

                if erase:
                    self.profile = copy.deepcopy(self.void_profile)
                self.refresh()

                self.ui.profile_LBL.setText(name)
                self.name = name

                self.old_profile = self.void_profile
                self.ui.confirm_BTN.setVisible(True)
                self.ui.save_BTN.setVisible(True)
        return name, confirmed

    #
    def import_profile(self):
        name, confirmed = '', False
        v = []

        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Apri File")
        try:
            if filename:
                months = ['Gen', 'Feb', 'Mar', 'Apr', 'Mag', 'Giu', 'Lug', 'Ago', 'Set', 'Ott', 'Nov', 'Dic']
                days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

                with open(filename, 'r') as f:
                    for line in f:
                        v.append(float(line.strip()))
                # print(len(v))
                if len(v) == 35040:
                    temp_dict = dict()

                    line = 0
                    for m in range(0, 12):
                        month = months[m]
                        temp_dict[month] = dict()
                        temp_dict[month]['prof'] = dict()
                        av_month = 0
                        for day in range(0, days[m]):
                            temp_dict[month]['prof'][day] = dict()
                            temp_dict[month]['prof'][day]['prof'] = dict()
                            av_day = 0
                            for h in range(0, 24):
                                temp_dict[month]['prof'][day]['prof'][h] = v[line]
                                av_day = av_day + v[line]
                                line += 1
                            temp_dict[month]['prof'][day]['av'] = av_day / 24
                            av_month = av_month + temp_dict[month]['prof'][day]['av']
                        temp_dict[month]['av'] = av_month / days[m]

                    chk = False
                    error_string = ''
                    profiles = [f for f in os.listdir(os.getcwd() + '/_data/_T_profiles') if f.endswith('.yml')]
                    while not chk:
                        name, confirmed = QtWidgets.QInputDialog.getText(self, 'Scenario',
                                                                         error_string + 'Inserisci il nome del Profilo',
                                                                         QtWidgets.QLineEdit.Normal, '')
                        error_string = ''
                        if name + '.yml' in profiles and confirmed:
                            testo = '"' + name + '" già presente nel database\nVuoi sovrascrivere?'
                            msgbox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon(), 'Profilo già esistente', testo)
                            yes = msgbox.addButton('Sì', QtWidgets.QMessageBox.YesRole)
                            no = msgbox.addButton('No', QtWidgets.QMessageBox.NoRole)
                            msgbox.exec_()
                            if msgbox.clickedButton() != yes:
                                name = ''

                        if not confirmed:
                            chk = True
                        elif name == '':
                            chk = False
                        else:
                            chk = True
                            self.profile = copy.deepcopy(temp_dict)
                            self.refresh()

                            self.ui.profile_LBL.setText(name)
                            self.name = name

                            self.old_profile = self.void_profile
                            self.ui.confirm_BTN.setVisible(True)
                            self.ui.save_BTN.setVisible(True)
                else:
                    msgbox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon(), 'File non conforme',
                                                   'Formato del file non conforme. Consultare il manuale.')
                    msgbox.exec_()
        except Exception as e:
            msgbox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon(), 'Errore caricamento file',
                                           'Errore inatteso nel caricamento del file')
            msgbox.exec_()
        return name, confirmed

    #
    def gen_profile(self):
        self.timeline = []
        self.graph_profile = []
        if not self.month:
            for month in self.months:
                self.graph_profile.append(self.profile[month]['av'])
                self.timeline = self.months
        elif not self.day:
            for day in self.profile[self.month]['prof']:
                self.graph_profile.append(self.profile[self.month]['prof'][day]['av'])
                self.timeline.append(int(day))
        else:
            for t in self.profile[self.month]['prof'][self.day]['prof']:
                self.graph_profile.append(self.profile[self.month]['prof'][self.day]['prof'][t])
                self.timeline.append(t)

    #
    def table_fill(self, y):
        self.ui.profile_TW.clearContents()
        self.ui.profile_TW.model().removeRows(0, self.ui.profile_TW.rowCount())

        self.ui.profile_TW.setShowGrid(False)
        self.ui.profile_TW.setStyleSheet('QTableView::item {border-top: 1px solid #333333;}')
        self.ui.profile_TW.verticalHeader().setVisible(False)

        for r in range(0, len(self.graph_profile)):
            self.ui.profile_TW.insertRow(r)
            x_item = QtWidgets.QTableWidgetItem(str(self.timeline[r]))
            x_item.setFlags(QtCore.Qt.ItemIsEditable)
            try:
                y_item = QtWidgets.QTableWidgetItem("%.1f" % y[r])
            except TypeError:
                y_item = QtWidgets.QTableWidgetItem('')
            x_item.setTextAlignment(QtCore.Qt.AlignCenter)
            y_item.setTextAlignment(QtCore.Qt.AlignCenter)
            self.ui.profile_TW.setItem(r, 0, x_item)
            self.ui.profile_TW.setItem(r, 1, y_item)

        stylesheet = "QHeaderView::section{color:rgb(251,251,251); Background-color:rgb(1,1,1); " \
                     "border - radius: 14 px; font-style: italic;}"
        self.ui.profile_TW.horizontalHeader().setStyleSheet(stylesheet)

        if self.day:
            label = 'Ora'
        elif self.month:
            label = 'Giorno'
        else:
            label = 'Mese'

        self.ui.profile_TW.setHorizontalHeaderLabels([label, 'Temp. [°C]'])
        self.ui.profile_TW.setColumnWidth(0, 65)
        self.ui.profile_TW.setColumnWidth(1, 85)

    def confirm_and_close(self):
        grid['rel']['prof_T'] = {
            'name': self.name,
            'profile': self.profile
        }
        self.confirmed = True
        self.close()

    #
    def save(self):
        profile_dict = dict()
        print(mainpath)
        filename = mainpath + '/_benchmark/T_profiles/' + self.ui.profile_LBL.text() + '.yml'
        profile_dict['name'] = self.ui.profile_LBL.text()
        profile_dict['profile'] = self.profile

        with open(filename, 'w') as file:
            documents = yaml.dump(profile_dict, file)
        file.close()

    #
    def load(self):
        folder = os.getcwd() + '/_data/_T_profiles/'
        options = QtWidgets.QFileDialog.Options()
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Apri File", folder,
                                                            "YAML (*.yml)", options=options)

        if filename and filename.endswith('.yml'):
            profile_dict = yaml.safe_load(open(filename))
            name = profile_dict['name']
            self.name = name
            self.month = None
            self.day = None
            for m in self.months:
                self.profile[m] = profile_dict['profile'][m]
            self.old_profile = copy.deepcopy(self.profile)

            self.refresh()
            self.ui.profile_LBL.setText(name)

    #
    def search_profiles(self):
        my_path = os.getcwd() + '/_data/_T_profiles/'
        profile_list = []
        for file in os.listdir(my_path):
            if file.endswith(".yml"):
                profile_list.append(file.strip('.yml'))
        return profile_list

    #
    def show_profile(self, name, profile):
        self.ui.profile_TW.itemChanged.disconnect()
        self.table_fill(profile)
        self.plot_graph(profile)
        self.ui.profile_LBL.setText(name)
        self.ui.profile_TW.itemChanged.connect(self.tab_value_changed)

    #
    def reset_profile(self):
        msgbox = QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon(), 'Reset', 'Scegliere i dati da resettare')
        current = msgbox.addButton('Schermata corrente', QtWidgets.QMessageBox.NoRole)
        all = msgbox.addButton('Intero anno', QtWidgets.QMessageBox.YesRole)
        cancel = msgbox.addButton('Annulla', QtWidgets.QMessageBox.RejectRole)
        cancel.setVisible(False)

        msgbox.exec_()

        if msgbox.clickedButton() == all:
            self.profile = copy.deepcopy(self.old_profile)
        elif msgbox.clickedButton() == current:
            if self.day:
                self.profile[self.month]['prof'][self.day] = copy.deepcopy(self.old_profile[self.month]['prof'][self.day])
                self.day_to_month_upd()
            elif self.month:
                self.profile[self.month] = copy.deepcopy(self.old_profile[self.month])
            else:
                self.profile = copy.deepcopy(self.old_profile)
        self.refresh()

    #
    def set_exit(self):
        self.profile_set = True

    #
    def closeEvent(self, event):
        if not self.profile_set:
            self.name = self.input_name
            self.profile = self.input_profile

    #
    def step_year(self):
        self.prof_wizard = True
        self.ui.step_BTN.setVisible(False)
        for button in ['confirm_BTN', 'save_BTN', 'new_BTN', 'load_BTN', 'import_BTN', 'clear_BTN', 'reset_BTN']:
            self.ui.__getattribute__(button).setVisible(False)
        self.step = True
        self.ui.step_BTN.setText('Profilo medie mensili completo')
        try:
            self.ui.profile_TW.cellDoubleClicked.disconnect()
        except:
            pass
        self.ui.step_BTN.clicked.connect(self.step_day)

    #
    def step_day(self):
        self.ui.step_BTN.disconnect()

        self.ui.step_BTN.setVisible(False)
        months = list(self.profile.keys())
        for m in range(0, 12):
            days = list(self.profile[months[m]]['prof'].keys())
            try:
                d0 = len(list(self.profile[months[m - 1]]['prof'].keys()))
                t0 = self.profile[months[m - 1]]['av']

            except:
                d0 = len(list(self.profile[months[11]]['prof'].keys()))
                t0 = self.profile[months[11]]['av']

            d1 = len(list(self.profile[months[m]]['prof'].keys()))
            t1 = self.profile[months[m]]['av']

            try:
                d2 = len(list(self.profile[months[m + 1]]['prof'].keys()))
                t2 = self.profile[months[m + 1]]['av']
            except:
                d2 = len(list(self.profile[months[0]]['prof'].keys()))
                t2 = self.profile[months[0]]['av']

            for d in self.profile[months[m]]['prof'].keys():
                if d <= len(days) / 2:
                    self.profile[months[m]]['prof'][d]['av'] = t1 - 2 * (t1 - t0) / (d1 + d0) * (d1 / 2 - d)
                else:
                    self.profile[months[m]]['prof'][d]['av'] = t1 + 2 * (t2 - t1) / (d2 + d1) * (d - d1 / 2)

        self.month = 'Gen'
        self.day = 1
        self.refresh()
        self.ui.step_BTN.setText('Profilo orario completo')

        self.ui.step_BTN.clicked.connect(self.step_uniform)

    #
    def  step_uniform(self):
        self.ui.step_BTN.disconnect()
        name, confirmed = self.new_profile(erase=False)
        self.ui.step_BTN.setVisible(not confirmed)
        if confirmed:
            for m in self.profile:
                self.month_to_day(m)
                for d in self.profile[m]['prof']:
                    self.profile[m]['prof'][d]['prof'] = copy.deepcopy(self.profile['Gen']['prof'][1]['prof'])
                    self.day_to_hours_upd(m, d)

            self.day = None
            self.month = None

            self.refresh()
            self.ui.profile_TW.cellDoubleClicked.connect(self.refresh_table)

            self.step = False
            self.old_profile = copy.deepcopy(self.profile)
            self.save()

            self.ui.step_BTN.setVisible(False)
            for button in ['confirm_BTN', 'save_BTN', 'new_BTN', 'load_BTN', 'import_BTN', 'clear_BTN', 'reset_BTN']:
                self.ui.__getattribute__(button).setVisible(True)
            self.prof_wizard = False

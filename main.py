import py_dss_interface
from PyQt5.QtCore import QTimer
from PySide2 import QtGui


from variables import c, vdss, v
import yaml
# from PySide2 import *
from PySide2.QtWidgets import *
import sys

import opendss
from threading import Thread

from mainUI import MainWindow

from UI.elementProperties import Window

import time


class Main:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.interface_open()

        # f_main = Thread(target=self.interface_open)
        # print('start')
        # f_main.start()

    def interface_open(self):
        print(1)
        self.mainwindow = MainWindow()
        print(2)
        self.ui = self.mainwindow.ui
        print('show)')
        self.mainwindow.show()

        self.ui.label_10.setText('APERTO!!!')

        from UI.table_wgt import Table
        self.myform = Table()
        mywidget = self.myform.ui.widget

        self.ui.homeSW.removeWidget(self.ui.homeSW.currentWidget())
        self.ui.homeSW.addWidget(mywidget)

        self.elementsTableFill()

        self.myform.ui.tableWidget.currentCellChanged.connect(self.test_action)

        # self.myform.ui.label.setText('riuscito! ......................................!')
        # self.myform.ui.label_2.setText(str(self.ui.homeSW.size()))

        self.ui.profileMenuBtn.clicked.connect(self.test_action2)
        self.ui.moreMenuBtn.clicked.connect(self.test_action2)

        # for w in self.ui.mainPages.
        # mywgt = myform.
        # a = QtWidgets.QWidget()

        # self.ui.mainPages.widget(0)
        # for w in self.ui.mainPages.count():
        #     print(w)
        # for w in self.ui.mainPages.w
        # self.ui.mainPages.
        # self.ui.mainPages.addWidget()

        print('exec')
        self.app.exec_()

    def readsize(self):
        self.par_wgt = Window('rs_line')
        self.ui.rightMenuPages.addWidget(self.par_wgt.mywidget)
        self.ui.rightMenuPages.setCurrentIndex(2)

        # self.ui.rightMenuContainer.expandMenu()
        # self.myform.ui.label_2.setText(str(self.ui.homeSW.size()))
        # self.timer = QTimer()
        # self.timer.setInterval(2000)
        # self.timer.timeout.connect(self.test_action)
        # self.timer.start()
        # self.elementsTableFill()
        pass

    def elementsTableFill(self):
        self.myform.ui.tableWidget.clear()
        self.myform.ui.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('Nome Elemento'))
        self.myform.ui.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem('Categoria'))

        self.myform.ui.tableWidget.setRowCount(len(v))

        i = 0
        for elem in v:
            self.myform.ui.tableWidget.setItem(i, 0, QTableWidgetItem(elem))
            self.myform.ui.tableWidget.setItem(i, 1, QTableWidgetItem(v[elem]['category']))
            i += 1
        self.elementsTableFormat()

    def elementsTableFormat(self):
        self.myform.ui.tableWidget.setShowGrid(False)
        self.myform.ui.tableWidget.setStyleSheet('QTableView::item {border-top: 1px solid #333333;}')
        self.myform.ui.tableWidget.verticalHeader().setVisible(False)

        stylesheet = \
            "QHeaderView::section{color:rgb(251,251,251); Background-color:rgb(1,1,1); border - radius: 14 px;}"
        self.myform.ui.tableWidget.horizontalHeader().setStyleSheet(stylesheet)

        for i in range(0, self.myform.ui.tableWidget.rowCount()):
            for j in range(0, self.myform.ui.tableWidget.columnCount()):
                self.myform.ui.tableWidget.item(i, j).setForeground(QtGui.QColor(255,255,255))

        self.myform.ui.tableWidget.setColumnWidth(0, 160)
        self.myform.ui.tableWidget.setColumnWidth(1, 150)

    def test_action(self):
        # self.myform.ui.label_2.setText(str(self.ui.homeSW.size().height()))
        # self.myform.ui.tableWidget.setMinimumHeight(self.ui.homeSW.size().height())
        # self.timer.stop()
        line = self .myform.ui.tableWidget.currentRow()
        elem = self.myform.ui.tableWidget.item(line, 0).text()
        print(elem)

        try:
        # self.ui.rightMenuPages.setCurrentIndex(self.ui.rightMenuPages.count() - 1)
        #     self.ui.rightMenuPages.removeWidget(self.ui.rightMenuPages.widget(self.ui.rightMenuPages.currentIndex()))
            self.ui.rightMenuPages.removeWidget(self.ui.rightMenuPages.widget(2))
        except:
        # print(self.ui.rightMenuPages.widget(self.ui.rightMenuPages.currentIndex()))
            pass
        self.par_wgt = Window(elem)
        self.ui.rightMenuPages.addWidget(self.par_wgt.mywidget)

        self.ui.rightMenuPages.setCurrentIndex(self.ui.rightMenuPages.count() - 1)
        self.ui.rightMenuContainer.expandMenu()

        print(self.ui.rightMenuPages.count())

        pass

    def test_action2(self):
        print(self.ui.rightMenuPages.currentIndex())


dss = opendss.OpenDSS()

filename = 'C:/Users/anton/PycharmProjects/OpenDSS/CityArea.dss'

dss.open(filename)

dss.write_all()

# dss.solve_profile()
dss.solve()

dss.losses_calc()
#
# print(dss.dss.circuit.total_power)
#
# el = 'pros_pv'
# v[el]['par']['P'] = 200
# dss.write('pros_pv')
# dss.solve()
#
# print(dss.dss.circuit.total_power)

Main()

with open('CityArea.yml', 'w') as file:
    yaml.dump(v, file)
    file.close()


# print('end2')

# Apri file

#
#
# # -- VECCHIO CODICE -------------------------------------------------------------------------------------------------
#
# dss = py_dss_interface.DSS(r"C:\Program Files\OpenDSS")
# dss_file = r"C:\Users\anton\PycharmProjects\OpenDSS\CityArea.dss"
#
# dss.text(f"compile [{dss_file}")
#
# dss.solution.solve()
#
# converged = dss.solution.converged
#
# # dss.text('Show voltage LN node')
#
# bus = dict()
#
# buses = dss.circuit.buses_names
#
# bus_V = dss.circuit.buses_vmag
#
# # dss.circuit_set_active_element('Load.UG_SERV_AC-LOAD1')
# # print(dss.cktelement_currents())
# # print(dss.cktelement_currents_mag_ang())
#
# print('\n\n')
# # print('Load.UG_SERV_AC-LOAD1')
#
# params = ['currents_mag_ang', 'currents', 'variables_values', 'name', 'property_names', 'variables_names',
#           'cplx_seq_currents', 'cplx_seq_voltages', 'energymeter', 'has_switch_control', 'has_volt_control',
#           'is_terminal_open', 'losses', 'node_order', 'num_conductors', 'num_controls', 'num_phases', 'num_properties',
#           'num_terminals', 'ocp_dev_index', 'ocp_dev_type', 'phase_losses', 'powers', 'bus_names', 'display',
#           'emerg_amps', 'is_enabled', 'norm_amps', 'residuals_currents', 'seq_currents', 'seq_powers', 'seq_voltages',
#           'voltages', 'voltages_mag_ang', 'y_prim']
# print('\n\n')
#
# for e in dss.circuit.elements_names:
#     print(e)
#     vdss[e] = dict()
#     dss.circuit.set_active_element(e)
#     for p in params:
#         # print(p + ' = ' + str(dss.cktelement_currents_mag_ang()))
#         # dss.cktelement_currents_mag_ang()
#         print(p)
#         print(p + ' = ' + str(dss.cktelement.__getattribute__('_' + p)()))
#         # dss.cktelement._is
#         vdss[e][p] = dss.cktelement.__getattribute__('_' + p)()
#
#     print('\n')
#
# # print('kW = ' + str(dss.dssproperties_read_value('kW')))
# # print('kW = ' + str(dss.dssproperties_read_value('Load.UG_SERV_AC-LOAD1')))
#
#
# print(dss.circuit.elements_names)
#
# i = 0
# for i in range(0, len(buses)):
#     bus[buses[i]] = dict()
#     for j in range(0, 3):
#         bus[buses[i]][j + 1] = dict()
#         bus[buses[i]][j + 1]['V'] = bus_V[3 * i + j]
#
# elem = dict()
# elem_names = dss.circuit.elements_names
#
# bus_names = dss.circuit.nodes_names
#
# # for el in elem_names:
# #     elem[el] = dict()
# #     dss.circuit.set_active_element(el)
# #     curr = dss.cktelement._currents_mag_ang()
# #     elem[el]['i'] = dict()
# #     for i in range(0, 3):
# #         elem[el]['i'][i] = curr[i * 2]
# #     elem[el]['i']['n'] = curr[6]
#
# for el in elem_names:
#     [macro_cat, name] = el.split('.')
#     # c = name.split('_')[len(name.split('_'))-1]
#     # print(c, mc[macro_cat])
#     try:
#         cat = c[name.split('_')[len(name.split('_'))-1]]
#     except KeyError:
#         cat = 'undefined'
#
#     print(name + ': ' + cat)
#
#     # print(el, dss.cktelement._property_names())
#
# # for el in elem_names:
# #     if
#
# with open('grid.yml', 'w') as file:
#     yaml.dump(vdss, file)
#     file.close()
# # print('here')
#
# dss.circuit.set_active_element('Load.rs_2_ac-load')
# print('\n\n\n\n')
# print(dss.loads.name)
# print(dss.loads.kw)
# print(dss.loads.names)
#
# dss.circuit.set_active_element('Vsource.source')
# # nodes = dss.cktelement.bus_names
# for node in dss.cktelement.bus_names:
#     if node not in elem.keys():
#         elem[node] = dict()
#         elem[node]['category'] = 'AC-Node'
#         elem[node]['par'] = dict()
#         elem[node]['par']['Vn'] = dss.vsources.base_kv
#         elem[node]['top'] = dict()
#         elem[node]['top']['conn'] = ['source']
#
# unr_conv = []
# unr_line = []
#
# for el in elem_names:
#     dss.circuit.set_active_element(el)
#
#     mcat = str(el).split('.')[0]
#     name = str(el).removeprefix(mcat + '.')
#     cat = name.split('_')[len(name.split('_')) - 1]
#     # if str(el).split('.')[0] == 'Generator':
#     # print(el, mcat, name, cat)
#     if mcat == 'Load':
#         print('break')
#
#     elem[name] = dict()
#     elem[name]['top'] = dict()
#     elem[name]['par'] = dict()
#     elem[name]['top']['conn'] = dss.cktelement.bus_names
#
#     # -- verifica e inizializzazione della busbar ------------
#     for i in [0, len(elem[name]['top']['conn']) - 1]:
#         bus = elem[name]['top']['conn'][i]
#         if bus not in elem.keys():
#             elem[bus] = dict()
#             elem[bus]['category'] = bus
#             elem[bus]['par'] = dict()
#             elem[bus]['par']['Vn'] = None
#             # elem[elem[name]['top']['conn'][1]]['par']['Vn'] = elem[name]['par']['Vn1']
#             elem[bus]['top'] = dict()
#             elem[bus]['top']['conn'] = [name]
#         elif name not in elem[bus]['top']['conn']:
#             elem[bus]['top']['conn'].append(name)
#     # --------------------------------------------------------
#
#     if mcat == 'Generator':
#         dss.generators.name = name
#
#         if cat == 'pv':
#             # print(el, name, dss.generators.name)
#             elem[name]['category'] = 'PV'
#             elem[name]['par']['P'] = dss.generators.kw
#             elem[name]['par']['Vn'] = dss.generators.kv
#             elem[name]['par']['profile'] = dict()
#             elem[name]['par']['profile']['name'] = None
#             elem[name]['par']['profile']['curve'] = 1
#
#         elif cat == 'bess':
#             elem[name]['category'] = 'BESS'
#             elem[name]['par']['Vn'] = dss.generators.kv
#             elem[name]['par']['P'] = dss.generators.kw
#             elem[name]['par']['cap'] = 100
#             elem[name]['par']['eff'] = 1
#
#         elif cat == 'wind':
#             elem[name]['category'] = 'Wind'
#             elem[name]['par']['Vn'] = dss.generators.kv
#             elem[name]['par']['P'] = dss.generators.kw
#             elem[name]['par']['Q'] = dss.generators.kvar
#             elem[name]['par']['f'] = dss.generators.pf
#             elem[name]['par']['eff'] = 1
#             elem[name]['par']['profile'] = dict()
#             elem[name]['par']['profile']['name'] = None
#             elem[name]['par']['profile']['curve'] = 1
#
#         elif cat == 'dc-micro-wind':
#             elem[name]['category'] = 'DC-micro-Wind'
#             elem[name]['par']['Vn'] = dss.generators.kv
#             elem[name]['par']['P'] = dss.generators.kw
#             elem[name]['par']['eff'] = 1
#             elem[name]['par']['profile'] = dict()
#             elem[name]['par']['profile']['name'] = None
#             elem[name]['par']['profile']['curve'] = 1
#
#     elif mcat == 'Transformer':
#         dss.transformers.name = name
#         unr_conv.append(name)
#
#         if cat == 'tr':       # no
#             elem[name]['category'] = '2W-Transformer'
#             bus = 'AC-Node'
#         elif cat == 'pwm':       # no
#             elem[name]['category'] = 'PWM'
#             bus = 'DC-Node'
#         elif cat == 'dc-dc-conv':       # no
#             elem[name]['category'] = '2W-Transformer'
#             bus = 'DC-Node'
#
#         elem[name]['par']['Vn1'] = dss.transformers.kv
#         elem[name]['par']['Sr'] = dss.transformers.kva
#         # elem[name]['par']['Rs'] = dss.transformers.r
#         # elem[name]['par']['Rn'] = dss.transformers.r_neut
#         elem[name]['par']['XHL'] = dss.transformers.xhl
#         # elem[name]['par']['XHT'] = dss.transformers.xht
#         # elem[name]['par']['XLT'] = dss.transformers.xlt
#         elem[elem[name]['top']['conn'][1]]['par']['Vn'] = elem[name]['par']['Vn1']
#
#         # if elem[name]['top']['conn'][1] not in elem.keys():
#         #     elem[elem[name]['top']['conn'][1]] = dict()
#         #     elem[elem[name]['top']['conn'][1]]['category'] = bus
#         #     elem[elem[name]['top']['conn'][1]]['par'] = dict()
#         #     elem[elem[name]['top']['conn'][1]]['top'] = dict()
#         #     elem[elem[name]['top']['conn'][1]]['par']['conn'] = [name]
#         # else:
#         #     elem[elem[name]['top']['conn'][1]]['par']['conn'].append(name)
#
#     elif mcat == 'Load':
#         if cat == 'ac-load':  # ok
#             elem[name]['category'] = 'AC-Load'
#             elem[name]['par']['Q'] = dss.loads.kvar
#             elem[name]['par']['f'] = dss.loads.pf
#
#         elif cat == 'dc-load':
#             elem[name]['category'] = 'DC-Load'
#
#         elem[name]['par']['P'] = dss.loads.kw
#         elem[name]['par']['Vn'] = dss.loads.kv
#         elem[name]['par']['profile'] = dict()
#         elem[name]['par']['profile']['name'] = None
#         elem[name]['par']['profile']['curve'] = 1
#
#     elif mcat == 'Line':     # ok
#         unr_line.append(name)
#
#         if cat == 'line':
#             elem[name]['category'] = 'AC-Load'
#             elem[name]['par']['R0'] = dss.lines.r0
#             elem[name]['par']['X0'] = dss.lines.x0
#             elem[name]['par']['c0'] = dss.lines.c0
#             elem[name]['par']['c1'] = dss.lines.c1
#
#         elif cat == 'dc-line':
#             elem[name]['category'] = 'DC-Load'
#
#         elem[name]['par']['length'] = dss.lines.length
#         elem[name]['par']['R1'] = dss.lines.r1
#         elem[name]['par']['X1'] = dss.lines.x1
#         elem[name]['par']['In'] = dss.lines.norm_amps
#
#         # for i in [0, 1]:
#         #     bus = elem[name]['top']['conn'][i]
#         #     if bus not in elem.keys():
#         #         elem[bus] = dict()
#         #         elem[bus]['category'] = bus
#         #         elem[bus]['par'] = dict()
#         #         # elem[elem[name]['top']['conn'][1]]['par']['Vn'] = elem[name]['par']['Vn1']
#         #         elem[bus]['top'] = dict()
#         #         elem[bus]['par']['conn'] = [name]
#         #     else:
#         #         elem[bus]['par']['conn'].append(name)
#
# while unr_conv + unr_line != []:
#     print(unr_conv, unr_line)
#
#     for name in unr_conv:
#         if elem[name]['top']['conn'][0] in elem.keys():
#             bus = elem[name]['top']['conn'][0]
#             if elem[bus]['par']['Vn']:
#                 elem[name]['par']['Vn0'] = elem[bus]['par']['Vn']
#                 unr_conv.remove(name)
#
#     for name in unr_line:
#         v = None
#         bus2 = None
#         if elem[name]['top']['conn'][0] in elem.keys():
#             bus = elem[name]['top']['conn'][0]
#             if elem[bus]['par']['Vn']:
#                 v = elem[bus]['par']['Vn']
#                 bus2 = elem[name]['top']['conn'][1]
#
#         elif elem[name]['top']['conn'][1] in elem.keys():
#             bus = elem[name]['top']['conn'][1]
#             if elem[bus]['par']['Vn']:
#                 v = elem[bus]['par']['Vn']
#                 bus2 = elem[name]['top']['conn'][0]
#
#         if v:
#             elem[name]['par']['Vn'] = v
#             elem[bus2]['par']['Vn'] = v
#             unr_line.remove(name)
#
# print('done')
#
# with open('CityArea.yml', 'w') as file:
#     yaml.dump(elem, file)
#     file.close()
#
# dss.circuit.set_active_element('Load.ug_dc-load')
# print(dss.cktelement.name)
# dss.cktelement.enabled(False)
# print(dss.cktelement.has_switch_control)
#
#
# dss.circuit.set_active_element('Transformer.ugs_pwm')
# print(dss.cktelement.name)
# dss.cktelement.enabled(True)
# print(dss.cktelement.has_switch_control)
#
# print(dss.cktelement.is_enabled)
#
# dss.circuit.set_active_element('Line.ug_line')
#
# print(dss.cktelement.name, dss.cktelement.has_switch_control, dss.lines.geometry)
#
# dss.solution.solve()
#
# dss.circuit.set_active_element('Vsource.source')
# print(dss.cktelement.powers)
#
# # -------------------------------------------------------------------------------------------------------------------
#
#

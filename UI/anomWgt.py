try:
    from UI.ui_anomWgt import *
except:
    from ui_anomWgt import *


from PySide2 import QtGui, QtCore, QtWidgets
# from PyQt5 import QtWidgets, QtGui, QtCore
import yaml
from variables import *


class AnomWgt(QtWidgets.QWidget):
    def __init__(self, cat):
        super(AnomWgt, self).__init__()
        self.ui = Ui_mainAnomWgt()
        self.ui.setupUi(self)

        self.cat = cat

        self.defdict = yaml.safe_load(open(mainpath + '/_temp/Functionalities/Anomalies/default.yml'))[self.cat]
        self.defdict.pop('Hourly_Degradation')
        #
        # self.anom_typol_par = {
        #     'scale': 'value',
        #     '(1-exp) decrease': 'alpha',
        #     '(-x+1) decrease': 'alpha'
        # }

        # self.ui.typeWgt.setVisible(False)
        # self.ui.anomParWgt.setVisible(False)
        self.ui.detailsPbWgt.setVisible(False)

        # self.type_changed()

    def ui_actions(self):
        self.ui.catCB.currentTextChanged.connect(self.cat_changed)
        self.ui.typeCB.currentTextChanged.connect(self.type_changed)

    def cat_changed(self):
        self.ui.anomLbl.setText(self.ui.catCB.currentText())

        cat = self.ui.catCB.currentText()

        self.ui.typeCB.currentTextChanged.disconnect()
        self.ui.typeCB.clear()
        self.ui.typeCB.currentTextChanged.connect(self.type_changed)
        try:
            self.ui.typeCB.insertItems(0, list(self.defdict[cat].keys()))
        except: pass
        # self.ui.typeCB.currentTextChanged.connect(self.type_changed)

    def type_changed(self):
        cat = self.ui.catCB.currentText()
        typol = self.ui.typeCB.currentText()

        par = anom_typol_par[typol]
        self.ui.parLbl.setText(anom_typol_par[typol])

        self.ui.lbdaDsb.setValue(self.defdict[cat][typol]['lambda_a'])
        self.ui.lbddurDsb.setValue(self.defdict[cat][typol]['lambda_duration'])
        self.ui.parDsb.setValue(self.defdict[cat][typol][anom_typol_par[typol]])
        self.ui.fixCkb.setChecked(self.defdict[cat][typol]['is_fixed'])


    def test(self):
        print('cliccato')

import datetime

from fpdf import FPDF
import os
import yaml
from variables import *
from pathlib import Path
# from PyQt5 import QtWidgets
from PySide2 import QtWidgets
import copy
from PIL import Image
import unicodedata as ud

root = os.getcwd()

# -- Cells and rows parameters -------------------
t1_h, t1_c, t1_ls, t1_s = 10, 16, 12, "B"  # Title 1 (height, font_size, line spacing, style)
t2_h, t2_c, t2_ls, t2_s = 4, 10, 12, "B"  # Title 2 (height, font_size, line spacing, style)
e_h, e_c, e_ls, e_s = 4, 8, 10, "B"  # Emphasis (height, font_size, line spacing, style)
p_h, p_c, p_ls, p_s = 3, 6, 8, ""  # Paragraph (height, font_size, line spacing, style)
i_h, i_c, i_ls, i_s = 3, 6, 8, "I"  # Captions (height, font_size, line spacing, style)
e_w, p_w, d_w = 35, 5, 17  # Cells width (element, port, data)
# ------------------------------------------------

par = dict()
par['Nodi AC'] = [['Vn'], ['Vn [kV]']]
par['Nodi DC'] = [['Vn'], ['Vn [kV]']]
par['Carichi AC'] = [['P', 'cosPhi', 'Vn'], ['P [kW]', 'cosPhi', 'Vn [kV]']]
par['Carichi DC'] = [['P', 'Vn'], ['P [kW]', 'Vn [kV]']]
par['PWM'] = [['Sr', 'VnAC', 'VnDC'], ['Sr [kVA]', 'Vn AC [kV]', 'Vn DC [kV]']]
par['Convertitori DC-DC'] = [['Sr', 'VnH', 'VnL'], ['Sr [kVA]', 'Vn HV [kV]', 'Vn LV [kV]']]
par['Trasformatori'] = [['Sr', 'VnH', 'VnL', 'Rs0', 'Rs1', 'XHL', 'imag'],
                        ['Sr [kVA]', 'Vn HV [kV]', 'Vn LV [kV]', 'Rs0 [p.u.]', 'Rs1 [p.u.]', 'XHL [p.u.]',
                         'imag [p.u.]']]
par['Fotovoltaico AC'] = [['P', 'Vn', 'eff'], ['Pn [kVA]', 'Vn [kV]', 'eff. [p.u.]']]
par['Fotovoltaico DC'] = [['P', 'Vn', 'eff'], ['Pn [kVA]', 'Vn [kV]', 'eff. [p.u.]']]
par['Eolici AC'] = [['P', 'cosPhi', 'eff', 'Vn'], ['P [kW]', 'cosPhi', 'eff [p.u.]', 'Vn [kV]']]
par['Eolici DC'] = [['P', 'eff', 'Vn'], ['P [kW]', 'eff [p.u.]', 'Vn [kV]']]
par['Batterie AC'] = [['cap', 'SOC', 'P', 'eff', 'Vn'],
                      ['Capacità [kWh]', 'S.o.C. [p.u.]', 'P [kW]', 'eff [p.u.]', 'Vn [kV]']]
par['Batterie DC'] = [['cap', 'SOC', 'P', 'eff', 'Vn'],
                      ['Capacità [kWh]', 'S.o.C. [p.u.]', 'P [kW]', 'eff [p.u.]', 'Vn [kV]']]
par['Linee AC'] = [['length', 'In', 'R1', 'X1', 'B1', 'R0', 'X0', 'B0'],
                   ['Lunghezza [m]', 'In [A]', 'R1 [Ohm/km]', 'X1 [Ohm/km]', 'B1 [uS/km]',
                    'R0 [Ohm/km]', 'X0 [Ohm/km]', 'B0 [uS/km]']]
par['Linee DC'] = [['length', 'In', 'R1', 'X1'],
                   ['Lunghezza [m]', 'In [A]', 'R [Ohm/km]', 'X [Ohm/km]']]

par['Switch'] = [[], []]

lf = dict()
lf['Nodi'] = [['v'], ['V [kV]'], 1]
lf['Periferiche'] = [['p', 'q', 'i', 'v'], ['P [kW]', 'Q [kVA]', 'I [A]', 'V [kV]'], 1]
lf['Links'] = [['p', 'q', 'i', 'v'], ['P [kW]', 'Q [kVA]', 'I [A]', 'V [kV]'], 2]

prot = [['type', 'cost', 'soglia_I', 'soglia_Vmax', 'soglia_Vmin', 'delay_I', 'delay_Vmax', 'delay_Vmin'],
        ['Tipologia', 'Costo [Euro]', 'Soglia I [A]', 'Soglia Vmax [kV]', 'Soglia Vmin [kV]',
         'Ritardo I [ms]', 'Ritardo Vmax [ms]', 'Ritardo Vmin [ms]']]

rel_par = [['t_preg', 'alfa', 'beta', 'Pi_E', 'Pi_Q'],
           ['Vita pregressa [h]', 'alfa [-]', 'beta [-]', 'Pi_E [-]', 'Pi_Q [-]']]
rel_other = [['lambda', 'Pi_Si', 'MTBF_ore', 'MTBF_anni'],
             ['lambda [fail./h]', 'Pi_Si', 'MTBF [ore]', 'MTBF [anni]']]
rel_loads = [['load_rel', 'load_rel1'], ['Aff. (giorno) [-]', 'Aff. (notte) [-]']]

ctrl = [['ris1', 'ris2', 'ris3', 'ti', 'ens', 'ng', 'st', 'gf', 'ri'],
        ['Indice di autonomia [%]', 'Indice di flessibilità [%]', 'Indice di modulazione', 'Tempo (Ti) [min]',
         'Energia non fornita (ENS)', 'Generazione flessibile (Ng)', 'Riserva dello Storage (ST)',
         'Capacità di Grid Forming (GF)', 'Rapporto di inerzia (RI)']]

anom_par = [[]]

cat = dict()
cat['AC-Node'] = 'Nodi AC'
cat['DC-Node'] = 'Nodi DC'
cat['AC-Load'] = 'Carichi AC'
cat['DC-Load'] = 'Carichi DC'
cat['PWM'] = 'PWM'
cat['DC-DC-Converter'] = 'Convertitori DC-DC'
cat['2W-Transformer'] = 'Trasformatori'
cat['AC-PV'] = 'Fotovoltaico AC'
cat['DC-PV'] = 'Fotovoltaico DC'
cat['AC-Wind'] = 'Eolici AC'
cat['DC-Wind'] = 'Eolici DC'
cat['AC-BESS'] = 'Batterie AC'
cat['DC-BESS'] = 'Batterie DC'
cat['AC-Line'] = 'Linee AC'
cat['DC-Line'] = 'Linee DC'
cat['Switch'] = 'Switch'


class PDF(FPDF):
    def __init__(self, sel, tlf=0, ds=None):
        super(PDF, self).__init__()

        # elements = copy.deepcopy(v.elements)

        self.page_name = ''

        elem_cat = dict()

        for el in v:
            c = v[el]['category']
            if c != 'ExternalGrid':
                if c not in elem_cat.keys():
                    elem_cat[c] = dict()
                elem_cat[v[el]['category']][el] = copy.deepcopy(v[el])
                if c == '2W-Transformer':
                    elem_cat[c][el]['par']['Sr'] = elem_cat[c][el]['par']['Sr'][0]
                    elem_cat[c][el]['par']['VnH'] = elem_cat[c][el]['par']['Vn'][0]
                    elem_cat[c][el]['par']['VnL'] = elem_cat[c][el]['par']['Vn'][1]
                    del elem_cat[c][el]['par']['Vn']
                    elem_cat[c][el]['par']['Rs0'] = elem_cat[c][el]['par']['Rs'][0]
                    elem_cat[c][el]['par']['Rs1'] = elem_cat[c][el]['par']['Rs'][1]
                    del elem_cat[c][el]['par']['Rs']
                elif c in mc['Node'] + mc['Load'] + mc['Generator']:
                    elem_cat[c][el]['par']['Vn'] = elem_cat[c][el]['par']['Vn'][0]
                elif c == 'DC-DC-Converter':
                    elem_cat[c][el]['par']['Sr'] = elem_cat[c][el]['par']['Sr'][0]
                    elem_cat[c][el]['par']['VnH'] = elem_cat[c][el]['par']['Vn'][0]
                    elem_cat[c][el]['par']['VnL'] = elem_cat[c][el]['par']['Vn'][1]
                    del elem_cat[c][el]['par']['Vn']
                elif c == 'PWM':
                    elem_cat[c][el]['par']['Sr'] = elem_cat[c][el]['par']['Sr'][0]
                    elem_cat[c][el]['par']['VnAC'] = elem_cat[c][el]['par']['Vn'][0]
                    elem_cat[c][el]['par']['VnDC'] = elem_cat[c][el]['par']['Vn'][1]
                    del elem_cat[c][el]['par']['Vn']

        self.set_draw_color(226, 226, 226)

        self.cover()
        if 'par' in sel:
            self.parameters(elem_cat)
        if 'lf' in sel:
            self.loadflow(elem_cat=elem_cat, tlf=tlf, ds=ds)
        if 'rel' in sel:
            self.reliability(elem_cat=elem_cat)
        if 'anom' in sel:
            self.anomalies()
        if 'adeq' in sel:
            self.adequacy()
        if 'onr' in sel:
            self.onr(elem_cat=elem_cat, elements='')
        if 'optstor' in sel:
            self.optimal_storage()

    #
    def del_PDF(self, filepath='mypdf.pdf'):
        try:
            os.remove(filepath)
        except:
            pass

    def header(self):
        if self.page_no() > 1:
            self.image(mainpath + '/_images/ARStool500.png', 8, 8, 20, 20)
            self.set_font('Arial', 'B', t1_c)
            self.set_xy(34, 18)
            self.set_text_color(217, 193, 221)
            self.write(0, 'Adequacy, ')
            self.set_font('Arial', 'B', t1_c)
            self.set_text_color(194, 214, 236)
            self.write(0, 'Reliability')

            self.set_xy(34, 25)
            self.set_font('Arial', '', t1_c)
            self.write(0, 'and ')
            self.set_text_color(204, 191, 233)
            self.write(0, 'Security ')
            self.set_text_color(240, 233, 173)
            self.write(0, 'Tool')

            self.set_xy(150, self.get_y() - t1_h)
            self.set_font('Arial', 'B', t1_c)
            self.set_text_color(0, 0, 0)
            self.cell(50, t1_h * 2, grid['name'], 0, 0, 'R')

            self.set_draw_color(0, 0, 0)
            self.set_line_width(0.5)
            self.line(0, 30, 210, 30)

            self.set_y(40)

    #
    def footer(self):
        if self.page_no() > 1:
            self.set_draw_color(0, 0, 0)
            self.set_line_width(0.5)
            self.line(0, 280, 210, 280)
            self.set_xy(10, 282)
            self.set_font('Arial', 'B', t2_c)
            self.set_text_color(0, 0, 0)
            self.cell(95, t2_h, self.page_name, 0, 0, 'L')
            self.cell(95, t2_h, 'Pagina ' + str(self.page_no()), 0, 0, 'R')

    #
    def cover(self):
        self.add_page()
        self.set_font('Arial', t1_s, 1.5 * t1_c)
        self.image(mainpath + '/_images/ARStool500.png', 55, 80, 100, 100)
        self.set_xy(60, 190)
        self.set_text_color(204, 191, 233)
        self.write(0, 'Adequacy, ')
        self.set_text_color(194, 214, 236)
        self.write(0, 'Reliability')
        self.set_xy(65, 200)
        self.set_font('Arial', '', 1.5 * t1_c)
        self.write(0, 'and ')
        self.set_text_color(217, 193, 221)
        self.set_font('Arial', 'B', 1.5 * t1_c)
        self.write(0, 'Security ')
        self.set_text_color(240, 233, 173)
        self.write(0, 'Tool')

        self.set_xy(20, 230)
        self.set_text_color(0, 0, 0)
        self.cell(170, 1.5 * t1_h, grid['name'], 0, 0, 'C')

    #
    def parameters(self, elem_cat):
        self.add_page()

        self.page_name = 'Parametri'

        self.set_font('Arial', t1_s, t1_c)
        self.write(0, 'Parametri')
        self.ln(t1_ls)

        for c in elem_cat:
            line_length = e_w + d_w * (len(par[cat[c]][1]) + 1)
            if 275 < self.get_y() + t2_h + i_h + p_h * len(elem_cat[c].items()):
                self.add_page()
            self.set_font('Arial', t2_s, t2_c)
            self.write(0, cat[c])
            self.ln(t2_h)
            self.set_font('Arial', i_s, i_c)
            self.set_fill_color(226, 226, 226)
            self.cell(e_w, i_h, 'Elemento', 1, 0, 'C', fill=True)
            for e in par[cat[c]][1]:
                self.cell(d_w, i_h, e, 1, 0, 'C', fill=True)
            if c not in mc['Node']:
                self.cell(d_w, i_h, 'out-of-serv.', 1, 0, 'C', fill=True)
            self.ln(i_h)

            self.set_font('Arial', p_s, p_c)
            for e in elem_cat[c]:
                self.cell(e_w, p_h, e, 0, 0, 'L')
                for item in par[cat[c]][0]:
                    try:
                        self.cell(d_w, p_h, '%.3f' % elem_cat[c][e]['par'][item], 0, 0, 'C')
                    except:
                        pass
                if c not in mc['Node']:
                    self.cell(d_w, p_h, str(elem_cat[c][e]['par']['out-of-service']), 0, 0, 'C')
                self.ln(p_h)
                self.line(self.get_x() + 1, self.get_y(), self.get_x() + line_length - 2, self.get_y())
            self.ln(p_ls)

    #
    def loadflow(self, elem_cat, tlf=0, ds=None):
        self.add_page()
        self.page_name = 'LoadFlow'

        # todo: da riattivare con l'immagine giusta
        img_path = mainpath + '/UI/_resources/icons/loadFlow.png'
        self.set_xy(12, 35)
        self.set_fill_color(0)
        self.set_draw_color(255, 170, 0)
        self.rect(self.get_x() - 2, self.get_y() - 2, 19, 19, style='FD')
        self.image(img_path, self.get_x(), self.get_y(), 15, 15)
        self.set_xy(37.5, 44)

        self.set_draw_color(25, 25, 25)
        self.set_line_width(0.3)
        self.line(35, 38, 195, 38)
        self.line(35, 48, 195, 48)

        self.set_font('Arial', t1_s, t1_c)
        self.write(0, 'LoadFlow')
        self.ln(t1_ls)

        if ds:
            day = (str(ds.date().day()) + '/' + str(ds.date().month()) + '/' + str(ds.date().year()) + '  -  ' +
                   ('%02i:%02i' % (ds.time().hour(), ds.time().minute())))
            self.set_font('Arial', t2_s, t2_c)
            self.write(0, 'LoadFlow relativo a:  ' + day)
            self.ln(t2_ls)

        p_loads, q_loads, p_gen, q_gen, p_bess, q_bess, p_eg, q_eg, p_loss, q_loss = self.loadflow_results(tlf)
        self.set_font('Arial', 'I', t2_c)
        self.write(0, 'Potenza dalla rete esterna:  ')
        self.set_font('Arial', t2_s, t2_c)
        self.write(0, 'P = %.1f kW - Q = %.1f kVA' % (p_eg, q_eg))
        self.ln(t2_ls)

        self.set_font('Arial', 'I', t2_c)
        self.write(0, 'Potenza prelevata dai carichi:  ')
        self.set_font('Arial', t2_s, t2_c)
        self.write(0, 'P = %.1f kW - Q = %.1f kVA' % (p_loads, q_loads))
        self.ln(t2_h)

        self.set_font('Arial', 'I', t2_c)
        self.write(0, 'Potenza generata:  ')
        self.set_font('Arial', t2_s, t2_c)
        self.write(0, 'P = %.1f kW - Q = %.1f kVA' % (p_gen, q_gen))
        self.ln(t2_h)

        self.set_font('Arial', 'I', t2_c)
        self.write(0, 'Potenza dai sistemi di accumulo:  ')
        self.set_font('Arial', t2_s, t2_c)
        self.write(0, 'P = %.1f kW - Q = %.1f kVA' % (p_bess, q_bess))
        self.ln(t2_ls)

        self.set_font('Arial', 'I', t2_c)
        self.write(0, 'Potenza dissipata:  ')
        self.set_font('Arial', t2_s, t2_c)
        self.write(0, 'P = %.1f kW - Q = %.1f kVA' % (p_loss, q_loss))
        self.ln(3 * t2_ls)

        for c in elem_cat:
            if c in ['AC-Node', 'DC-Node']:
                captions = lf['Nodi']
                node, line = '', 1

            elif c in ['2W-Transformer', 'AC-Line', 'DC-Line', 'PWM', 'DC-DC-Converter']:
                captions = lf['Links']
                node, line = 'Nodo', 2
            else:
                captions = lf['Periferiche']
                node, line = '', 1

            if 275 < self.get_y() + t2_h + i_h + p_h * len(elem_cat[c].items()) * line:
                self.add_page()
            self.set_font('Arial', t2_s, t2_c)
            self.write(0, cat[c])
            self.ln(t2_h)
            self.set_font('Arial', i_s, i_c)
            self.set_fill_color(226, 226, 226)
            self.cell(e_w, i_h, 'Elemento', 1, 0, 'C', fill=True)
            self.cell(p_w, i_h, node, 1, 0, 'C', fill=True)

            line_length = e_w + p_w + d_w * len(captions[1])

            for e in captions[1]:
                self.cell(d_w, i_h, e, 1, 0, 'C', fill=True)
            self.ln(i_h)

            self.set_font('Arial', p_s, p_c)
            for e in elem_cat[c]:
                if node != '':
                    self.cell(e_w, 2 * p_h, e, 0, 0, 'L')
                    if c in ['2W-Transformer', 'DC-DC_Conv']:
                        nodes = ['HV', 'LV']
                    elif c == 'PWM':
                        nodes = ['AC', 'DC']
                    else:
                        nodes = ['1', '2']

                    for n in [1, 2]:
                        if n == 2:
                            self.cell(e_w, p_h, '', 0, 0, 'C')
                        self.cell(p_w, p_h, nodes[n - 1], 0, 0, 'C')
                        for item in captions[0]:
                            try:
                                data = '%.3f' % elem_cat[c][e]['lf'][item][n - 1][tlf]
                            except:
                                data = ''
                            self.cell(d_w, p_h, data, 0, 0, 'C')
                        if n == 1:
                            self.ln(p_h)

                    self.set_xy(self.get_x(), self.get_y() - p_h)
                    self.ln(2 * p_h)

                else:
                    self.cell(e_w, p_h, e, 0, 0, 'L')
                    self.cell(p_w, p_h, '', 0, 0, 'C')

                    for item in captions[0]:
                        try:
                            if item in captions[0]:
                                data = '%.3f' % elem_cat[c][e]['lf'][item][tlf]
                            else:
                                data = str(elem_cat[c][e]['lf'][item][tlf])
                        except:
                            data = ''
                        self.cell(d_w, p_h, data, 0, 0, 'C')
                    self.ln(p_h)
                self.set_draw_color(226, 226, 226)
                self.line(self.get_x() + 1, self.get_y(), self.get_x() + line_length - 2, self.get_y())

            self.ln(p_ls)

    def loadflow_results(self, t=0):
        p_loads, q_loads = 0, 0
        p_gen, q_gen = 0, 0
        p_bess, q_bess = 0, 0

        for elem in v.keys():
            if v[elem]['category'] in mc['Load']:
                p_loads += v[elem]['lf']['p'][t]
                q_loads += v[elem]['lf']['q'][t]

            elif v[elem]['category'] in mc['BESS']:
                p_bess += v[elem]['lf']['p'][t]
                q_bess += v[elem]['lf']['q'][t]

            elif v[elem]['category'] in mc['Generator']:
                p_gen -= v[elem]['lf']['p'][t]
                q_gen -= v[elem]['lf']['q'][t]

        p_eg, q_eg = -v['source']['lf']['p'][t], -v['source']['lf']['q'][t]
        p_loss = p_eg + p_gen - p_loads - p_bess
        q_loss = q_eg + q_gen - q_loads - q_bess

        return p_loads, q_loads, p_gen, q_gen, p_bess, q_bess, p_eg, q_eg, p_loss, q_loss

    #
    def optimal_storage(self):
        self.add_page()
        self.page_name = 'Optimal Storage'

        img_path = mainpath + '/UI/_resources/icons/storage.png'
        self.set_xy(12, 35)
        self.set_fill_color(0)
        self.set_draw_color(255, 170, 0)
        self.rect(self.get_x() - 2, self.get_y() - 2, 19, 19, style='FD')
        self.image(img_path, self.get_x(), self.get_y(), 15, 15)
        self.set_xy(37.5, 44)

        self.set_draw_color(25, 25, 25)
        self.set_line_width(0.3)
        self.line(35, 38, 195, 38)
        self.line(35, 48, 195, 48)

        self.set_font('Arial', t1_s, t1_c)
        self.write(0, 'Optimal storage')
        self.ln(t1_ls)

        # -- Parametri ------------------------------------------------------------------------------------------------
        self.set_font('Arial', t2_s, t2_c)
        self.write(0, 'Parametri')
        self.ln(t2_h * 1.5)

        # -- Input --------------------------------------------------------------
        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Input')
        self.ln(e_h)

        self.set_font('Arial', i_s, i_c)
        self.set_fill_color(226, 226, 226)
        self.cell(e_w + d_w, i_h, 'Parametro', 0, 0, 'C', fill=True)
        self.cell(d_w, i_h, 'Valore', 0, 0, 'C', fill=True)
        self.ln(i_h)

        for p in opt_stor['par']['Input']:
            self.set_font('Arial', i_s, i_c)
            self.cell(e_w + d_w, p_h, opt_stor['par']['Input'][p]['lbl'], 0, 0, 'L')
            self.set_font('Arial', p_s, p_c)
            self.cell(d_w, p_h, ('%.2f ' % opt_stor['par']['Input'][p]['val']) + opt_stor['par']['Input'][p]['unit'],
                      0, 0, 'R')
            self.ln(p_h)
        self.ln(e_h * 3)
        # -----------------------------------------------------------------------

        # -- Scenario -----------------------------------------------------------
        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Scenario ' + str(opt_stor['par']['Scenario'][0]['year']['val']) + ' ' +
                   opt_stor['par']['Scenario'][0]['scen']['val'])
        self.ln(e_h)

        self.set_font('Arial', i_s, i_c)
        self.set_fill_color(226, 226, 226)
        self.cell(e_w, i_h, 'Parametro', 0, 0, 'C', fill=True)
        self.cell(d_w, i_h, 'Valore', 0, 0, 'C', fill=True)
        self.cell(d_w, i_h, 'Percentuale', 0, 0, 'C', fill=True)
        self.ln(i_h)

        for i in range(1, 5):
            for p in opt_stor['par']['Scenario'][i]:
                self.set_font('Arial', i_s, i_c)
                self.cell(e_w, p_h, opt_stor['par']['Scenario'][i][p]['lbl'], 0, 0, 'L')
                self.set_font('Arial', p_s, p_c)
                # val =
                self.cell(d_w, p_h,
                          ('%.2f ' % opt_stor['par']['Scenario'][i][p]['val']) +
                          opt_stor['par']['Scenario'][i][p]['unit'],
                          0, 0, 'R')
                try:
                    self.cell(d_w, p_h, ('%.2f%%' % opt_stor['par']['Scenario'][i][p]['perc']), 0, 0, 'R')
                except:
                    self.cell(d_w, p_h, '-', 0, 0, 'R')
                self.ln(p_h)
            self.ln(p_h)
        self.ln(e_h)
        # -----------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------------

        # -- Risultati ------------------------------------------------------------------------------------------------
        self.add_page()
        self.page_name = 'Optimal Storage'

        self.set_font('Arial', t2_s, t2_c)
        self.write(0, 'Risultati')
        self.ln(t2_h * 1.5)

        # -- Fabbisogno----------------------------------------------------------
        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Fabbisogno')
        self.ln(e_h)

        self.set_font('Arial', i_s, i_c)
        self.set_fill_color(226, 226, 226)
        self.cell(e_w, i_h, '', 0, 0, 'C', fill=True)
        self.cell(2 * d_w, i_h, 'Valori', 0, 0, 'C', fill=True)
        self.ln(i_h)
        self.set_fill_color(226, 226, 226)
        self.cell(e_w, i_h, 'Parametro', 0, 0, 'C', fill=True)
        self.cell(d_w, i_h, 'Attuale', 0, 0, 'C', fill=True)
        self.cell(d_w, i_h, 'Prospettico', 0, 0, 'C', fill=True)
        self.ln(i_h)

        for p in opt_stor['res']['Fabbisogno'][0]:
            self.set_font('Arial', i_s, i_c)
            self.cell(e_w, p_h, opt_stor['res']['Fabbisogno'][0][p]['lbl'], 0, 0, 'L')
            self.set_font('Arial', p_s, p_c)
            self.cell(d_w, p_h, ('%.2f ' % opt_stor['res']['Fabbisogno'][0][p]['val_act']) +
                      opt_stor['res']['Fabbisogno'][0][p]['unit'],
                      0, 0, 'R')
            self.cell(d_w, p_h, ('%.2f ' % opt_stor['res']['Fabbisogno'][0][p]['val_prosp']) +
                      opt_stor['res']['Fabbisogno'][0][p]['unit'],
                      0, 0, 'R')
            self.ln(p_h)
        self.ln(e_h * 3)
        # -----------------------------------------------------------------------

        # -- Rinnovabili --------------------------------------------------------
        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Rinnovabili')
        self.ln(e_h)

        self.set_font('Arial', i_s, i_c)
        self.set_fill_color(226, 226, 226)
        self.cell(e_w, i_h, '', 0, 0, 'C', fill=True)
        self.cell(d_w * 2, i_h, 'Attuale', 0, 0, 'C', fill=True)
        self.cell(d_w * 2, i_h, 'Prospettico', 0, 0, 'C', fill=True)
        self.ln(i_h)
        self.set_fill_color(226, 226, 226)
        self.cell(e_w, i_h, 'Parametro', 0, 0, 'C', fill=True)
        self.cell(d_w, i_h, 'Valore', 0, 0, 'R', fill=True)
        self.cell(d_w, i_h, 'Percentuale', 0, 0, 'L', fill=True)
        self.cell(d_w, i_h, 'Valore', 0, 0, 'R', fill=True)
        self.cell(d_w, i_h, 'Percentuale', 0, 0, 'L', fill=True)
        self.ln(i_h)

        for i in opt_stor['res']['Rinnovabili']:
            for p in opt_stor['res']['Rinnovabili'][i]:
                self.set_font('Arial', i_s, i_c)
                self.cell(e_w, p_h, opt_stor['res']['Rinnovabili'][i][p]['lbl'], 0, 0, 'L')
                self.set_font('Arial', p_s, p_c)
                self.cell(d_w, p_h,
                          ('%.2f ' % opt_stor['res']['Rinnovabili'][i][p]['val_act']) +
                          opt_stor['res']['Rinnovabili'][i][p]['unit'],
                          0, 0, 'R')
                try:
                    self.cell(d_w, p_h, ('%.2f%%' % opt_stor['res']['Rinnovabili'][i][p]['perc_act']), 0, 0, 'L')
                except:
                    self.cell(d_w, p_h, '-', 0, 0, 'R')
                self.cell(d_w, p_h,
                          ('%.2f ' % opt_stor['res']['Rinnovabili'][i][p]['val_prosp']) +
                          opt_stor['res']['Rinnovabili'][i][p]['unit'],
                          0, 0, 'R')
                try:
                    self.cell(d_w, p_h, ('%.2f%%' % opt_stor['res']['Rinnovabili'][i][p]['perc_prosp']), 0, 0, 'L')
                except:
                    self.cell(d_w, p_h, '-', 0, 0, 'R')

                self.ln(p_h)
            self.ln(p_h)
        self.ln(e_h * 3)
        # -----------------------------------------------------------------------

        # -- Accumuli -----------------------------------------------------------
        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Accumuili')
        self.ln(e_h)

        self.set_font('Arial', i_s, i_c)
        self.set_fill_color(226, 226, 226)
        self.cell(e_w + d_w, i_h, 'Parametro', 0, 0, 'C', fill=True)
        self.cell(d_w, i_h, 'Val. Prospettico', 0, 0, 'C', fill=True)
        self.ln(i_h)

        self.set_font('Arial', i_s, i_c)
        self.cell(e_w + d_w, p_h, 'Sistemi di stoccaggio (ipotesi TERNA)', 0, 0, 'L')
        self.set_font('Arial', p_s, p_c)
        self.cell(d_w, p_h, ('%.2f ' % opt_stor['res']['Accumuli']['sysStor']['val']) +
                  opt_stor['res']['Accumuli']['sysStor']['unit'],
                  0, 0, 'R')
        self.ln(e_h * 3)
        # -----------------------------------------------------------------------

        # -- Idrogeno -----------------------------------------------------------
        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Idrogeno')
        self.ln(e_h)

        self.set_font('Arial', i_s, i_c)
        self.set_fill_color(226, 226, 226)
        self.cell(e_w, i_h, '', 0, 0, 'C', fill=True)
        self.cell(2 * d_w, i_h, 'Valori', 0, 0, 'C', fill=True)
        self.ln(i_h)
        self.set_fill_color(226, 226, 226)
        self.cell(e_w, i_h, 'Parametro', 0, 0, 'C', fill=True)
        self.cell(d_w, i_h, 'Alta', 0, 0, 'C', fill=True)
        self.cell(d_w, i_h, 'Bassa', 0, 0, 'C', fill=True)
        self.ln(i_h)

        for p in opt_stor['res']['Idrogeno']:
            self.set_font('Arial', i_s, i_c)
            self.cell(e_w, p_h, opt_stor['res']['Idrogeno'][p]['lbl'], 0, 0, 'L')
            self.set_font('Arial', p_s, p_c)
            # val =
            self.cell(d_w, p_h, ('%.2f ' % opt_stor['res']['Idrogeno'][p]['val_HI']) +
                      opt_stor['res']['Idrogeno'][p]['unit'],
                      0, 0, 'R')
            self.cell(d_w, p_h, ('%.2f ' % opt_stor['res']['Idrogeno'][p]['val_LO']) +
                      opt_stor['res']['Idrogeno'][p]['unit'],
                      0, 0, 'R')
            self.ln(p_h)
        self.ln(e_h * 3)
        # -----------------------------------------------------------------------

        # -- Costi --------------------------------------------------------------
        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Costi')
        self.ln(e_h)

        self.set_font('Arial', i_s, i_c)
        self.set_fill_color(226, 226, 226)
        self.cell(e_w + d_w, i_h, 'Parametro', 0, 0, 'C', fill=True)
        self.cell(d_w, i_h, 'Val. Prospettici', 0, 0, 'C', fill=True)
        self.ln(i_h)

        for p in opt_stor['res']['Costi']:
            self.set_font('Arial', i_s, i_c)
            self.cell(e_w + d_w, p_h, opt_stor['res']['Costi'][p]['lbl'], 0, 0, 'L')
            self.set_font('Arial', p_s, p_c)
            # val =
            self.cell(d_w, p_h, ('%.2f ' % opt_stor['res']['Costi'][p]['val']) +
                      opt_stor['res']['Costi'][p]['unit'],
                      0, 0, 'R')
            self.ln(p_h)
        self.ln(e_h * 3)
        # -----------------------------------------------------------------------

        # -- Emissioni ----------------------------------------------------------
        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Emissioni')
        self.ln(e_h)

        self.set_font('Arial', i_s, i_c)
        self.set_fill_color(226, 226, 226)
        self.cell(e_w, i_h, '', 0, 0, 'C', fill=True)
        self.cell(2 * d_w, i_h, 'Valori', 0, 0, 'C', fill=True)
        self.ln(i_h)
        self.set_fill_color(226, 226, 226)
        self.cell(e_w, i_h, 'Parametro', 0, 0, 'C', fill=True)
        self.cell(d_w, i_h, 'Attuale', 0, 0, 'C', fill=True)
        self.cell(d_w, i_h, 'Prospettico', 0, 0, 'C', fill=True)
        self.ln(i_h)

        for p in opt_stor['res']['Emissioni']:
            self.set_font('Arial', i_s, i_c)
            self.cell(e_w, p_h, opt_stor['res']['Emissioni'][p]['lbl'], 0, 0, 'L')
            self.set_font('Arial', p_s, p_c)
            self.cell(d_w, p_h, ('%.2f ' % opt_stor['res']['Emissioni'][p]['val_act']) +
                      opt_stor['res']['Emissioni'][p]['unit'],
                      0, 0, 'R')
            self.cell(d_w, p_h, ('%.2f ' % opt_stor['res']['Emissioni'][p]['val_prosp']) +
                      opt_stor['res']['Emissioni'][p]['unit'],
                      0, 0, 'R')
            self.ln(p_h)
        # -----------------------------------------------------------------------
        # -------------------------------------------------------------------------------------------------------------

    #
    def reliability(self, elem_cat):
        self.add_page()
        self.page_name = "Calcolo dell'Affidabilità"

        img_path = mainpath + '/UI/_resources/icons/reliability.png'
        self.set_xy(12, 35)
        self.set_fill_color(0)
        self.set_draw_color(255, 170, 0)
        self.rect(self.get_x() - 2, self.get_y() - 2, 19, 19, style='FD')
        self.image(img_path, self.get_x(), self.get_y(), 15, 15)
        self.set_xy(37.5, 44)

        self.set_draw_color(25, 25, 25)
        self.set_line_width(0.3)
        self.line(35, 38, 195, 38)
        self.line(35, 48, 195, 48)

        self.set_font('Arial', t1_s, t1_c)
        self.write(0, "Calcolo dell'Affidabilità")
        self.ln(t1_ls)

        self.set_draw_color(226, 226, 226)
        self.set_line_width(0.1)

        self.set_draw_color(226, 226, 226)
        for c in elem_cat:
            if c not in ['Ext-Grid', 'AC-Node', 'DC-Node']:
                if c in mc['Load']:
                    rel = rel_loads
                else:
                    rel = rel_other

                line_length = e_w + d_w * len(rel[1])
                if 275 < self.get_y() + t2_h + i_h + p_h * len(elem_cat[c].items()):
                    self.add_page()
                self.set_font('Arial', t2_s, t2_c)
                self.write(0, cat[c])
                self.ln(t2_h)
                self.set_font('Arial', i_s, i_c)
                self.set_fill_color(226, 226, 226)
                self.cell(e_w, i_h, 'Elemento', 1, 0, 'C', fill=True)
                for e in rel[1]:
                    self.cell(d_w, i_h, e, 1, 0, 'C', fill=True)
                self.ln(i_h)
                self.set_font('Arial', p_s, p_c)
                for e in elem_cat[c]:
                    self.cell(e_w, p_h, e, 0, 0, 'L')
                    for item in rel[0]:
                        try:
                            if elem_cat[c][e]['rel']['results'][item] < 0.001:
                                val = '%.4e' % elem_cat[c][e]['rel']['results'][item]
                            elif elem_cat[c][e]['rel']['results'][item] < 1:
                                val = '%.5f' % elem_cat[c][e]['rel']['results'][item]
                            else:
                                val = '%.2f' % elem_cat[c][e]['rel']['results'][item]
                        except:
                            pass
                        self.cell(d_w, p_h, val, 0, 0, 'C')
                    self.ln(p_h)
                    self.line(self.get_x() + 1, self.get_y(), self.get_x() + line_length - 2, self.get_y())
                self.ln(p_ls)

    def anomalies(self):
        self.add_page()
        self.page_name = "Stima delle Anomalie"

        img_path = mainpath + '/UI/_resources/icons/anomaly.png'
        self.set_xy(12, 35)
        self.set_fill_color(0)
        self.set_draw_color(255, 170, 0)
        self.rect(self.get_x() - 2, self.get_y() - 2, 19, 19, style='FD')
        self.image(img_path, self.get_x(), self.get_y(), 15, 15)
        self.set_xy(37.5, 44)

        self.set_draw_color(25, 25, 25)
        self.set_line_width(0.3)
        self.line(35, 38, 195, 38)
        self.line(35, 48, 195, 48)

        self.set_font('Arial', t1_s, t1_c)
        self.write(0, "Stima delle Anomalie")
        self.ln(t1_ls)

        self.set_draw_color(226, 226, 226)
        self.set_line_width(0.1)

        self.set_draw_color(226, 226, 226)
        for el in v:
            if 'anom' in v[el]:
                anom = copy.deepcopy(v[el]['anom'])
                if 'Hourly_Degradation' in anom['par'] or anom['par']['anomalies'] != {}:
                    self.set_font('Arial', t2_s, t2_c)
                    self.write(0, el)
                    self.ln(t2_h)
                    if 'Hourly_Degradation' in anom['par']:
                        self.set_font('Arial', i_s, i_c)
                        self.write(0, 'Velocità di degradazione: ')
                        self.set_font('Arial', p_s, p_c)
                        self.write(0, str(anom['par']['Hourly_Degradation']['rate']) + ' p.u./anno')
                        self.ln(p_h * 1.5)

                    std_par = {'is_fixed': '', 'lambda_a': 'h/y', 'lambda_duration': 'h'}
                    if anom['par']['anomalies'] != {}:
                        self.set_font('Arial', t2_s, p_c)
                        self.write(0, 'Parametri Anomalie')
                        self.ln(p_h)
                        for n in anom['par']['anomalies']:
                            self.set_font('Arial', p_s, p_c)
                            for tp in anom['par']['anomalies'][n]:
                                self.cell(d_w, p_h * 0.7, tp, 0, 0, 'L')
                                for c in anom['par']['anomalies'][n][tp]:
                                    for p in list(std_par.keys()):
                                        self.set_font('Arial', i_s, i_c)
                                        self.cell(d_w, p_h * 0.7, p, 0, 0, 'R')
                                        self.set_font('Arial', p_s, p_c)
                                        self.cell(d_w, p_h * 0.7,
                                                  str(anom['par']['anomalies'][n][tp][c][p]) + std_par[p], 0, 0, 'L')
                                    for p in anom['par']['anomalies'][n][tp][c]:
                                        if p not in list(std_par.keys()):
                                            self.set_font('Arial', i_s, i_c)
                                            self.cell(d_w, p_h * 0.7, p, 0, 0, 'R')
                                            self.set_font('Arial', p_s, p_c)
                                            self.cell(d_w, p_h * 0.7, str(anom['par']['anomalies'][n][tp][c][p]), 0, 0,
                                                      'L')
                                    pass
                            self.ln(p_h)
                        self.ln((p_h))

                    n_event = 0
                    events = []
                    ev_cap = ['N. Evento', 'Inizio [h]', 'Fine [h]', 'Tipo']
                    for a in v[el]['anom']['res']['a_dict']:
                        for n_ev in v[el]['anom']['res']['a_dict'][a]:
                            for event in n_ev:
                                events.append([n_event, n_ev[event]['orig_start'], n_ev[event]['orig_end'],
                                               n_ev[event]['descr']])
                            n_event += 1

                    s_events = sorted(events, key=lambda kv: kv[1])

                    if s_events:
                        self.set_font('Arial', i_s, i_c)
                        self.set_fill_color(226, 226, 226)
                        for e in ev_cap:
                            self.cell(d_w, i_h, e, 1, 0, 'C', fill=True)
                        self.ln(p_h)
                        for event in s_events:
                            for i in range(len(event)):
                                if i in [1, 2]:
                                    val = '%.1f' % event[i]
                                else:
                                    val = str(event[i])
                                self.cell(d_w, p_h, val, 0, 0, 'C')
                            self.ln(p_h)
                        pass
                    else:
                        self.set_font('Arial', e_s, e_c)
                        self.write(0, 'Non sono stimate anomalie')

                    self.ln(p_ls)

    #
    def adequacy(self):
        # -- Pagina iniziale ---------------------------------------------------
        self.add_page()
        self.page_name = "Calcolo dell'Adeguatezza"

        img_path = mainpath + '/UI/_resources/icons/adequacy.png'
        self.set_xy(12, 35)
        self.set_fill_color(0)
        self.set_draw_color(255, 170, 0)
        self.rect(self.get_x() - 2, self.get_y() - 2, 19, 19, style='FD')
        self.image(img_path, self.get_x(), self.get_y(), 15, 15)
        self.set_xy(37.5, 44)

        self.set_draw_color(25, 25, 25)
        self.set_line_width(0.3)
        self.line(35, 38, 195, 38)
        self.line(35, 48, 195, 48)

        img_path = mainpath + '/_temp/Functionalities/Adequacy/__images__/'
        x, y = 0, 32  # devono essere i margini della pagina

        self.set_font('Arial', t1_s, t1_c)
        self.write(0, "Calcolo dell'Adeguatezza")
        self.ln(t1_ls)

        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Profili di potenza')
        img = img_path + '1.png'
        w, h = self.img_size(img, 160, 120)
        self.set_fill_color(0)
        self.rect(25, y + 25, w, h, style='FD')
        self.image(img, 25, y + 25, w, h)

        pos_y = y + 30 + h
        self.set_y(pos_y)
        self.set_font('Arial', 'I', e_c)
        self.write(0, 'Generazione distribuita / Generazione interna totale = ')
        self.set_font('Arial', e_s, e_c)
        self.write(0, '%.2f %%' % grid['adeq']['x_gen_est'])
        self.ln(e_h * 3)

        pos_y = self.get_y()
        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Demand Not Served')
        img = img_path + '2.png'
        w, h = self.img_size(img, 160, 120)
        self.set_fill_color(0)
        self.rect(25, pos_y + e_h, w, h, style='FD')
        self.image(img, 25, pos_y + e_h, w, h)
        # ----------------------------------------------------------------------

        # -- Seconda pagina ----------------------------------------------------
        self.add_page()
        self.page_name = "Calcolo dell'Adeguatezza"

        pos_xlab, pos_ylab = self.get_x(), self.get_y()

        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Loss Of Load Expectation (LOLE)')
        img = img_path + '3.png'
        w, h = self.img_size(img, 100, 100)
        self.set_fill_color(0)
        self.rect(5, pos_ylab + e_h, w, h, style='FD')
        self.image(img, 5, pos_ylab + e_h, w, h)

        pos_y = pos_ylab + e_h + h + e_h
        self.set_y(pos_y)
        self.set_font('Arial', 'I', e_c)
        self.write(0, 'LOLE (con Affidabilità dei componenti = ')
        self.set_font('Arial', e_s, e_c)
        self.write(0, '%.4f ore/anno' % grid['adeq']['av_lole_funr_rel'])
        self.ln(e_h)
        self.set_font('Arial', 'I', e_c)
        self.write(0, 'LOLE (con Affidabilità ed Anomalie = ')
        self.set_font('Arial', e_s, e_c)
        self.write(0, '%.4f ore/anno' % grid['adeq']['av_lole_anom'])

        self.set_xy(105, pos_ylab)
        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Expected Energy Not Supplied (EENS)')
        img = img_path + '4.png'
        w, h = self.img_size(img, 100, 100)
        self.set_fill_color(0)
        self.rect(105, pos_ylab + e_h, w, h, style='FD')
        self.image(img, 105, pos_ylab + e_h, w, h)

        self.set_xy(105, pos_ylab + e_h + h + e_h)
        self.set_font('Arial', 'I', e_c)
        self.write(0, 'EENS (con Affidabilità dei componenti = ')
        self.set_font('Arial', e_s, e_c)
        self.write(0, '%.4f kWh' % grid['adeq']['av_eens_furn_rel'])
        self.ln(e_h)
        self.set_x(105)
        self.set_font('Arial', 'I', e_c)
        self.write(0, 'EENS (con Affidabilità ed Anomalie = ')
        self.set_font('Arial', e_s, e_c)
        self.write(0, '%.4f kWh' % grid['adeq']['av_eens_anom'])

    #
    def onr(self, elem_cat):
        # -- Pagina iniziale ---------------------------------------------------
        self.add_page()
        self.page_name = "Optimal Network Reconfiguration"

        img_path = mainpath + '/UI/_resources/icons/onr.png'
        self.set_xy(12, 35)
        self.set_fill_color(0)
        self.set_draw_color(255, 170, 0)
        self.rect(self.get_x() - 2, self.get_y() - 2, 19, 19, style='FD')
        self.image(img_path, self.get_x(), self.get_y(), 15, 15)
        self.set_xy(37.5, 44)

        self.set_draw_color(25, 25, 25)
        self.set_line_width(0.3)
        self.line(35, 38, 195, 38)
        self.line(35, 48, 195, 48)

        self.set_font('Arial', t1_s, t1_c)
        self.write(0, "Optimal Network Reconfiguration")
        self.ln(t1_ls)

        self.set_draw_color(226, 226, 226)
        self.set_line_width(0.1)

        self.set_draw_color(226, 226, 226)

        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Stato della rete prima del Solver')
        self.ln(e_h)

        self.set_font('Arial', p_s, p_c)
        text = grid['onr']['log_pre_grafos'].split('\n')
        for t in text:
            self.write(0, t)
            self.ln(p_h)

        self.line(10, 92, 190, 92)

        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Grafo Nodale Zonale')

        img_path = mainpath + '/_temp/Functionalities/ONR/__images__/'
        x, y = 0, 32  # devono essere i margini della pagina
        img = img_path + 'grafo_zonale_pre_ONR.png'

        w, h = self.img_size(img, 200, 230)

        self.image(img, 5, y + 70, w, h)
        # ----------------------------------------------------------------------

        # -- Seconda pagina ----------------------------------------------------
        self.add_page()
        self.page_name = "Optimal Network Reconfiguration"

        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Grafo Nodale Radiale')

        img = img_path + 'grafo_nodale_pre_ONR.png'

        w, h = self.img_size(img, 200, 230)

        self.image(img, (210 - w) / 2, y + 15, w, h)
        # ----------------------------------------------------------------------

        # -- Terza pagina ------------------------------------------------------
        self.add_page()
        self.page_name = "Optimal Network Reconfiguration"

        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Indici affidabilistici topologia iniziale radiale')

        img = img_path + 'SAIDI.png'
        self.image(img, 35, y + 15, 70, 70)

        img = img_path + 'SAIFI.png'
        self.image(img, 105, y + 15, 70, 70)

        img = img_path + 'EENS.png'
        self.image(img, 35, y + 85, 70, 70)

        img = img_path + 'obj_funct.png'
        self.image(img, 105, y + 85, 70, 70)

        self.ln(150)

        self.write(0, 'Indici di affidabilità allo stato iniziale')
        self.ln(2)

        x_lbl = ['EENS', 'SAIDI', 'SAIFI']
        y_lbl = ['FRG', 'FNC', 'SFS']

        self.set_font('Arial', i_s, i_c)
        self.set_fill_color(226, 226, 226)

        self.cell(d_w, i_h, '', 1, 0, 'C', fill=True)
        for i in x_lbl:
            self.cell(d_w, i_h, i, 1, 0, 'C', fill=True)
        self.ln()

        for m in y_lbl:
            self.cell(d_w, p_h, m, 0, 0, 'C')
            for i in x_lbl:
                if i == 'EENS':
                    val = '%.1f' % grid['onr']['indexes']['Abs'][m][i]
                else:
                    val = '%.4f' % grid['onr']['indexes']['Abs'][m][i]
                self.cell(d_w, p_h, val, 0, 0, 'C')
            self.ln(p_h)

        self.set_font('Arial', e_s, e_c)
        self.ln(10)
        self.write(0, 'Indici di affidabilità normalizzati allo stato iniziale')
        self.ln(2)

        self.set_font('Arial', i_s, i_c)
        self.set_fill_color(226, 226, 226)

        self.cell(d_w, i_h, '', 1, 0, 'C', fill=True)
        for i in x_lbl:
            self.cell(d_w, i_h, i, 1, 0, 'C', fill=True)
        self.ln()

        for m in y_lbl:
            self.cell(d_w, p_h, m, 0, 0, 'C')
            for i in x_lbl:
                val = '%.4f' % grid['onr']['indexes']['Norm'][m][i]
                self.cell(d_w, p_h, val, 0, 0, 'C')
            self.ln(p_h)

        self.set_font('Arial', e_s, e_c)
        self.ln(10)
        self.write(0, 'Funzione obiettivo allo stato iniziale')
        self.ln(2)

        self.set_font('Arial', i_s, i_c)
        self.set_fill_color(226, 226, 226)

        self.cell(d_w, i_h, '', 1, 0, 'C', fill=True)
        self.cell(d_w, i_h, 'F. obiettivo', 1, 0, 'C', fill=True)
        self.ln()

        for m in y_lbl:
            self.cell(d_w, p_h, m, 0, 0, 'C')
            val = '%.4f' % grid['onr']['indexes']['Fob'][m]['fob']
            self.cell(d_w, p_h, val, 0, 0, 'C')
            self.ln(p_h)
        # ----------------------------------------------------------------------

        # -- quarta pagna ------------------------------------------------------
        self.add_page()
        self.page_name = "Optimal Network Reconfiguration"

        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Violazioni si nodi e line allo stato iniziale')

        img = img_path + 'nodes_violations_pre.png'
        w, h = self.img_size(img, 200, 230)
        self.image(img, 5, y + 15, w, h)
        dy = y + 15 + h

        img = img_path + 'lines_overload.png'
        w, h = self.img_size(img, 200, 230)
        self.image(img, 5, dy + 15, w, h)

        self.ln(y + dy + 30)

        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Log Solver allo stato iniziale')
        self.ln(e_h)

        self.set_font('Arial', p_s, p_c)
        text = grid['onr']['log_pre_solver'].split('\n')
        for t in text:
            self.write(0, t)
            self.ln(p_h)
        self.ln(p_h)
        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Log Violazioni allo stato iniziale')
        self.ln(e_h)

        self.set_font('Arial', p_s, p_c)
        text = grid['onr']['log_pre_viol'].split('\n')
        for t in text:
            self.write(0, t)
            self.ln(p_h)
        # ----------------------------------------------------------------------

        # -- Quinta pagna ------------------------------------------------------
        self.add_page()
        self.page_name = "Optimal Network Reconfiguration"

        self.set_font('Arial', t2_s, t2_c)
        self.write(0, 'Optimal Network reconfiguration: Post-ottimizzazione')
        self.ln(t2_h * 2)

        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Grafo Zonale Nodale')

        img = img_path + 'Grafo_zonale_post_ONR.png'
        w, h = self.img_size(img, 200, 230)
        self.image(img, 5, y + 5, w, h)

        self.ln(10 + h)

        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Log Solver post otimizzazione')
        self.ln(e_h)

        self.set_font('Arial', p_s, p_c)
        text = grid['onr']['log_post_solver'].split('\n')
        for t in text:
            self.write(0, t)
            self.ln(p_h)
        self.ln(p_h)
        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Log Switch post-ottimizzazione')
        self.ln(e_h)

        self.set_font('Arial', p_s, p_c)
        text = grid['onr']['log_post_switch'].split('\n')
        for t in text:
            self.write(0, t)
            self.ln(p_h)
        # ----------------------------------------------------------------------

        # -- Sesta pagina ------------------------------------------------------
        self.add_page()
        self.page_name = "Optimal Network Reconfiguration"

        self.set_font('Arial', t2_s, t2_c)
        self.write(0, 'Optimal Network Reconfiguration: Post-ottimizzazione')
        self.ln(t2_h * 2)

        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Indici di Affidabilità')

        img = img_path + 'indexes_post.png'
        w, h = self.img_size(img, 160, 230)
        self.image(img, 5, y + 20, w, h)

        self.ln(15 + h)

        x_lbl = ['EENS', 'SAIDI', 'SAIFI', 'FOB']
        y_lbl = ['pre', 'post']
        y_lbl_ext = ['Pre-ONR', 'Post-ONR']

        self.set_font('Arial', i_s, i_c)
        self.set_fill_color(226, 226, 226)

        self.cell(d_w, i_h, '', 1, 0, 'C', fill=True)
        for i in x_lbl:
            self.cell(d_w, i_h, i, 1, 0, 'C', fill=True)
        self.ln()

        for m in range(len(y_lbl)):
            self.set_font('Arial', i_s, i_c)
            self.cell(d_w, p_h, y_lbl_ext[m], 0, 0, 'C')
            for i in x_lbl:
                if i == 'EENS':
                    val = '%.1f' % grid['onr']['indexes_post'][y_lbl[m]][i]
                else:
                    val = '%.4f' % grid['onr']['indexes_post'][y_lbl[m]][i]
                self.set_font('Arial', p_s, p_c)
                self.cell(d_w, p_h, val, 0, 0, 'C')
            self.ln(p_h)

        # ----------------------------------------------------------------------

        # -- Settima pagna -----------------------------------------------------
        self.add_page()
        self.page_name = "Optimal Network Reconfiguration"

        self.set_font('Arial', t2_s, t2_c)
        self.write(0, 'Optimal Network Reconfiguration: Post-ottimizzazione')
        self.ln(t2_h * 2)

        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Violazioni sui nodi')

        img = img_path + 'nodes_violations_post.png'
        w, h = self.img_size(img, 200, 230)
        self.image(img, 5, y + 20, w, h)

        self.ln(15 + h)

        dy = y + h + 35

        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Violazioni sulle linee')

        img = img_path + 'lines_overload.png'
        w, h = self.img_size(img, 100, 230)
        self.image(img, 5, dy, w, h)

        img = img_path + 'lines_overload_post.png'
        w, h = self.img_size(img, 100, 230)
        self.image(img, 105, dy, w, h)

        self.ln(15 + h)

        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Log Violazioni post-ottimizzazione')
        self.ln(e_h)

        self.set_font('Arial', p_s, p_c)
        text = grid['onr']['log_post_viol'].split('\n')
        for t in text:
            self.write(0, t)
            self.ln(p_h)
        # ----------------------------------------------------------------------

        # -- Ottava pagna ------------------------------------------------------
        self.add_page()
        self.page_name = "Optimal Network Reconfiguration"

        self.set_font('Arial', t2_s, t2_c)
        self.write(0, 'Confronto LoadFlow prima e dopo ONR')
        self.ln(t2_h * 2)

        for c in elem_cat:
            if c in ['AC-Node', 'DC-Node']:
                captions = lf['Nodi']
                node, line = '', 1

            elif c in ['2W-Transformer', 'AC-Line', 'DC-Line', 'PWM', 'DC-DC-Converter', 'Switch']:
                captions = lf['Links']
                node, line = 'Nodo', 2
            else:
                captions = lf['Periferiche']
                node, line = '', 1

            # if 275 < self.get_y() + t2_h + i_h + p_h * len(elem_cat[c].items()) * line:
            if 255 < self.get_y():
                self.add_page()
            self.set_font('Arial', t2_s, t2_c)
            self.write(0, cat[c])
            self.ln(t2_h)
            self.set_font('Arial', i_s, i_c)
            self.set_fill_color(226, 226, 226)
            self.cell(e_w, i_h, 'Elemento', 1, 0, 'C', fill=True)
            self.cell(p_w, i_h, node, 1, 0, 'C', fill=True)

            line_length = e_w + p_w + d_w * len(captions[1]) * 2

            for e in captions[1]:
                for pp in ['pre', 'post']:
                    self.cell(d_w, i_h, e + ' ' + pp, 1, 0, 'C', fill=True)
            self.ln(i_h)

            self.set_font('Arial', p_s, p_c)
            for e in elem_cat[c]:
                if node != '':
                    self.cell(e_w, 2 * p_h, e, 0, 0, 'L')
                    if c in ['2W-Transformer', 'DC-DC_Conv']:
                        nodes = ['HV', 'LV']
                    elif c == 'PWM':
                        nodes = ['AC', 'DC']
                    else:
                        nodes = ['1', '2']

                    for n in [1, 2]:
                        if n == 2:
                            self.cell(e_w, p_h, '', 0, 0, 'C')
                        self.cell(p_w, p_h, nodes[n - 1], 0, 0, 'C')
                        for item in captions[0]:
                            for pp in ['pre', 'post']:
                                try:
                                    data = '%.3f' % v[e]['ONR']['lf_' + pp][item][
                                        n - 1]  #  elem_cat[c][e]['lf'][item][n-1][tlf]
                                except:
                                    data = ''
                                self.cell(d_w, p_h, data, 0, 0, 'C')

                        if n == 1:
                            self.ln(p_h)

                    self.set_xy(self.get_x(), self.get_y() - p_h)
                    self.ln(2 * p_h)

                else:
                    self.cell(e_w, p_h, e, 0, 0, 'L')
                    self.cell(p_w, p_h, '', 0, 0, 'C')

                    for item in captions[0]:
                        for pp in ['pre', 'post']:
                            try:
                                if item in captions[0]:
                                    try:
                                        data = '%.3f' % v[e]['ONR']['lf_' + pp][item][0]
                                    except:
                                        data = '%.3f' % v[e]['ONR']['lf_' + pp][item]
                                else:
                                    data = '%.3f' % v[e]['ONR']['lf_' + pp][item]
                            except:
                                data = ''
                            self.cell(d_w, p_h, data, 0, 0, 'C')
                    self.ln(p_h)
                self.set_draw_color(226, 226, 226)
                self.line(self.get_x() + 1, self.get_y(), self.get_x() + line_length - 2, self.get_y())

            self.ln(p_ls)

    #
    def img_size(self, img, w_max, h_max):
        image = Image.open(img)
        w0, h0 = image.size
        if w0 / h0 < w_max / h_max:
            w, h = h_max * w0 / h0, h_max
        else:
            w, h = w_max, w_max * h0 / w0
        return w, h

    #
    def save(self):
        options = QtWidgets.QFileDialog.Options()

        saved = False
        while not saved:
            filename, _ = QtWidgets.QFileDialog.getSaveFileName(QtWidgets.QFileDialog(), "Save File", mainpath,
                                                                "PDF File (*.pdf)", options=options)

            if filename:
                if not filename.endswith('.pdf'):
                    filename = filename + '.pdf'
                self.del_PDF(filename)
                try:
                    # self.output(filename, 'F')    da controllare se lasciare questo o quello di sotto
                    self.output(filename)
                    saved = True
                except PermissionError:
                    QtWidgets.QMessageBox.warning(QtWidgets.QMessageBox(),
                                                  'File non accessibile',
                                                  'Accesso al file non consentito.\nScegliere un percorso differente')
                    pass
            else:
                saved = True

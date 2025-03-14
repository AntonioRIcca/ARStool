from fpdf import FPDF
import os
import yaml
from variables import *
from pathlib import Path
from PyQt5 import QtWidgets
import copy
from PIL import Image
import unicodedata as ud


root = os.getcwd()

# -- Cells and rows parameters -------------------
t1_h, t1_c, t1_ls, t1_s = 10, 16, 12, "B"    # Title 1 (height, font_size, line spacing, style)
t2_h, t2_c, t2_ls, t2_s = 4, 10, 12, "B"     # Title 2 (height, font_size, line spacing, style)
e_h, e_c, e_ls, e_s = 4, 8, 10, "B"          # Emphasis (height, font_size, line spacing, style)
p_h, p_c, p_ls, p_s = 3, 6, 8, ""          # Paragraph (height, font_size, line spacing, style)
i_h, i_c, i_ls, i_s = 3, 6, 8, "I"         # Captions (height, font_size, line spacing, style)
e_w, p_w, d_w = 35, 5, 17       # Cells width (element, port, data)
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
    def __init__(self):
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

        self.parameters(elem_cat)

        print(grid['studies'])
        # for study in grid['studies']:
        if grid['studies']['lf']:
            self.loadflow(elem_cat=elem_cat)
        if grid['studies']['rel']:
            self.reliability(elem_cat=elem_cat, elements='')
        if grid['studies']['anom']:
            self.anomalies(elem_cat=elem_cat, elements='')
        if grid['studies']['onr']:
            self.onr(elem_cat=elem_cat, elements='')

        print('done')

    #
    def del_PDF(self, filepath='mypdf.pdf'):
        try:
            os.remove(filepath)
        except:
            pass

    def header(self):
        if self.page_no() > 1:
            self.image(mainpath + '/_images/ARStool500.png', 8, 8, 24.5, 20)
            self.set_font('Arial', 'B', t1_c)
            self.set_xy(34, 18)
            self.set_text_color(217, 193, 221)
            self.write(0, 'Optimization')
            self.set_font('Arial', '', t1_c)
            self.write(0, ' and')

            self.set_font('Arial', 'B', t1_c)
            self.set_xy(34, 25)
            self.set_text_color(194, 214, 236)
            self.write(0, 'Reliability')
            self.set_text_color(204, 191, 233)
            self.write(0, 'Assessment')
            self.set_text_color(240, 233, 173)
            self.write(0, 'Tool')

            self.set_xy(150, self.get_y() - t1_h)
            self.set_font('Arial', 'B', t1_c)
            self.set_text_color(0, 0, 0)
            self.cell(50, t1_h*2, grid['name'], 0, 0, 'R')

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
        self.set_font('Arial', t1_s, 1.5*t1_c)
        self.image(mainpath + '/_images/ARStool500.png', 55, 80, 100, 82)
        self.set_xy(60, 170)
        self.set_text_color(204, 191, 233)
        self.write(0, 'Adequacy, ')
        self.set_text_color(194, 214, 236)
        self.write(0, 'Reliability')
        self.set_xy(65, 180)
        self.set_font('Arial', '', 1.5*t1_c)
        self.write(0, ' and')
        self.set_text_color(217, 193, 221)
        self.set_font('Arial', 'B', 1.5*t1_c)
        self.write(0, 'Security')
        self.set_text_color(240, 233, 173)
        self.write(0, 'Tool')

        self.set_xy(20, 230)
        self.set_text_color(0, 0, 0)
        # self.cell(170, 1.5*t1_h, v.features['name'], 0, 0, 'C')
        self.cell(170, 1.5*t1_h, grid['name'], 0, 0, 'C')
        print(grid)

    #
    def parameters(self, elem_cat):
        self.add_page()

        self.page_name = 'Parametri'

        self.set_font('Arial', t1_s, t1_c)
        self.write(0, 'Parametri')
        self.ln(t1_ls)

        for c in elem_cat:
            print(c)
            line_length = e_w + d_w * (len(par[cat[c]][1]) + 1)
            if 275 < self.get_y() + t2_h + i_h + p_h*len(elem_cat[c].items()):
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
                        print('c', c, '\te', e, '\titem', item)
                if c not in mc['Node']:
                    self.cell(d_w, p_h, str(elem_cat[c][e]['par']['out-of-service']), 0, 0, 'C')
                self.ln(p_h)
                self.line(self.get_x() + 1, self.get_y(), self.get_x() + line_length - 2, self.get_y())
            self.ln(p_ls)

    #
    def loadflow(self, elem_cat, tlf=0):
        self.add_page()

        self.page_name = 'LoadFlow'

        self.set_font('Arial', t1_s, t1_c)
        self.write(0, 'LoadFlow')
        self.ln(t1_ls)

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
                    print(e, captions[0])
                    self.cell(e_w, 2*p_h, e, 0, 0, 'L')
                    if c in ['2W-Transformer', 'DC-DC_Conv']:
                        nodes = ['HV', 'LV']
                    elif c == 'PWM':
                        nodes = ['AC', 'DC']
                    else:
                        nodes = ['1', '2']

                    for n in [1, 2]:
                        if n == 2:
                            self.cell(e_w, p_h, '', 0, 0, 'C')
                        self.cell(p_w, p_h, nodes[n-1], 0, 0, 'C')
                        # for item in captions[0][:len(captions[0])-1]:
                        for item in captions[0]:
                            try:
                                data = '%.3f' % elem_cat[c][e]['lf'][item][n-1][tlf]
                            except:
                                data = ''
                            self.cell(d_w, p_h, data, 0, 0, 'C')
                        if n == 1:
                            self.ln(p_h)

                    self.set_xy(self.get_x(), self.get_y() - p_h)
                    # print(e)
                    # try:
                    #     data = str(elem_cat[c][e]['results']['LimitViolated'])
                    # except:
                    #     data = ''
                    # self.cell(d_w, 2 * p_h, data, 0, 0, 'C')
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

    #
    def ems(self, elem_cat):
        self.add_page()
        self.page_name = 'EMS'

        img_path = os.getcwd() + '/_images/SplashScreen/EMS_80x80.png'
        self.set_xy(15, 35)
        self.image(img_path, self.get_x(), self.get_y(), 15, 15)
        self.set_xy(37.5, 44)

        self.set_draw_color(25, 25, 25)
        self.set_line_width(0.3)
        self.line(35, 38, 195, 38)
        self.line(35, 48, 195, 48)

        self.set_font('Arial', t1_s, t1_c)
        self.write(0, 'EMS')
        self.ln(t1_ls)

        img_path = v.project_folder + '/EMS/results'
        images = []
        for file in os.listdir(img_path):
            if file.endswith('.png') and file != 'LoadPie.png' and file != 'SelfConsPie.png':
                images.append(file)
        x, y = 20, 35   # devono essere i margini della pagina

        self.image(img_path + '/LoadPie.png', 50, 55, 110, 110)
        self.image(img_path + '/SelfConsPie.png', 50, 175, 110, 110)

        self.add_page()
        count = 0
        for img in images:
            if count >= 4:
                self.add_page()
                count = 0
                y = 35
            self.image(img_path + '/' + img, 55, y, 100, 55)
            y = y + 60
            count += 1
        print('ems done')

    # -- Stampa Protezioni ---------
    def protections(self, elem_cat):
        self.add_page()
        self.page_name = 'Protezioni'

        calc_prot = []
        prot_cost = 0
        prot_cost_max = 0
        prot_cost_min = 0

        for c in elem_cat:
            for elem in elem_cat[c]:
                if elem_cat[c][elem]['protections'] != {}:
                    prot_cost += elem_cat[c][elem]['protections']['results']['cost']
                    prot_cost_min += elem_cat[c][elem]['protections']['results']['comparison']['em']['cost']
                    prot_cost_max += elem_cat[c][elem]['protections']['results']['comparison']['el']['cost']
                    if elem_cat[c][elem]['category'] not in calc_prot:
                        calc_prot.append(elem_cat[c][elem]['category'])

        img_path = os.getcwd() + '/_images/SplashScreen/Pr_80x80.png'
        self.set_xy(15, 35)
        self.image(img_path, self.get_x(), self.get_y(), 15, 15)
        self.set_xy(37.5, 44)

        self.set_draw_color(25, 25, 25)
        self.set_line_width(0.3)
        self.line(35, 38, 195, 38)
        self.line(35, 48, 195, 48)

        self.set_font('Arial', t1_s, t1_c)
        self.write(0, 'Protezioni')
        self.ln(t1_ls)

        self.set_font('Arial', t2_s, t2_c)
        self.cell(100, t2_h, 'Costo delle Protezioni', fill=True)
        self.ln(t2_h*2)
        self.set_font('Arial', p_s, int(p_c * 1.5))
        self.cell(e_w, p_h, 'Costo minimo: ', 0, 0, 'R')
        self.cell(e_w, p_h, '%.2f Euro' % prot_cost_min, 0, 0, 'R')
        self.ln(p_h*1.5)
        self.cell(e_w, p_h, 'Costo massimo: ', 0, 0, 'R')
        self.cell(e_w, p_h, '%.2f Euro' % prot_cost_max, 0, 0, 'R')
        self.ln(p_h*2)
        self.set_font('Arial', p_s, p_c*2)
        self.cell(e_w, p_h, 'Costo Soluzione: ', 0, 0, 'R')
        self.cell(e_w, p_h, '%.2f Euro' % prot_cost, 0, 0, 'R')
        self.ln(p_h*5)

        self.set_font('Arial', t2_s, t2_c)
        self.write(0, 'Confronto caratteristiche protezioni')
        self.ln(t2_h)

        self.set_draw_color(226, 226, 226)

        self.set_font('Arial', i_s, int(i_c*0.8))
        self.cell(e_w, i_h, '', 1, 0, 'C', fill=True)
        self.cell(d_w * 3, i_h, 'Protezioni elettromeccaniche', 1, 0, 'C', fill=True)
        self.cell(d_w/2, i_h, '', 1, 0, 'C', fill=True)
        self.cell(d_w * 3, i_h, 'Protezioni elettroniche', 1, 0, 'C', fill=True)
        self.ln(i_h)
        self.cell(e_w, i_h, 'elemento', 1, 0, 'C', fill=True)
        for i in range(0, 2):
            self.cell(d_w, i_h, 'Sovracorrente [A]', 1, 0, 'C', fill=True)
            self.cell(d_w, i_h, 'Sovrarensione [kV]', 1, 0, 'C', fill=True)
            self.cell(d_w, i_h, 'Costo [Euro]', 1, 0, 'C', fill=True)
            if i == 0:
                self.cell(d_w/2, i_h, '', 1, 0, 'C', fill=True)
        self.ln(i_h)

        for c in calc_prot:
            for e in elem_cat[c]:
                line_length = e_w + d_w * 6.5
                self.set_font('Arial', i_s, i_c)
                self.cell(e_w, p_h, e, 0, 0, 'L')
                for t in ['em', 'el']:
                    if (elem_cat[c][e]['protections']['results']['type'] == 'Interruttore elettronico' and t == 'el') \
                            or (elem_cat[c][e]['protections']['results']['type'] == 'Interruttore elettromeccanico' and
                                t == 'em'):
                        self.set_font('Arial', 'B', i_c)
                    else:
                        self.set_font('Arial', i_s, i_c)
                    self.cell(d_w, p_h, '%.1f' % elem_cat[c][e]['protections']['results']['comparison'][t]['overcurrent'],
                             0, 0, 'C')
                    self.cell(d_w, p_h, '%.3f' % elem_cat[c][e]['protections']['results']['comparison'][t]['overvoltage'],
                             0, 0, 'C')
                    self.cell(d_w, p_h, '%.2f' % elem_cat[c][e]['protections']['results']['comparison'][t]['cost'], 0, 0, 'C')
                    self.cell(d_w/2, p_h, '', 0, 0, 'C')
                self.ln(p_h)
                self.line(self.get_x() + 1, self.get_y(), self.get_x() + line_length - 2, self.get_y())

        self.add_page()
        for c in calc_prot:
            line_length = e_w + d_w * len(prot[1])
            if 275 < self.get_y() + t2_h + i_h + p_h * len(elem_cat[c].items()):
                self.add_page()
            self.set_font('Arial', t2_s, t2_c)
            self.write(0, cat[c])
            self.ln(t2_h)
            self.set_font('Arial', i_s, i_c)
            self.set_fill_color(226, 226, 226)
            self.cell(e_w, i_h, 'Elemento', 1, 0, 'C', fill=True)
            for e in prot[1]:
                self.cell(d_w, i_h, e, 1, 0, 'C', fill=True)
            self.ln(i_h)
            self.set_font('Arial', p_s, p_c)
            for e in elem_cat[c]:
                self.cell(e_w, p_h, e, 0, 0, 'L')
                self.cell(d_w, p_h, elem_cat[c][e]['protections']['results']['type'].replace('Interruttore ', ''), 0, 0, 'C')
                for item in prot[0][1:]:
                    self.cell(d_w, p_h, '%.3f' % elem_cat[c][e]['protections']['results'][item], 0, 0, 'C')
                self.ln(p_h)
                self.line(self.get_x() + 1, self.get_y(), self.get_x() + line_length - 2, self.get_y())
            self.ln(p_ls)

    #
    def reliability(self, elem_cat, elements):
        self.add_page()
        self.page_name = "Calcolo dell'Affidabilità"

        # todo: da riattivare con l'immagine giusta
        # img_path = os.getcwd() + '/_images/SplashScreen/Re_80x80.png'
        # self.set_xy(15, 35)
        # self.image(img_path, self.get_x(), self.get_y(), 15, 15)
        # self.set_xy(37.5, 44)

        self.set_draw_color(25, 25, 25)
        self.set_line_width(0.3)
        self.line(35, 38, 195, 38)
        self.line(35, 48, 195, 48)

        self.set_font('Arial', t1_s, t1_c)
        self.write(0, "Calcolo dell'Affidabilità")
        self.ln(t1_ls)

        self.set_draw_color(226, 226, 226)
        self.set_line_width(0.1)

        # self.set_font('Arial', t2_s, t2_c)
        # self.cell(2 * (e_w + d_w), t2_h, 'Indici affidabilistici di sistema', 0, 0, 'L')
        # self.ln(t2_h * 1.5)
        #
        # ri = [['saifi', 'saidi', 'asai', 'caifi', 'caidi', 'ens'],
        #       ['SAIFI [1/Ca]', 'SAIDI [h/Ca]', 'ASAI [-]', 'CAIFI [1/Ca]', 'CAIDI [h]', 'ENS [KWh]']]
        #
        # for i in range(0, len(ri[0])):
        #     self.set_font('Arial', 'I', int(t2_c * 0.8))
        #     self.cell(d_w, p_h, ri[1][i], 0, 0, 'R')
        #     self.set_font('Arial', t2_s, t2_c)
        #     if v.rel_indexes[ri[0][i]] < 1:
        #         self.cell(d_w, p_h, '%.5f' % v.rel_indexes[ri[0][i]], 0, 0, 'L')
        #     else:
        #         self.cell(d_w, p_h, '%.2f' % v.rel_indexes[ri[0][i]], 0, 0, 'L')
        #     self.ln(t2_h * 1.5)
        # self.set_font('Arial', 'I', int(t2_c * 0.7))
        # self.write(0, "\tNOTA: h = ore;   C = utenze (customers);   a = anni")
        # self.ln(t2_ls)

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
                        # if item == 'MTBF_ore' and c in ['PWM', 'DC-DC_Conv', 'DC-Load', 'DC-Wind', 'PV', 'Battery']:
                        #     val = '%.4e' % (elem_cat[c][e]['reliability']['results'][item] * 1000000)
                        try:
                            if elem_cat[c][e]['rel']['results'][item] < 0.001:
                                val = '%.4e' % elem_cat[c][e]['rel']['results'][item]
                            elif elem_cat[c][e]['rel']['results'][item] < 1:
                                val = '%.5f' % elem_cat[c][e]['rel']['results'][item]
                            else:
                                val = '%.2f' % elem_cat[c][e]['rel']['results'][item]
                        except: pass
                        self.cell(d_w, p_h, val, 0, 0, 'C')
                    self.ln(p_h)
                    self.line(self.get_x() + 1, self.get_y(), self.get_x() + line_length - 2, self.get_y())
                self.ln(p_ls)

        # self.add_page()
        # img_path = v.project_folder + '/reliability/img'
        # images = []
        # for file in os.listdir(img_path):
        #     if file.endswith('.png'):
        #         images.append(file)
        # x, y = 0, 32   # devono essere i margini della pagina
        #
        # count = 0
        # for img in images:
        #     self.set_font('Arial', t2_s, t2_c)
        #
        #     name = img.replace('.png', '')
        #     if count >= 2:
        #         self.add_page()
        #         count = 0
        #         y = 32
        #         self.ln(20)
        #     self.image(img_path + '/' + img, 5, y, 200, 133)
        #
        #     self.set_y(y+15)
        #     self.cell(e_w, t2_h, name)
        #     r = elements[name]['reliability']['results']['load_rel']
        #     if r < 0.01:
        #         r_str = 'R(t) = %.4e' % r
        #     else:
        #         r_str = 'R(t) = %.5s' % r
        #     self.cell(e_w, t2_h, '')
        #     self.cell(e_w, t2_h, r_str)
        #     y = y + 130
        #     self.ln(133)
        #     count += 1

    def anomalies(self, elem_cat, elements):
        self.add_page()
        self.page_name = "Stima delle Anomalie"

        # todo: da riattivare con l'immagine giusta
        # img_path = os.getcwd() + '/_images/SplashScreen/Re_80x80.png'
        # self.set_xy(15, 35)
        # self.image(img_path, self.get_x(), self.get_y(), 15, 15)
        # self.set_xy(37.5, 44)

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
                        self.ln(p_h*1.5)

                    # std_par = [['is_fixed', 'lambda_a', 'lambda_duration'], ['', 'h/y', 'h']]
                    std_par = {'is_fixed': '', 'lambda_a': 'h/y', 'lambda_duration': 'h'}
                    if anom['par']['anomalies'] != {}:
                        self.set_font('Arial', t2_s, p_c)
                        self.write(0, 'Parametri Anomalie')
                        self.ln(p_h)
                        for n in anom['par']['anomalies']:
                            self.set_font('Arial', p_s, p_c)
                            for tp in anom['par']['anomalies'][n]:
                                self.cell(d_w, p_h*0.7, tp, 0, 0, 'L')
                                for c in anom['par']['anomalies'][n][tp]:
                                    for p in list(std_par.keys()):
                                        self.set_font('Arial', i_s, i_c)
                                        self.cell(d_w, p_h*0.7, p, 0, 0, 'R')
                                        self.set_font('Arial', p_s, p_c)
                                        self.cell(d_w, p_h*0.7, str(anom['par']['anomalies'][n][tp][c][p]) + std_par[p], 0, 0, 'L')
                                    for p in anom['par']['anomalies'][n][tp][c]:
                                        if p not in list(std_par.keys()):
                                            self.set_font('Arial', i_s, i_c)
                                            self.cell(d_w, p_h*0.7, p, 0, 0, 'R')
                                            self.set_font('Arial', p_s, p_c)
                                            self.cell(d_w, p_h*0.7, str(anom['par']['anomalies'][n][tp][c][p]), 0, 0, 'L')
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

    def onr(self, elem_cat, elements):
        # -- Pagina iniziale ---------------------------------------------------
        self.add_page()
        self.page_name = "Optimal Network Reconfiguration"

        # todo: da riattivare con l'immagine giusta
        # img_path = os.getcwd() + '/_images/SplashScreen/Re_80x80.png'
        # self.set_xy(15, 35)
        # self.image(img_path, self.get_x(), self.get_y(), 15, 15)
        # self.set_xy(37.5, 44)

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
        text = onr_dict['log_pre_grafos'].split('\n')
        for t in text:
            self.write(0, t)
            self.ln(p_h)

        self.line(10, 92, 190, 92)

        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Grafo Nodale Zonale')

        img_path = mainpath + '/Functionalities/ONR/__images__/'
        x, y = 0, 32   # devono essere i margini della pagina
        img = img_path + 'grafo_zonale_pre_ONR.png'

        w, h = self.img_size(img, 200, 230)

        self.image(img, 5, y + 70, w, h)
        # ----------------------------------------------------------------------

        # -- Seconda pagina ----------------------------------------------------
        self.add_page()
        self.page_name = "Optimal Network Reconfiguration"

        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Grafo Nodale Radiale')

        # todo: da riattivare con l'immagine giusta
        # img_path = os.getcwd() + '/_images/SplashScreen/Re_80x80.png'
        # self.set_xy(15, 35)
        # self.image(img_path, self.get_x(), self.get_y(), 15, 15)
        # self.set_xy(37.5, 44)

        # img_path = mainpath + '/Functionalities/ONR/__images__/'
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
                    val = '%.1f' % onr_dict['indexes']['Abs'][m][i]
                else:
                    val = '%.4f' % onr_dict['indexes']['Abs'][m][i]
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
                val = '%.4f' % onr_dict['indexes']['Norm'][m][i]
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
            val = '%.4f' % onr_dict['indexes']['Fob'][m]['fob']
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
        text = onr_dict['log_pre_solver'].split('\n')
        for t in text:
            self.write(0, t)
            self.ln(p_h)
        self.ln(p_h)
        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Log Violazioni allo stato iniziale')
        self.ln(e_h)

        self.set_font('Arial', p_s, p_c)
        text = onr_dict['log_pre_viol'].split('\n')
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
        text = onr_dict['log_post_solver'].split('\n')
        for t in text:
            self.write(0, t)
            self.ln(p_h)
        self.ln(p_h)
        self.set_font('Arial', e_s, e_c)
        self.write(0, 'Log Switch post-ottimizzazione')
        self.ln(e_h)

        self.set_font('Arial', p_s, p_c)
        text = onr_dict['log_post_switch'].split('\n')
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
                    val = '%.1f' % onr_dict['indexes_post'][y_lbl[m]][i]
                else:
                    val = '%.4f' % onr_dict['indexes_post'][y_lbl[m]][i]
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
        text = onr_dict['log_post_viol'].split('\n')
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
                    print(e, captions[0])
                    self.cell(e_w, 2*p_h, e, 0, 0, 'L')
                    if c in ['2W-Transformer', 'DC-DC_Conv']:
                        nodes = ['HV', 'LV']
                    elif c == 'PWM':
                        nodes = ['AC', 'DC']
                    else:
                        nodes = ['1', '2']

                    for n in [1, 2]:
                        if n == 2:
                            self.cell(e_w, p_h, '', 0, 0, 'C')
                        self.cell(p_w, p_h, nodes[n-1], 0, 0, 'C')
                        # for item in captions[0][:len(captions[0])-1]:
                        for item in captions[0]:
                            for pp in ['pre', 'post']:
                                try:
                                    data = '%.3f' % v[e]['ONR']['lf_' + pp][item][n-1]  #  elem_cat[c][e]['lf'][item][n-1][tlf]
                                except:
                                    data = ''
                                self.cell(d_w, p_h, data, 0, 0, 'C')

                        if n == 1:
                            self.ln(p_h)

                    self.set_xy(self.get_x(), self.get_y() - p_h)
                    # print(e)
                    # try:
                    #     data = str(elem_cat[c][e]['results']['LimitViolated'])
                    # except:
                    #     data = ''
                    # self.cell(d_w, 2 * p_h, data, 0, 0, 'C')
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

    def img_size(self, img, w_max, h_max):
        image = Image.open(img)
        w0, h0 = image.size
        if w0/h0 < w_max/h_max:
            w, h = h_max * w0 / h0, h_max
        else:
            w, h = w_max, w_max * h0 / w0

        print('w = ', w, '\th = ', h)

        return w, h





        # count = 0
        # for img in images:
        #     self.set_font('Arial', t2_s, t2_c)
        #
        #     name = img.replace('.png', '')
        #     if count >= 2:
        #         self.add_page()
        #         count = 0
        #         y = 32
        #         self.ln(20)
        #     self.image(img_path + '/' + img, 5, y, 200, 133)
        #
        #     self.set_y(y+15)
        #     self.cell(e_w, t2_h, name)
        #     r = elements[name]['reliability']['results']['load_rel']
        #     if r < 0.01:
        #         r_str = 'R(t) = %.4e' % r
        #     else:
        #         r_str = 'R(t) = %.5s' % r
        #     self.cell(e_w, t2_h, '')
        #     self.cell(e_w, t2_h, r_str)
        #     y = y + 130
        #     self.ln(133)
        #     count += 1

    #
    def controls(self):
        self.add_page()
        self.page_name = 'Controlli'

        img_path = os.getcwd() + '/_images/SplashScreen/Co_80x80.png'
        self.set_xy(15, 35)
        self.image(img_path, self.get_x(), self.get_y(), 15, 15)
        self.set_xy(37.5, 44)

        self.set_draw_color(25, 25, 25)
        self.set_line_width(0.3)
        self.line(35, 38, 195, 38)
        self.line(35, 48, 195, 48)

        self.set_font('Arial', t1_s, t1_c)
        self.write(0, "Controlli")
        self.ln(t1_ls)

        data_path = str(Path(os.getcwd())) + '/_functionalities/Controls'
        images_path = str(Path(os.getcwd())) + '/_images/Controls'
        cont_res = yaml.safe_load(open(data_path + '/results.yml'))

        self.set_font('Arial', i_s, int(i_c*1.2))
        self.cell(e_w, t2_h, 'Area', 0, 0, 'R')
        self.set_font('Arial', t2_s, t2_c)
        areas = [['PORT', 'RES', 'RS', 'UG'], ['PORT AREA', 'CITY AREA - Settore Residenziale',
                                               'CITY AREA - Settore Servizi Stradali',
                                               'CITY AREA - Settore Metropolitana']]
        self.cell(4*p_w, t2_h, areas[1][areas[0].index(cont_res['area'])], 0, 0, 'L')
        self.ln(p_ls)

        self.set_font('Arial', i_s, int(i_c*1.2))
        self.cell(e_w, t2_h, 'Scenario', 0, 0, 'R')
        self.set_font('Arial', t2_s, t2_c)
        self.cell(5*p_w, t2_h, cont_res['scen_year'], 0, 0, 'L')
        if cont_res['scen_year'] != 'Personalizzato':
            self.set_font('Arial', i_s, int(i_c*1.2))
            self.cell(p_w, t2_h, 'Configurazione', 0, 0, 'R')
            self.set_font('Arial', t2_s, t2_c)
            self.cell(2*p_w, t2_h, cont_res['scen_conf'], 0, 0, 'L')

        self.ln(p_ls)

        self.set_font('Arial', i_s, int(i_c*1.2))
        self.cell(e_w, t2_h, 'Mese', 0, 0, 'R')
        self.set_font('Arial', t2_s, t2_c)
        months = ['Gennaio', 'Febbraio', 'Marzo', 'Aprile', 'Maggio', 'Giugno', 'Luglio', 'Agosto', 'Settembre',
                  'Ottobre', 'Novembre', 'Dicembre']

        self.cell(5*p_w, t2_h, months[int(cont_res['month']-1)], 0, 0, 'L')

        self.set_font('Arial', i_s, int(i_c*1.2))
        self.cell(p_w, t2_h, 'Giorno', 0, 0, 'R')
        self.set_font('Arial', t2_s, t2_c)
        days = ['n.d.', 'Lunedì', 'Martedì', 'Mercoeldì', 'Giovedì', 'Venerdì', 'Sabato', 'Domenica']
        self.cell(p_w, t2_h, days[int(cont_res['day'])], 0, 0, 'L')
        self.ln(p_ls)

        self.set_font('Arial', i_s, int(i_c*1.2))
        self.cell(e_w, t2_h, 'Ora Inizio', 0, 0, 'R')
        self.set_font('Arial', t2_s, t2_c)
        inizio = '%02i:%02i' % (int(cont_res['start']), (cont_res['start']-int(cont_res['start']))*60)
        self.cell(5*p_w, t2_h, inizio, 0, 0, 'L')

        self.set_font('Arial', i_s, int(i_c*1.2))
        self.cell(p_w, t2_h, 'Ora Fine', 0, 0, 'R')
        self.set_font('Arial', t2_s, t2_c)
        fine = '%02i:%02i' % (int(cont_res['end']), (cont_res['end']-int(cont_res['end']))*60)
        self.cell(p_w, t2_h, fine, 0, 0, 'L')
        self.ln(p_ls)

        self.set_font('Arial', i_s, int(i_c*1.2))
        self.cell(e_w, t2_h, 'Linee di Backup', 0, 0, 'R')
        self.set_font('Arial', t2_s, t2_c)
        if cont_res['backup_line']:
            backup_line = '%.2f' % cont_res['backup_power']
        else:
            backup_line = 'assente'
        self.cell(5*p_w, t2_h, backup_line, 0, 0, 'L')
        self.ln(2*p_ls)

        count = 0
        for i in ctrl[0]:
            if count >= 3:
                self.ln(p_ls)
                count = 0
            self.set_font('Arial', i_s, int(i_c * 1.2))
            self.cell(e_w, t2_h, ctrl[1][ctrl[0].index(i)], 0, 0, 'R')
            self.set_font('Arial', t2_s, t2_c)
            self.cell(4 * p_w, t2_h, '%.2f' % cont_res[i], 0, 0, 'L')
            count += 1
        self.ln(p_ls)

        self.set_font('Arial', i_s, int(i_c*1.2))
        self.cell(e_w, t2_h, 'Commento', 0, 0, 'R')
        self.set_font('Arial', p_s, int(p_c*1.2))
        self.multi_cell(180-e_w, t2_h, cont_res['log'], 0, 'L')
        # self.cell(190-e_w, t2_h, cont_res['log'], 0, 0, 'L')
        self.ln(2*p_ls)

        y = self.get_y()
        self.image(images_path + '/' + cont_res['area'] + '.png', 30, y, 150, 120)

        self.add_page()
        y = 32
        for g in ctrl[0]:
            if y > 180:
                self.add_page()
                y = 32
            self.set_font('Arial', t2_s, t2_c)
            self.set_y(y)
            self.image(images_path + '/RES_' + g + '.png', 30, y, 150, 120)
            y = y + 120

    #
    def ems_indexes(self):
        self.add_page()
        self.page_name = 'EMS Energy Indexes'

        ei = [['ENS', 'ENS_pu', 'ENS_cost', 'ENS_cost_pu'], ['ENS [kWh]', 'ENS [p.u.]', 'EIC [Euro]', 'EIC [p.u.]']]
        ei_dict = yaml.safe_load(open(v.project_folder + '/ems_fault_results.yml'))

        img_path = os.getcwd() + '/_images/SplashScreen/Ei_80x80.png'
        self.set_xy(15, 35)
        self.image(img_path, self.get_x(), self.get_y(), 15, 15)
        self.set_xy(37.5, 44)

        self.set_draw_color(25, 25, 25)
        self.set_line_width(0.3)
        self.line(35, 38, 195, 38)
        self.line(35, 48, 195, 48)

        self.set_font('Arial', t1_s, t1_c)
        self.write(0, "Energy Indexes")
        self.ln(2*t1_ls)

        line_length = e_w + 8.5 * d_w

        self.set_draw_color(226, 226, 226)
        self.set_line_width(0.1)

        self.set_font('Arial', t2_s, t2_c)
        self.write(0, 'Indici Affidabilistici: Guasti stocastici e controllo EMS')
        self.ln(t2_ls)

        self.set_font('Arial', t2_s, t2_c)
        self.cell(2*(e_w+d_w), t2_h, 'Sistema',  0, 0, 'L')
        self.ln(t2_h)
        self.set_font('Arial', i_s, i_c)
        self.cell(e_w + d_w, p_h, 'Caso base', 1, 0, 'L', fill=True)
        self.cell(e_w + d_w, p_h, 'Modello EMS', 1, 0, 'L', fill=True)
        self.ln(t2_h*1.5)

        for i in range(0, len(ei[0])):
            for t in ['Base case', 'EMS model']:
                self.set_font('Arial', 'I', int(t2_c*0.8))
                self.cell(e_w, p_h, ei[1][i], 0, 0, 'R')
                self.set_font('Arial', t2_s, t2_c)
                if 'p.u' in ei[1][i]:
                    self.cell(d_w, p_h, '%.5f' % ei_dict[t]['ALL_SYSTEM'][ei[0][i]], 0, 0, 'L')
                else:
                    self.cell(d_w, p_h, '%.3f' % ei_dict[t]['ALL_SYSTEM'][ei[0][i]], 0, 0, 'L')
            self.ln(t2_h*1.5)
        self.ln(t2_ls)

        self.set_font('Arial', t2_s, t2_c)
        self.write(0, 'Carichi')
        self.ln(t2_h)
        self.set_font('Arial', i_s, i_c)
        self.cell(e_w, i_h, '', 1, 0, 'C', fill=True)
        self.cell(d_w * 4, i_h, 'Caso Base', 1, 0, 'C', fill=True)
        self.cell(d_w/2, i_h, '', 1, 0, 'C', fill=True)
        self.cell(d_w * 4, i_h, 'Modello EMS', 1, 0, 'C', fill=True)
        self.ln(i_h)
        self.cell(e_w, i_h, 'elemento', 1, 0, 'C', fill=True)
        for i in range(0, 2):
            for e in ei[1]:
                self.cell(d_w, i_h, e, 1, 0, 'C', fill=True)

            if i == 0:
                self.cell(d_w/2, i_h, '', 1, 0, 'C', fill=True)
        self.ln(i_h)

        for e in ei_dict['Base case']:
            if e != 'ALL_SYSTEM':
                self.cell(e_w, p_h, e, 0, 0, 'L')
                for t in ['Base case', 'EMS model']:
                    for p in ei[0]:
                        if p in ['ENS_pu', 'ENS_cost_pu']:
                            self.cell(d_w, p_h, '%.5f' % max(ei_dict[t][e][p], 0), 0, 0, 'C')
                        else:
                            self.cell(d_w, p_h, '%.3f' % max(ei_dict[t][e][p], 0), 0, 0, 'C')
                    if t == 'Base case':
                        self.cell(d_w / 2, p_h, '', 0, 0, 'C')
                self.ln(p_h)
                self.line(self.get_x() + 1, self.get_y(), self.get_x() + line_length - 2, self.get_y())

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

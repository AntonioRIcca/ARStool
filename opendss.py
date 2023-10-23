import py_dss_interface
from variables import v, c, mc, par_dict
# import yaml
# import os


class OpenDSS:
    def __init__(self):
        self.dss = py_dss_interface.DSS()   # sostituisce self.dss = None
        self.unr_conv = []
        self.unr_lines = []

    def open(self, filename):
        self.dss = py_dss_interface.DSS(r"C:\Program Files\OpenDSS")
        self.dss.text(f"compile [{filename}]")

        for item in self.dss.circuit.elements_names:
            cat = item.split('_')[len(item.split('_')) - 1]
            [mcat, el] = item.split('.')
            if mcat == 'Vsource':
                cat = 'source'

            self.dict_initialize(el)
            v[el]['category'] = c[cat]
            self.rel_initialize(el)
            self.lf_initialize(el)

            self.read(el)
        self.node_define()

    def read(self, el):
        mcat = ''
        v1 = None

        for m in mc.keys():
            if v[el]['category'] in mc[m]:
                mcat = m
                break

        self.dss.circuit.set_active_element(mcat + '.' + el)
        if mcat == 'Vsource':
            v[el]['par']['Vn'] = self.dss.vsources.base_kv

        elif mcat == 'Generator':
            self.dss.generators.name = el
            v1 = self.dss.generators.kv

            v[el]['par']['P'] = self.dss.generators.kw
            v[el]['par']['Vn'] = self.dss.generators.kv

            if v[el]['category'] == 'PV':
                self.create_profile(el)

            elif v[el]['category'] == 'BESS':
                v[el]['par']['cap'] = 100
                v[el]['par']['eff'] = 1
                self.create_profile(el)

            elif v[el]['category'] == 'AC-Wind':
                v[el]['par']['Q'] = self.dss.generators.kvar
                v[el]['par']['f'] = self.dss.generators.pf
                v[el]['par']['eff'] = 1
                self.create_profile(el)

            elif v[el]['category'] == 'DC-Wind':
                v[el]['par']['eff'] = 1
                self.create_profile(el)

        elif mcat == 'Transformer':
            self.unr_conv.append(el)
            self.dss.transformers.name = el
            v1 = self.dss.transformers.kv

            v[el]['par']['Vn1'] = self.dss.transformers.kv
            v[el]['par']['Sr'] = self.dss.transformers.kva
            v[el]['par']['XHL'] = self.dss.transformers.xhl

        elif mcat == 'Load':
            self.dss.loads.name = el
            v1 = self.dss.loads.kv

            v[el]['par']['P'] = self.dss.loads.kw
            v[el]['par']['Vn'] = self.dss.loads.kv
            self.create_profile(el)

            if v[el]['category'] == 'AC-Load':
                v[el]['par']['Q'] = self.dss.loads.kvar
                v[el]['par']['f'] = self.dss.loads.pf

        elif mcat == 'Line':
            self.unr_lines.append(el)
            self.dss.lines.name = el

            v[el]['par']['length'] = self.dss.lines.length
            v[el]['par']['R1'] = self.dss.lines.r1
            v[el]['par']['X1'] = self.dss.lines.x1
            v[el]['par']['In'] = self.dss.lines.norm_amps

            if v[el]['category'] == 'AC-Line':
                v[el]['par']['R0'] = self.dss.lines.r0
                v[el]['par']['X0'] = self.dss.lines.x0
                v[el]['par']['C0'] = self.dss.lines.c0
                v[el]['par']['C1'] = self.dss.lines.c1

        for node in self.dss.cktelement.bus_names:
            if node not in v.keys():
                self.dict_initialize(node)
                v[node]['category'] = 'Node'
                self.rel_initialize(node)
                self.lf_initialize(node)
                v[node]['par']['Vn'] = None
            v[node]['top']['conn'].append(el)
            v[el]['top']['conn'].append(node)
            if v1:
                v[node]['par']['Vn'] = v1

    def node_define(self):
        sourcebus = v['source']['top']['conn'][0]
        v.pop(sourcebus + '.0.0.0')

        while self.unr_conv + self.unr_lines != []:
            for el in self.unr_conv:
                if v[el]['top']['conn'][0] in v.keys():
                    bus = v[el]['top']['conn'][0]
                    if v[bus]['par']['Vn']:
                        v[el]['par']['Vn0'] = v[bus]['par']['Vn']
                        self.unr_conv.remove(el)

            for el in self.unr_lines:
                vn = None
                bus2 = None
                if v[el]['top']['conn'][0] in v.keys():
                    bus = v[el]['top']['conn'][0]
                    if v[bus]['par']['Vn']:
                        vn = v[bus]['par']['Vn']
                        bus2 = v[el]['top']['conn'][1]

                elif v[el]['top']['conn'][1] in v.keys():
                    bus = v[el]['top']['conn'][1]
                    if v[bus]['par']['Vn']:
                        vn = v[bus]['par']['Vn']
                        bus2 = v[el]['top']['conn'][0]

                if vn:
                    v[el]['par']['Vn'] = vn
                    v[bus2]['par']['Vn'] = vn
                    self.unr_lines.remove(el)

    def write_all(self):
        for el in v.keys():
            self.write(el=el)

    def write(self, el, t=None):
        mcat = None
        cat = v[el]['category']
        for m in mc.keys():
            if cat in mc[m]:
                mcat = m
                break
        self.dss.circuit.set_active_element(mcat + '.' + el)

        f = 1

        if t is not None and cat in mc['Generator'] + mc['Load'] and v[el]['par']['profile']['curve'] is not None:
            self.dss.__getattribute__(mcat.lower() + 's').__setattr__('name', el)
            f = v[el]['par']['profile']['curve'][int(t * 4)]

        if cat not in ['ExternalGrid', 'Node']:
            self.dss.__getattribute__(mcat.lower() + 's').__setattr__('name', el)
            for par in par_dict[cat].keys():
                if par in ['P', 'Q']:
                    self.dss.__getattribute__(mcat.lower() + 's').__setattr__(par_dict[cat][par], v[el]['par'][par] * f)
                else:
                    self.dss.__getattribute__(mcat.lower() + 's').__setattr__(par_dict[cat][par], v[el]['par'][par])

    def results_append(self, el):
        if v[el]['category'] != 'Node':
            mcat = ''
            for m in mc.keys():
                if v[el]['category'] in mc[m]:
                    mcat = m
                    break

            cf0, cf1 = 1, 1
            if v[el]['category'] in ['DC-Line', 'DC-DC-Converter', 'DC-Load', 'BESS', 'PV', 'DC-Wind']:
                cf0 = 3**0.5
            if v[el]['category'] in ['DC-Line', 'DC-DC-Converter', 'DC-Load', 'BESS', 'PV', 'DC-Wind', 'PWM']:
                cf1 = 3 ** 0.5

            self.dss.circuit.set_active_element(mcat + '.' + el)

            if v[el]['category'] not in mc['Line'] + mc['Transformer']:
                p, q = 0, 0
                for i in range(0, 3):
                    p = p + self.dss.cktelement.powers[2 * i]
                    q = q + self.dss.cktelement.powers[2 * i + 1]

                v[el]['lf']['p'].append(p)
                v[el]['lf']['q'].append(q)
                v[el]['lf']['v'].append(self.dss.cktelement.voltages_mag_ang[0] * 3**0.5)
                v[el]['lf']['i'].append(self.dss.cktelement.currents_mag_ang[0] * cf0)

            else:
                if v[el]['category'] in mc['Line']:
                    j = 6
                else:
                    j = 8
                p0, q0, p1, q1 = 0, 0, 0, 0
                for i in range(0, 3):
                    p0 = p0 + self.dss.cktelement.powers[2 * i]
                    q0 = q0 + self.dss.cktelement.powers[2 * i + 1]
                    p1 = p1 - self.dss.cktelement.powers[2 * i + j]
                    q1 = q1 - self.dss.cktelement.powers[2 * i + j + 1]

                v[el]['lf']['p'][0].append(p0)
                v[el]['lf']['q'][0].append(q0)
                v[el]['lf']['p'][1].append(p1)
                v[el]['lf']['q'][1].append(q1)
                v[el]['lf']['v'][0].append(self.dss.cktelement.voltages_mag_ang[0] * 3**0.5)
                v[el]['lf']['v'][1].append(self.dss.cktelement.voltages_mag_ang[j] * 3**0.5)
                v[el]['lf']['i'][0].append(self.dss.cktelement.currents_mag_ang[0] * cf0)
                v[el]['lf']['i'][1].append(self.dss.cktelement.currents_mag_ang[j] * cf1)

        else:
            self.dss.circuit.set_active_bus(el)
            v[el]['lf']['v'].append(self.dss.cktelement.voltages_mag_ang[0] * 3 ** 0.5)

    def results_store(self, el):

        if v[el]['category'] != 'Node':
            mcat = ''
            for m in mc.keys():
                if v[el]['category'] in mc[m]:
                    mcat = m
                    break

            cf0, cf1 = 1, 1
            if v[el]['category'] in ['DC-Line', 'DC-DC-Converter', 'DC-Load', 'BESS', 'PV', 'DC-Wind']:
                cf0 = 3**0.5
            if v[el]['category'] in ['DC-Line', 'DC-DC-Converter', 'DC-Load', 'BESS', 'PV', 'DC-Wind', 'PWM']:
                cf1 = 3 ** 0.5

            self.dss.circuit.set_active_element(mcat + '.' + el)

            if v[el]['category'] not in mc['Line'] + mc['Transformer']:
                p, q = 0, 0
                for i in range(0, 3):
                    p = p + self.dss.cktelement.powers[2 * i]
                    q = q + self.dss.cktelement.powers[2 * i + 1]
                v[el]['lf']['p'] = p
                v[el]['lf']['q'] = q
                v[el]['lf']['v'] = self.dss.cktelement.voltages_mag_ang[0] * 3**0.5
                v[el]['lf']['i'] = self.dss.cktelement.currents_mag_ang[0] * cf0

            else:
                if v[el]['category'] in mc['Line']:
                    j = 6
                else:
                    j = 8
                p0, q0, p1, q1 = 0, 0, 0, 0
                for i in range(0, 3):
                    p0 = p0 + self.dss.cktelement.powers[2 * i]
                    q0 = q0 + self.dss.cktelement.powers[2 * i + 1]
                    p1 = p1 - self.dss.cktelement.powers[2 * i + j]
                    q1 = q1 - self.dss.cktelement.powers[2 * i + j + 1]

                v[el]['lf']['p'][0] = p0
                v[el]['lf']['q'][0] = q0
                v[el]['lf']['p'][1] = p1
                v[el]['lf']['q'][1] = q1
                v[el]['lf']['v'][0] = self.dss.cktelement.voltages_mag_ang[0] * 3**0.5
                v[el]['lf']['v'][1] = self.dss.cktelement.voltages_mag_ang[j] * 3**0.5
                v[el]['lf']['i'][0] = self.dss.cktelement.currents_mag_ang[0] * cf0
                v[el]['lf']['i'][1] = self.dss.cktelement.currents_mag_ang[j] * cf1

        else:
            self.dss.circuit.set_active_bus(el)
            v[el]['lf']['V'] = self.dss.cktelement.voltages_mag_ang[0] * 3 ** 0.5

    def solve(self):
        self.dss.solution.solve()

        for el in v.keys():
            self.results_store(el)

        return self.dss.solution.converged

    def solve_profile(self):
        for t in range(0, 96):
            for el in v.keys():
                if v[el]['category'] not in mc['Vsource'] + mc['Node']:
                    self.write(el=el, t=t/4)
                    self.dss.solution.solve()
                self.results_append(el)
        pass

    def dict_initialize(self, el):
        v[el] = dict()
        for sub in ['top', 'par', 'lf', 'rel']:
            v[el][sub] = dict()
        v[el]['top']['conn'] = []

    def rel_initialize(self, el):
        v[el]['rel']['par'] = dict()
        for p in ['Pi_E', 'Pi_Q', 'alfa', 'beta']:
            v[el]['rel']['par'][p] = None

        v[el]['rel']['results'] = dict()
        if v[el]['category'] in mc['Load']:
            v[el]['rel']['results']['load_rel'] = None
        for p in ['lambda', 'MTBF_ore', 'MTBF_anni', 'Pi_Si']:
            v[el]['rel']['results'][p] = None

    def lf_initialize(self, el):
        params = ['i', 'v', 'p', 'q']

        if v[el]['category'] in mc['Transformer'] + mc['Line']:
            for p in params:
                v[el]['lf'][p] = dict()
                v[el]['lf'][p][0] = []
                v[el]['lf'][p][1] = []
        else:
            for p in params:
                v[el]['lf'][p] = []

    def create_profile(self, el):
        v[el]['par']['profile'] = dict()
        v[el]['par']['profile']['name'] = None
        v[el]['par']['profile']['curve'] = None

        # profile = None
        #
        # if v[el]['category'] == 'AC-Load':
        #     profile = 'AC-Load'
        # elif v[el]['category'] == 'DC-Load':
        #     profile = 'DC-Load'
        # elif v[el]['category'] in ['AC-Wind', 'DC-Wind']:
        #     profile = 'Wind'
        # elif v[el]['category'] == 'PV':
        #     profile = 'PV'
        #
        # if profile:
        #     filename = os.getcwd() + '/_benchmark/_data/_profiles/' + profile + '.yml'
        #     d = yaml.safe_load(open(filename))
        #
        #     v[el]['par']['profile']['name'] = d['name']
        #     v[el]['par']['profile']['curve'] = d['profile']
        # else:
        #     v[el]['par']['profile']['name'] = None
        #     v[el]['par']['profile']['curve'] = None

    def losses_calc(self):
        for el in v.keys():
            if v[el]['category'] in mc['Transformer']:
                self.dss.transformers.name = el
                self.dss.circuit.set_active_element('transformer.' + el)
                print(self.dss.cktelement.name + ': ' + str(self.dss.cktelement.losses), str(self.dss.cktelement.phase_losses))


OpenDSS()

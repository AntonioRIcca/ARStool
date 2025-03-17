import copy
import os

mainpath = os.getcwd()


def v_initialize():
    for k in list(v.keys()):
        del v[k]
    grid_initialize()


def grid_initialize():
    # grid0 = {
    #     'benchmark': False,
    #     'current': None,
    #     'name': None,
    #     'studies': {
    #         'lf': False,
    #         'anom': False,
    #         'rel': False,
    #         'adeq': False,
    #         'optstor': False,
    #         'onr': False,
    #     },
    #     'profile': {
    #         'points': None,
    #         'step': None,
    #         'start': None,
    #         'end': None,
    #         'exist': False,
    #     },
    #     'lf': {
    #         'start': None,
    #         'end': None,
    #         'points': None,
    #     },
    #     'rel': {
    #         'T0': 25,
    #         't': 1,
    #         'prof_T': {
    #             'name': None,
    #             'profile': None,
    #         },
    #     },
    #     'adeq': {
    #         'x_gen_est': None,
    #         'av_lole_funr_rel': None,
    #         'av_lole_anom': None,
    #         'av_eens_furn_rel': None,
    #         'av_eens_anom': None,
    #     },
    #     'onr': {
    #         'log_pre_grafos': '',
    #         'log_pre_solver': '',
    #         'log_pre_viol': '',
    #         'log_post_solver': '',
    #         'log_post_switch': '',
    #         'log_post_viol': '',
    #         'indexes': {},
    #         'indexes_post': {},
    #     }
    # }

    for p in grid0:
        grid[p] = copy.deepcopy(grid0[p])


opt_stor = {
    'par': {
        'Input': {
            'electrLev': {
                'lbl': 'Livello di elettrificazione',
                'val': 0,
                'unit': '%'
            },
            'enConsGrow': {
                'lbl': 'Crescita annua dei consumi di energia finale t.m.a',
                'val': 0,
                'unit': '%'
            },
            'ferGen': {
                'lbl': 'Generazione da FER',
                'val': 0,
                'unit': '%'
            },
            'h2Cons': {
                'lbl': 'Produzione solare su RES',
                'val': 0,
                'unit': '%'
            },
            'solarFer': {
                'lbl': 'Consumo per produzione H2',
                'val': 0,
                'unit': '%'
            },
        },
        'Scenario': {
            0: {
                'year': {
                    'lbl': 'Anno Scenario',
                    'val': 2019,
                    'unit': '',
                },
                'scen': {
                    'lbl': 'Scenario',
                    'val': '',
                    'unit': '',
                },
            },
            1: {
                'totEnConsMtep': {
                    'lbl': 'Consumi finali di energia',
                    'val': 0,
                    'unit': 'Mtep',
                },
                'totEnCons': {
                    'lbl': '-',
                    'val': 0,
                    'unit': 'TWh',
                },
                'h2Cons': {
                    'lbl': 'di cui consumi per produrre H2',
                    'val': 0,
                    'unit': 'TWh',
                },
                'enDuty': {
                    'lbl': 'Fabbisogno di energia elettrica',
                    'val': 0,
                    'unit': 'TWh',
                },
                'enImport': {
                    'lbl': 'Energia importata',
                    'val': 0,
                    'unit': 'TWh',
                },
                'enProd': {
                    'lbl': 'Energia prodotta',
                    'val': 0,
                    'unit': 'TWh',
                },
            },
            2: {
                'ferGen': {
                    'lbl': 'Generazione da FER',
                    'val': 0,
                    'perc': 0,
                    'unit': 'TWh',
                },
                'solarGen': {
                    'lbl': 'di cui Solare',
                    'val': 0,
                    'perc': 0,
                    'unit': 'TWh',
                },
                'windGen': {
                    'lbl': 'di cui Eolico',
                    'val': 0,
                    'perc': 0,
                    'unit': 'TWh',
                },
                'otherGen': {
                    'lbl': 'di cui Altre fonti',
                    'val': 0,
                    'perc': 0,
                    'unit': 'TWh',
                },
            },
            3: {
                'ferCap': {
                    'lbl': 'Capacità installata FER',
                    'val': 0,
                    'perc': 0,
                    'unit': 'GW',
                },
                'solarCap': {
                    'lbl': 'di cui Solare',
                    'val': 0,
                    'perc': 0,
                    'unit': 'GW',
                },
                'windCap': {
                    'lbl': 'di cui Eolico',
                    'val': 0,
                    'perc': 0,
                    'unit': 'GW',
                },
                'otherCap': {
                    'lbl': 'di cui Altre fonti',
                    'val': 0,
                    'perc': 0,
                    'unit': 'GW',
                },
            },

            4: {
                'co2Emis': {
                    'lbl': 'Emissioni di CO2',
                    'val': 0,
                    'unit': 'kg',
                },
            },
        },
    },
    'res': {
        'Fabbisogno': {
            0: {
                'totEnConsMtep': {
                    'lbl': 'Consumi finali di energia',
                    'val_act': 0,
                    'val_prosp': 0,
                    'unit': 'Mtep',
                },
                'totEnCons': {
                    'lbl': '-',
                    'val_act': 0,
                    'val_prosp': 0,
                    'unit': 'TWh',
                },
                'h2Cons': {
                    'lbl': 'di cui consumi per produrre H2',
                    'val_act': 0,
                    'val_prosp': 0,
                    'unit': 'TWh',
                },
                'enDuty': {
                    'lbl': 'Fabbisogno di energia elettrica',
                    'val_act': 0,
                    'val_prosp': 0,
                    'unit': 'TWh',
                },
                'enImport': {
                    'lbl': 'Energia importata',
                    'val_act': 0,
                    'val_prosp': 0,
                    'unit': 'TWh',
                },
                'enProd': {
                    'lbl': 'Energia prodotta',
                    'val_act': 0,
                    'val_prosp': 0,
                    'unit': 'TWh',
                },
            },
        },
        'Rinnovabili': {
            0: {
                'ferGen': {
                    'lbl': 'Generazione da FER',
                    'val_act': 0,
                    'val_prosp': 0,
                    'perc_act': 0,
                    'perc_prosp': 0,
                    'unit': 'TWh',
                },
                'solarGen': {
                    'lbl': 'di cui Solare',
                    'val_act': 0,
                    'val_prosp': 0,
                    'perc_act': 0,
                    'perc_prosp': 0,
                    'unit': 'TWh',
                },
                'windGen': {
                    'lbl': 'di cui Eolico',
                    'val_act': 0,
                    'val_prosp': 0,
                    'perc_act': 0,
                    'perc_prosp': 0,
                    'unit': 'TWh',
                },
                'otherGen': {
                    'lbl': 'di cui Altre fonti',
                    'val_act': 0,
                    'val_prosp': 0,
                    'perc_act': 0,
                    'perc_prosp': 0,
                    'unit': 'TWh',
                },
            },
            1: {
                'hiOvergen': {
                    'lbl': 'Overgenerazione Alta',
                    'val_act': 0,
                    'val_prosp': 0,
                    'unit': 'TWh',
                },
                'lowOvergen': {
                    'lbl': 'Overgenerazione Bassa',
                    'val_act': 0,
                    'val_prosp': 0,
                    'unit': 'TWh',
                },
            },
            2: {
                'ferCap': {
                    'lbl': 'Capacità installata FER',
                    'val_act': 0,
                    'val_prosp': 0,
                    'perc_act': 0,
                    'perc_prosp': 0,
                    'unit': 'GW',
                },
                'solarCap': {
                    'lbl': 'di cui Solare',
                    'val_act': 0,
                    'val_prosp': 0,
                    'perc_act': 0,
                    'perc_prosp': 0,
                    'unit': 'GW',
                },
                'windCap': {
                    'lbl': 'di cui Eolico',
                    'val_act': 0,
                    'val_prosp': 0,
                    'perc_act': 0,
                    'perc_prosp': 0,
                    'unit': 'GW',
                },
                'otherCap': {
                    'lbl': 'di cui Altre fonti',
                    'val_act': 0,
                    'val_prosp': 0,
                    'perc_act': 0,
                    'perc_prosp': 0,
                    'unit': 'GW',
                },
            },
        },
        'Accumuli': {
            'sysStor': {
                'lbl': 'Sistemi di stoccaggio (ipotesi TERNA)',
                'val': 0,
                'unit': 'GWh',
            },
        },
        'Idrogeno': {
            'maxH2': {
                'lbl': 'Max Produzione di H2 da overgeneration',
                'val_HI': 0,
                'val_LO': 0,
                'unit': 'TWh',
            },
            'toprodH2': {
                'lbl': 'Produzione di H2 oltre overgeneration',
                'val_HI': 0,
                'val_LO': 0,
                'unit': 'TWh',
            },
        },
        'Costi': {
            'frnpCosts': {
                'lbl': 'Costo FRNP M(al kW installato)',
                'val': 0,
                'unit': 'M€',
            },
            'capexCosts': {
                'lbl': 'CAPEX totale SdA',
                'val': 0,
                'unit': '€',
            },
            'h2Costs': {
                'lbl': 'Costo H2)',
                'val': 0,
                'unit': '€',
            },
        },
        'Emissioni': {
            'co2Emis': {
                'lbl': 'Emissioni di CO2',
                'val_act': 0,
                'val_prosp': 0,
                'unit': 'Mt',
            },
            'co2EmisRed': {
                'lbl': 'Riduzione delle emissioni',
                'val_act': 0,
                'val_prosp': 0,
                'unit': 'Mt',
            },
        },
    },
}


grid0 = {
        'benchmark': False,
        'current': None,
        'name': None,
        'studies': {
            'lf': False,
            'anom': False,
            'rel': False,
            'adeq': False,
            'optstor': False,
            'onr': False,
        },
        'profile': {
            'points': None,
            'step': None,
            'start': None,
            'end': None,
            'exist': False,
        },
        'lf': {
            'start': None,
            'end': None,
            'points': None,
        },
        'rel': {
            'T0': 25,
            't': 1,
            'prof_T': {
                'name': None,
                'profile': None,
            },
        },
        'adeq': {
            'x_gen_est': None,
            'av_lole_funr_rel': None,
            'av_lole_anom': None,
            'av_eens_furn_rel': None,
            'av_eens_anom': None,
        },
        'onr': {
            'log_pre_grafos': '',
            'log_pre_solver': '',
            'log_pre_viol': '',
            'log_post_solver': '',
            'log_post_switch': '',
            'log_post_viol': '',
            'indexes': {},
            'indexes_post': {},
        }
    }

# onr_dict = {}
#
#
# _onr_dict_ = {
#     'log_pre_grafos': '',
#     'log_pre_solver': '',
#     'log_pre_viol': '',
#     'log_post_solver': '',
#     'log_post_switch': '',
#     'log_post_viol': '',
#     'indexes': {},
#     'indexes_post': {},
# }


# def onr_dict_init():
#     for i in _onr_dict_:
#         onr_dict[i] = _onr_dict_[i]


bench = {
    'profiles': {
        'load': {
            'RES': 'Residenziale',
            'IND': 'Industriale',
            'COM': 'Commerciale',
            'AGR': 'Agricolo',
            'RLV': 'Rurale - LV',
            'RMV_CUST1': 'Rurale - MV 1',
            'RMV_CUST2': 'Rurale - MV 2',
            'RMV_CUST3': 'Rurale - MV 3',
        },
        'gen': {
            'HYDRO': 'Idroelettrico',
            'PV': 'Fotovoltaico',
            'CHP': 'Cogeneratore',
        },
    },
    'categories': {
        'AC-Load': 'load',
        'DC-Load': 'load',
        'AC-PV': 'PV',
        'DC-PV': 'PV',
        'AC-Wind': 'CHP',
        'DC-Wind': 'CHP',
        'Diesel-Motor': 'CHP',
        'Turbine': 'HYDRO',
    },

}

fn = {
    'lf': False,
    'anom': False,
    'rel': False,
    'optstor': False,
}

fn_en = {
    'lf': True,
    'anom': True,
    # 'opf': True,
    'rel': True,
    'adeq': True
    # 'gm': True,
    # 'onr': True,
}

visualpar = 'lf'

v = dict()
vdss = dict()

grid = {}

mc = {
    'Vsource': ['ExternalGrid'],
    'LoadShape': [],
    'GrowthShape': [],
    'TCC_Curve': [],
    'Spectrum': [],
    'Line': ['AC-Line', 'DC-Line', 'Switch'],
    'Load': ['AC-Load', 'DC-Load'],
    'Transformer': ['2W-Transformer', 'PWM', 'DC-DC-Converter'],
    'Generator': ['AC-PV', 'DC-PV', 'AC-Wind', 'DC-Wind', 'Diesel-Motor', 'Turbine', 'AC-BESS', 'DC-BESS'],
    'BESS': ['AC-BESS', 'DC-BESS'],
    'LineCode': ['AC-LineCode', 'DC-LineCode', ],
    'Node': ['AC-Node', 'DC-Node'],
}

dss_cat = {
    'Vsource': [],
    'LineCode': [],
    'LoadShape': [],
    'GrowthShape': [],
    'TCC_Curve': [],
    'Spectrum': [],
    'Line': [],
    'Load': [],
    'Transformer': [],
    'Generator': [],
}

c = {
    'source': 'ExternalGrid',
    'line': 'AC-Line',
    'dc-line': 'DC-Line',
    'tr': '2W-Transformer',
    'pwm': 'PWM',
    'dc-dc-conv': 'DC-DC-Converter',
    'ac-load': 'AC-Load',
    'dc-load': 'DC-Load',
    'bess': 'AC-BESS',
    'ac-bess': 'AC-BESS',
    'dc-bess': 'DC-BESS',
    'pv': 'AC-PV',
    'ac-pv': 'AC-PV',
    'dc-pv': 'DC-PV',
    'wind': 'AC-Wind',
    'dc-micro-wind': 'DC-Wind',
    'diesel': 'Diesel-Motor',
    'turb': 'Turbine',
    'bb': 'AC-Node',
    'node': 'AC-Node',
    'dc-bb': 'DC-Node',
    'dc-node': 'DC-Node',
    'sourcebus': 'AC-Node'
}

dsstag = {
    'transformer': {
        'default': '2W-Transformer',
        'tr': '2W-Transformer',
        'pwm': 'PWM',
        'dc-dc-conv': 'DC-DC-Converter',
    },
    'generator': {
        'default': 'Turbine',
        'diesel': 'Diesel-Motor',
        'pv': 'AC-PV',
        'ac-pv': 'AC-PV',
        'ac-wind': 'AC-Wind',
        'wind': 'AC-Wind',
        'dc-pv': 'DC-PV',
        'dc-wind': 'DC-Wind',
        'dc-micro-wind': 'DC-Wind',
        'bess': 'AC-BESS',
        'ac-bess': 'AC-BESS',
        'dc-bess': 'DC-BESS',
    },
    'load': {
        'default': 'AC-Load',
        'ac-load': 'AC-Load',
        'load': 'AC-Load',
        'dc-load': 'DC-Load',
    },
    'line': {
        'default': 'AC-Line',
        'line': 'AC-Line',
        'ac-line': 'AC-Line',
        'dc-line': 'DC-Line',
        's': 'Switch',
        'm': 'Switch',
    },

}

new_par_dict = {
    'Turbine': {
        'top': {
            'conn': {
                'label': ['bus1'],
            },
        },
        'par': {
            'P': {
                'label': 'kW',
                'unit': 'kW',
            },
            'cosPhi': {
                'label': 'kW',
                'unit': '',
                'default': 1
            },
            'Vn': {
                'label': 'kv',
                'unit': 'kV',
            },
            'others': {
                'phases': '3',
            },
        },
    },

    'AC-PV': {
        'top': {
            'conn': {
                'label': ['bus1'],
            },
        },
        'par': {
            'P': {
                'label': 'kW',
                'unit': 'kW',
            },
            'Vn': {
                'label': 'kv',
                'unit': 'kV',
            },
            'others': {
                'phases': '3',
                'kvar': '0',
                'model': '3',
            },
        },
    },

    'DC-PV': {
        'top': {
            'conn': {
                'label': ['bus1'],
            },
        },
        'par': {
            'P': {
                'label': 'kW',
                'unit': 'kW',
            },
            'Vn': {
                'label': 'kv',
                'unit': 'kV',
            },
            'others': {
                'phases': '3',
                'kvar': '0',
                'model': '3',
            },
        },
    },

    'AC-BESS': {
        'top': {
            'conn': {
                'label': ['bus1'],
            },
        },
        'par': {
            'P': {
                'label': 'kW',
                'unit': 'kW',
            },
            'cosPhi': {
                'label': 'pf',
                'unit': '',
                'default': 1,
            },
            'cap': {
                'label': 'Cap',
                'unit': 'kVAh',
                'default': 1000,
            },
            # 'SOC': {
            #     'label': 'SOC',
            #     'unit': '-',
            #     'default': 50,
            # },
            'Vn': {
                'label': 'kv',
                'unit': 'kV',
            },
            'others': {
                'phases': '3',
                # 'kvar': '0',
                'model': '3',
            },
        },
    },

    'DC-BESS': {
        'top': {
            'conn': {
                'label': ['bus1'],
            },
        },
        'par': {
            'P': {
                'label': 'kW',
                'unit': 'kW',
            },
            'Vn': {
                'label': 'kv',
                'unit': 'kV',
            },
            'cap': {
                'label': 'Cap',
                'unit': 'kWh',
                'default': 1000,
            },
            # 'SOC': {
            #     'label': 'SOC',
            #     'unit': '-',
            #     'default': 50,
            # },
            'others': {
                'phases': '3',
                # 'kvar': '0',
                'model': '3',
            },
        },
    },

    'DC-Wind': {
        'top': {
            'conn': {
                'label': ['bus1'],
            },
        },
        'par': {
            'P': {
                'label': 'kW',
                'unit': 'kW',
            },
            'Vn': {
                'label': 'kv',
                'unit': 'kV',
            },
            'others': {
                'phases': '3',
                'kvar': '0',
                'model': '3',
            },
        },
    },

    'AC-Wind': {
        'top': {
            'conn': {
                'label': ['bus1'],
            },
        },
        'par': {
            'P': {
                'label': 'kW',
                'unit': 'kW',
            },
            'cosPhi': {
                'label': 'kW',
                'unit': '',
            },
            'Vn': {
                'label': 'kv',
                'unit': 'kV',
            },
            'others': {
                'phases': '3',
            },
        },
    },

    '2W-Transformer': {
        'top': {
            'conn': {
                'label': ['buses'],
            },
        },
        'par': {
            'Sr': {
                'label': 'kVAs',
                'unit': 'kVA',
            },
            'Vn': {
                'label': 'kVs',
                'unit': 'kV',
            },
            'Rs': {
                'label': '%Rs',
                'unit': '%',
                'default': 0
            },
            'XHL': {
                'label': 'XHL',
                'unit': '',
                'default': 1E-9
            },
            'imag': {
                'label': '%imag',
                'unit': '%',
                'default': 0,
            },
            'others': {
                'windings': '2',
                'conns': '[delta, wye, ]',
            },
        },
    },

    'PWM': {
        'top': {
            'conn': {
                'label': ['buses'],
            },
        },
        'par': {
            'Sr': {
                'label': 'kVAs',
                'unit': 'kVA',
            },
            'Vn': {
                'label': 'kVs',
                'unit': 'kV',
            },
            'others': {
                'windings': '2',
                'conns': '[delta, wye, ]',
                '%Rs': '[0, 0, ]',
                'XHL': '1E-009',
                '%imag': '0'
            },
        },
    },

    'DC-DC-Converter': {
        'top': {
            'conn': {
                'label': ['buses'],
            },
        },
        'par': {
            'Sr': {
                'label': 'kVAs',
                'unit': 'kVA',
            },
            'Vn': {
                'label': 'kVs',
                'unit': 'kV',
            },
            'others': {
                'windings': '2',
                'conns': '[delta, wye, ]',
                '%Rs': '[0, 0, ]',
                'XHL': '1E-009',
                '%imag': '0'
            },
        },
    },

    'AC-Load': {
        'top': {
            'conn': {
                'label': ['bus1'],
            },
        },
        'par': {
            'P': {
                'label': 'kW',
                'unit': 'kW',
            },
            'cosPhi': {
                'label': 'pf',
                'unit': '',
                'default': 1,
            },
            'Vn': {
                'label': 'kV',
                'unit': 'kV',
            },
            'Customers': {
                'label': 'NumCust',
                'unit': '',
                'default': 1,
            },
            'others': {
                'phases': '3',
            },
        },
    },

    'DC-Load': {
        'top': {
            'conn': {
                'label': ['bus1'],
            },
        },
        'par': {
            'P': {
                'label': 'kW',
                'unit': 'kW',
            },
            'Vn': {
                'label': 'kV',
                'unit': 'kV',
            },
            'Customers': {
                'label': 'NumCust',
                'unit': '',
                'default': 1,
            },
            'others': {
                'phases': '3',
                'pf': '1',
            },
        },
    },

    'AC-LineCode': {
        'top': {},
        'par': {
            'R1': {
                'label': 'r1',
                'unit': 'ohm',
            },
            'X1': {
                'label': 'x1',
                'unit': 'ohm',
            },
            'B1': {
                'label': 'B1',
                'unit': 'uS',
            },
            'R0': {
                'label': 'r0',
                'unit': 'ohm',
            },
            'X0': {
                'label': 'x0',
                'unit': 'ohm',
                'default': 1e-9,
            },
            'B0': {
                'label': 'B0',
                'unit': 'uS',
                'default': 1e-9,
            },
            'others': {
                'nphases': '3',
            },
        },
    },

    'DC-LineCode': {
        'top': {},
        'par': {
            'R1': {
                'label': 'r1',
                'unit': 'ohm',
            },
            'X1': {
                'label': 'x1',
                'unit': 'ohm',
            },
            'others': {
                'nphases': '3',
            },
        },
    },

    'AC-Line': {
        'top': {
            'conn': {
                'label': ['bus1', 'bus2', ],
            },
            # 'type': {
            #     'label': ['linecode'],
            # },
        },
        'par': {
            'In': {
                'label': 'normamps',
                'unit': 'ohm/km',
            },
            'length': {
                'label': 'length',
                'unit': 'km',
            },

            # -- TODO: da verificare -------------
            'R1': {
                'label': 'r1',
                'unit': 'ohm',
                'default': 0,
            },
            'X1': {
                'label': 'x1',
                'unit': 'ohm',
                'default': 1E-9,
            },
            'B1': {
                'label': 'B1',
                'unit': 'uS',
                'default': 1E-9,
            },
            # 'C1': {
            #     'label': 'C1',
            #     'unit': 'uS',
            #     'default': 1E-9,
            # },
            'R0': {
                'label': 'r0',
                'unit': 'ohm',
                'default': 0,
            },
            'X0': {
                'label': 'x0',
                'unit': 'ohm',
                'default': 1E-9,
            },
            'B0': {
                'label': 'B0',
                'unit': 'uS',
                'default': 1E-9,
            },
            # 'C0': {
            #     'label': 'C0',
            #     'unit': 'uS',
            #     'default': 1E-9,
            # },

            # 'linecode': {
            #     'label': 'linecode',
            #     'default': '',
            # },
            # ------------------------------------

            'others': {
                'Season': '1',
                'Ratings': '[400,]',
                'emergamps': '600',
            },
        },
    },

    'DC-Line': {
        'top': {
            'conn': {
                'label': ['bus1', 'bus2', ],
            },
            'type': {
                'label': ['linecode'],
            },
        },
        'par': {
            'In': {
                'label': 'normamps',
                'unit': 'ohm/km',
            },
            'length': {
                'label': 'length',
                'unit': 'km',
            },
            'others': {
                'Season': '1',
                'Ratings': '[400,]',
                'emergamps': '600',
            },
        },
    },

    'Switch': {
        'top': {
            'conn': {
                'label': ['bus1', 'bus2', ],
            },
        },
        'par': {
            'others': {
                'Season': '1',
                'Ratings': '[400,]',
                'emergamps': '600',
                'normamps': '1000',
                'length': '0.01',
                'R1': '0',
                'X1': '1e-9',
                'B1': '1e-9',
                'R0': '0',
                'X0': '1e-9',
                'B0': '1e-9',
            },
        },
    },

    'ExternalGrid': {
        'top': {
            'conn': {
                'label': ['bus1'],
            },
        },
        'par': {
            'Vn': {
                'label': 'basekv',
                'unit': 'kV',
            },
            'others': {}
        },
    },
}

par_dict = {
    'AC-PV': {
        'P': 'kw',
        'Vn': 'kv'
    },

    'DC-PV': {
        'P': 'kw',
        'Vn': 'kv'
    },

    'AC-BESS': {
        'P': 'kw',
        'Vn': 'kv'
    },

    'DC-BESS': {
        'P': 'kw',
        'Vn': 'kv'
    },

    'AC-Wind': {
        'P': 'kw',
        'Q': 'kvar',
        'cosPhi': 'pf',
        'Vn': 'kv'
    },

    'DC-Wind': {
        'P': 'kw',
        'Vn': 'kv'
    },

    '2W-Transformer': {
        'Vn1': 'kv'
    },

    'AC-Line': {
        'C0': 'c0',
        'C1': 'c1',
        'In': 'norm_amps',
        'R0': 'r0',
        'R1': 'r1',
        'X0': 'x0',
        'X1': 'x1',
        'length': 'length',
    },

    'DC-Line': {},
    'PWM': {},
    'DC-DC-Converter': {},
    'AC-Load': {
        'P': 'kw',
        'Q': 'kvar',
        'cosPhi': 'pf',
    },
    'DC-Load': {
        'P': 'kw',
    },
    'Diesel-Motor': {},
    'Turbine': {},
    'Node': {},
    'ExternalGrid': {},
}

el_lfresults = {
    'ExternalGrid': {
        'Vn': {'tag': 'v', 'i': None, 'decimal': 3, 'unit': 'kV'},
    },
    'AC-Node': {
        'Vn': {'tag': 'v', 'i': None, 'decimal': 3, 'unit': 'kV'},
    },
    'DC-Node': {
        'Vn': {'tag': 'v', 'i': None, 'decimal': 3, 'unit': 'kV'},
    },
    'AC-Line': {
        'P0': {'tag': 'p', 'i': 0, 'decimal': 3, 'unit': 'kW'},
        'P1': {'tag': 'p', 'i': 1, 'decimal': 3, 'unit': 'kW'},
        'Q0': {'tag': 'q', 'i': 0, 'decimal': 3, 'unit': 'kVar'},
        'Q1': {'tag': 'q', 'i': 1, 'decimal': 3, 'unit': 'kVar'},
        'i': {'tag': 'i', 'i': 0, 'decimal': 3, 'unit': 'A'},
        'V0': {'tag': 'v', 'i': 0, 'decimal': 3, 'unit': 'kV'},
        'V1': {'tag': 'v', 'i': 1, 'decimal': 3, 'unit': 'kV'},
    },
    'DC-Line': {
        'P0': {'tag': 'p', 'i': 0, 'decimal': 3, 'unit': 'kW'},
        'P1': {'tag': 'p', 'i': 1, 'decimal': 3, 'unit': 'kW'},
        'i': {'tag': 'i', 'i': 0, 'decimal': 3, 'unit': 'A'},
        'V0': {'tag': 'v', 'i': 0, 'decimal': 3, 'unit': 'kV'},
        'V1': {'tag': 'v', 'i': 1, 'decimal': 3, 'unit': 'kV'},
    },
    '2W-Transformer': {
        'P0': {'tag': 'p', 'i': 0, 'decimal': 3, 'unit': 'kW'},
        'P1': {'tag': 'p', 'i': 1, 'decimal': 3, 'unit': 'kW'},
        'Q0': {'tag': 'q', 'i': 0, 'decimal': 3, 'unit': 'kVar'},
        'Q1': {'tag': 'q', 'i': 1, 'decimal': 3, 'unit': 'kVar'},
        'i0': {'tag': 'i', 'i': 0, 'decimal': 3, 'unit': 'A'},
        'i1': {'tag': 'i', 'i': 1, 'decimal': 3, 'unit': 'A'},
        'V0': {'tag': 'v', 'i': 0, 'decimal': 3, 'unit': 'kV'},
        'V1': {'tag': 'v', 'i': 1, 'decimal': 3, 'unit': 'kV'},
    },
    'PWM': {
        'P0': {'tag': 'p', 'i': 0, 'decimal': 3, 'unit': 'kW'},
        'P1': {'tag': 'p', 'i': 1, 'decimal': 3, 'unit': 'kW'},
        'Q0': {'tag': 'q', 'i': 0, 'decimal': 3, 'unit': 'kVar'},
        'Q1': {'tag': 'q', 'i': 1, 'decimal': 3, 'unit': 'kVar'},
        'i0': {'tag': 'i', 'i': 0, 'decimal': 3, 'unit': 'A'},
        'i1': {'tag': 'i', 'i': 1, 'decimal': 3, 'unit': 'A'},
        'V0': {'tag': 'v', 'i': 0, 'decimal': 3, 'unit': 'kV'},
        'V1': {'tag': 'v', 'i': 1, 'decimal': 3, 'unit': 'kV'},
    },
    'DC-DC-Converter': {
        'P0': {'tag': 'p', 'i': 0, 'decimal': 3, 'unit': 'kW'},
        'P1': {'tag': 'p', 'i': 1, 'decimal': 3, 'unit': 'kW'},
        'Q0': {'tag': 'q', 'i': 0, 'decimal': 3, 'unit': 'kVar'},
        'Q1': {'tag': 'q', 'i': 1, 'decimal': 3, 'unit': 'kVar'},
        'i0': {'tag': 'i', 'i': 0, 'decimal': 3, 'unit': 'A'},
        'i1': {'tag': 'i', 'i': 1, 'decimal': 3, 'unit': 'A'},
        'V0': {'tag': 'v', 'i': 0, 'decimal': 3, 'unit': 'kV'},
        'V1': {'tag': 'v', 'i': 1, 'decimal': 3, 'unit': 'kV'},
    },
    'AC-Load': {
        'P': {'tag': 'p', 'i': None, 'decimal': 3, 'unit': 'kW'},
        'Q': {'tag': 'q', 'i': None, 'decimal': 3, 'unit': 'kVar'},
        'i': {'tag': 'i', 'i': None, 'decimal': 3, 'unit': 'A'},
        'V': {'tag': 'v', 'i': None, 'decimal': 3, 'unit': 'kV'},
    },
    'DC-Load': {
        'P': {'tag': 'p', 'i': None, 'decimal': 3, 'unit': 'kW'},
        'i': {'tag': 'i', 'i': None, 'decimal': 3, 'unit': 'A'},
        'V': {'tag': 'v', 'i': None, 'decimal': 3, 'unit': 'kV'},
    },
    'AC-PV': {
        'P': {'tag': 'p', 'i': None, 'decimal': 3, 'unit': 'kW'},
        'i': {'tag': 'i', 'i': None, 'decimal': 3, 'unit': 'A'},
        'V': {'tag': 'v', 'i': None, 'decimal': 3, 'unit': 'kV'},
    },
    'DC-PV': {
        'P': {'tag': 'p', 'i': None, 'decimal': 3, 'unit': 'kW'},
        'i': {'tag': 'i', 'i': None, 'decimal': 3, 'unit': 'A'},
        'V': {'tag': 'v', 'i': None, 'decimal': 3, 'unit': 'kV'},
    },
    'AC-Wind': {
        'P': {'tag': 'p', 'i': None, 'decimal': 3, 'unit': 'kW'},
        'Q': {'tag': 'q', 'i': None, 'decimal': 3, 'unit': 'kVar'},
        'i': {'tag': 'i', 'i': None, 'decimal': 3, 'unit': 'A'},
        'V': {'tag': 'v', 'i': None, 'decimal': 3, 'unit': 'kV'},
    },
    'DC-Wind': {
        'P': {'tag': 'p', 'i': None, 'decimal': 3, 'unit': 'kW'},
        'i': {'tag': 'i', 'i': None, 'decimal': 3, 'unit': 'A'},
        'V': {'tag': 'v', 'i': None, 'decimal': 3, 'unit': 'kV'},
    },
    'AC-BESS': {
        'P': {'tag': 'p', 'i': None, 'decimal': 3, 'unit': 'kW'},
        'i': {'tag': 'i', 'i': None, 'decimal': 3, 'unit': 'A'},
        'V': {'tag': 'v', 'i': None, 'decimal': 3, 'unit': 'kV'},
    },
    'DC-BESS': {
        'P': {'tag': 'p', 'i': None, 'decimal': 3, 'unit': 'kW'},
        'i': {'tag': 'i', 'i': None, 'decimal': 3, 'unit': 'A'},
        'V': {'tag': 'v', 'i': None, 'decimal': 3, 'unit': 'kV'},
    },
    'Switch': {},
}

el_format = {
    'ExternalGrid': {
        'Vn': {'min': 0.001, 'max': 999.999, 'decimal': 3, 'unit': 'kV', 'default': None},
    },
    'AC-Node': {
        'Vn': {'min': 0.001, 'max': 999.999, 'decimal': 3, 'unit': 'kV', 'default': 0.4},
    },
    'DC-Node': {
        'Vn': {'min': 0.001, 'max': 999.999, 'decimal': 3, 'unit': 'kV', 'default': 0.4},
    },
    'AC-Line': {
        'B0': {'min': 0.001, 'max': 999.9999, 'decimal': 3, 'unit': 'uS', 'default': 0},
        'B1': {'min': 0.001, 'max': 999.9999, 'decimal': 3, 'unit': 'uS', 'default': 0},
        'In': {'min': 0.001, 'max': 999.9999, 'decimal': 3, 'unit': 'A', 'default': 100},
        'R0': {'min': 0.001, 'max': 999.99999, 'decimal': 5, 'unit': 'Ohm', 'default': 0},
        'R1': {'min': 0, 'max': 999.99999, 'decimal': 5, 'unit': 'Ohm', 'default': 0},
        'X0': {'min': 0.00001, 'max': 999.99999, 'decimal': 5, 'unit': 'Ohm', 'default': 0},
        'X1': {'min': 0.00001, 'max': 999.99999, 'decimal': 5, 'unit': 'Ohm', 'default': 0},
        'length': {'min': 0, 'max': 9999.999, 'decimal': 3, 'unit': 'Km', 'default': 1},
    },
    'DC-Line': {
        'In': {'min': 0.001, 'max': 999.9999, 'decimal': 3, 'unit': 'A', 'default': 100},
        'R1': {'min': 0, 'max': 999.99999, 'decimal': 5, 'unit': 'Ohm', 'default': 0},
        'X1': {'min': 0, 'max': 999.99999, 'decimal': 5, 'unit': 'Ohm', 'default': 0},
        'length': {'min': 0, 'max': 9999.999, 'decimal': 3, 'unit': 'Km', 'default': 1},
    },
    'Switch': {},
    '2W-Transformer': {
        'Sr': {'min': 0.001, 'max': 99999.9, 'decimal': 1, 'unit': 'kVA', 'default': 1000},
        # 'Vn0': {'min': 0, 'max': 999.999, 'decimal': 3, 'unit': 'kV'},
        # 'Vn1': {'min': 0, 'max': 999.999, 'decimal': 3, 'unit': 'kV'},
        'XHL': {'min': 0, 'max': 99.99999, 'decimal': 3, 'unit': '%', 'default': 0},
    },
    'PWM': {
        'Sr': {'min': 0.001, 'max': 99999.9, 'decimal': 1, 'unit': 'kVA', 'default': 1000},
        # 'Vn0': {'min': 0, 'max': 999.999, 'decimal': 3, 'unit': 'kV'},
        # 'Vn1': {'min': 0, 'max': 999.999, 'decimal': 3, 'unit': 'kV'},
        # 'XHL': {'min': 0, 'max': 99.99999, 'decimal': 3, 'unit': '%'},
    },
    'DC-DC-Converter': {
        'Sr': {'min': 0.001, 'max': 99999.9, 'decimal': 1, 'unit': 'kVA', 'default': 1000},
        # 'Vn0': {'min': 0, 'max': 999.999, 'decimal': 3, 'unit': 'kV'},
        # 'Vn1': {'min': 0, 'max': 999.999, 'decimal': 3, 'unit': 'kV'},
        # 'XHL': {'min': 0, 'max': 99.99999, 'decimal': 3, 'unit': '%'},
    },
    'AC-Load': {
        'P': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'kW', 'default': 100},
        # 'Q': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'kVAr'},
        'cosPhi': {'min': -1, 'max': 1, 'decimal': 4, 'unit': '', 'default': 1},
        'Customers': {'min': 0, 'max': 1000, 'decimal': 0, 'unit': '', 'default': 1},
    },
    'DC-Load': {
        'P': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'kW', 'default': 100},
        'Customers': {'min': 0, 'max': 1000, 'decimal': 0, 'unit': '', 'default': 1},
    },
    'AC-PV': {
        'P': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'kW', 'default': 100},
    },
    'DC-PV': {
        'P': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'kW', 'default': 100},
    },
    'AC-Wind': {
        'P': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'kW', 'default': 100},
        # 'Q': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'kVAr'},
        'cosPhi': {'min': -1, 'max': 1, 'decimal': 4, 'unit': '', 'default': 1},
        'eff': {'min': 0, 'max': 1, 'decimal': 4, 'unit': '', 'default': 1},
    },
    'Turbine': {
        'P': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'kW', 'default': 100},
        # 'Q': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'kVAr'},
        'cosPhi': {'min': -1, 'max': 1, 'decimal': 4, 'unit': '', 'default': 1},
        'eff': {'min': 0, 'max': 1, 'decimal': 4, 'unit': '', 'default': 1},
    },
    'Diesel-Motor': {
        'P': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'kW', 'default': 100},
        # 'Q': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'kVAr'},
        'cosPhi': {'min': -1, 'max': 1, 'decimal': 4, 'unit': '', 'default': 1},
        'eff': {'min': 0, 'max': 1, 'decimal': 4, 'unit': '', 'default': 1},
    },
    'DC-Wind': {
        'P': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'kW', 'default': 100},
        'eff': {'min': 0, 'max': 1, 'decimal': 4, 'unit': '', 'default': 1},
    },
    'AC-BESS': {
        'P': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'kW', 'default': 100},
        'eff': {'min': 0, 'max': 1, 'decimal': 4, 'unit': '', 'default': 1},
        'cap': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'kWh', 'default': 100},
        'SOC': {'min': 0, 'max': 100, 'decimal': 2, 'unit': '%', 'default': 50},
    },
    'DC-BESS': {
        'P': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'kW', 'default': 100},
        'eff': {'min': 0, 'max': 1, 'decimal': 4, 'unit': '', 'default': 1},
        'cap': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'kWh', 'default': 100},
    },
}

DC_elem = ['DC-Line', 'DC-DC-Converter', 'DC-Load', 'DC-BESS', 'DC-PV', 'DC-Wind']

prof_elem = ['AC-Load', 'DC-Load', 'AC-BESS', 'DC-BESS', 'AC-PV', 'DC-PV', 'AC-Wind', 'DC-Wind', 'Diesel-Motor',
             'Turbine']

anom_typol_par = {
    'scale': 'value',
    '(1-exp) decrease': 'alpha',
    '(-x+1) decrease': 'alpha'
}

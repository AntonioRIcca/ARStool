import os
mainpath = os.getcwd()


def v_initialize():
    for k in list(v.keys()):
        del v[k]
    print(v)


fn = {
    'lf': False,
    'rel': False,
    'optstor': False,
}

fn_en = {
    'lf': True,
    'anom': False,
    'opf': False,
    'rel': False,
    'gm': False,
    'onr': False,
}

v = dict()
vdss = dict()

mc = {
    'Vsource': ['ExternalGrid'],
    'LoadShape': [],
    'GrowthShape': [],
    'TCC_Curve': [],
    'Spectrum': [],
    'Line': ['AC-Line', 'DC-Line'],
    'Load': ['AC-Load', 'DC-Load'],
    'Transformer': ['2W-Transformer', 'PWM', 'DC-DC-Converter'],
    'Generator': ['BESS', 'PV', 'AC-Wind', 'DC-Wind', 'Diesel-Motor'],
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
    'bess': 'BESS',
    'pv': 'PV',
    'wind': 'AC-Wind',
    'dc-micro-wind': 'DC-Wind',
    'diesel': 'Diesel-Motor',
    'bb': 'AC-Node',
    'node': 'AC-Node',
    'dc-bb': 'DC-Node',
    'dc-node': 'DC-Node',
    'sourcebus': 'AC-Node'
}

new_par_dict = {
    'PV': {
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

    'BESS': {
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
            },
            'XHL': {
                'label': 'XHL',
                'unit': '',
            },
            'imag': {
                'label': '%imag',
                'unit': '%',
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
            },
            'B0': {
                'label': 'B0',
                'unit': 'uS',
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
    'PV': {
        'P': 'kw',
        'Vn': 'kv'
    },

    'BESS': {
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
    'PV': {
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
    'BESS': {
        'P': {'tag': 'p', 'i': None, 'decimal': 3, 'unit': 'kW'},
        'i': {'tag': 'i', 'i': None, 'decimal': 3, 'unit': 'A'},
        'V': {'tag': 'v', 'i': None, 'decimal': 3, 'unit': 'kV'},
    },

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
        'B0': {'min': 0, 'max': 999.9999, 'decimal': 3, 'unit': 'uS', 'default': 0},
        'B1': {'min': 0, 'max': 999.9999, 'decimal': 3, 'unit': 'uS', 'default': 0},
        'In': {'min': 0.001, 'max': 999.9999, 'decimal': 3, 'unit': 'A', 'default': 100},
        'R0': {'min': 0, 'max': 999.99999, 'decimal': 5, 'unit': 'Ohm', 'default': 0},
        'R1': {'min': 0, 'max': 999.99999, 'decimal': 5, 'unit': 'Ohm', 'default': 0},
        'X0': {'min': 0, 'max': 999.99999, 'decimal': 5, 'unit': 'Ohm', 'default': 0},
        'X1': {'min': 0, 'max': 999.99999, 'decimal': 5, 'unit': 'Ohm', 'default': 0},
        'length': {'min': 0, 'max': 9999.999, 'decimal': 3, 'unit': 'Km', 'default': 1},
    },
    'DC-Line': {
        'In': {'min': 0.001, 'max': 999.9999, 'decimal': 3, 'unit': 'A', 'default': 100},
        'R1': {'min': 0, 'max': 999.99999, 'decimal': 5, 'unit': 'Ohm', 'default': 0},
        'X1': {'min': 0, 'max': 999.99999, 'decimal': 5, 'unit': 'Ohm', 'default': 0},
        'length': {'min': 0, 'max': 9999.999, 'decimal': 3, 'unit': 'Km', 'default': 1},
    },
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
    'PV': {
        'P': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'kW', 'default': 100},
    },
    'AC-Wind': {
        'P': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'kW', 'default': 100},
        # 'Q': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'kVAr'},
        'cosPhi': {'min': -1, 'max': 1, 'decimal': 4, 'unit': '', 'default': 1},
        'eff': {'min': 0, 'max': 1, 'decimal': 4, 'unit': '', 'default': 1},
    },
    'DC-Wind': {
        'P': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'kW', 'default': 100},
        'eff': {'min': 0, 'max': 1, 'decimal': 4, 'unit': '', 'default': 1},
    },
    'BESS': {
        'P': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'kW', 'default': 100},
        'eff': {'min': 0, 'max': 1, 'decimal': 4, 'unit': '', 'default': 1},
        'cap': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'kWh', 'default': 100},
    },
}

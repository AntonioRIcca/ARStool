v = dict()
vdss = dict()

mc = {
    'Vsource': ['ExternalGrid'],
    'Line': ['AC-Line', 'DC-Line'],
    'Transformer': ['2W-Transformer', 'PWM', 'DC-DC-Converter'],
    'Load': ['AC-Load', 'DC-Load'],
    'Generator': ['BESS', 'PV', 'AC-Wind', 'DC-Wind', 'Diesel-Motor'],
    'Node': ['Node']
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
    'bb': 'Node',
    'node': 'Node'
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
        'f': 'pf',
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
    },
    'DC-Load': {
        'P': 'kw',
    },
    'Diesel-Motor': {},
    'Node': {},
    'ExternalGrid': {},
}

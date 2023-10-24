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


el_format = {
    'ExternalGrid': {
        'Vn': {'min': 0, 'max': 999.999, 'decimal': 3, 'unit': 'kV'},
    },
    'Node': {
        'Vn': {'min': 0, 'max': 999.999, 'decimal': 3, 'unit': 'kV'},
    },
    'AC-Line': {
        'C0': {'min': 0, 'max': 999.9999, 'decimal': 3, 'unit': 'uS'},
        'C1': {'min': 0, 'max': 999.9999, 'decimal': 3, 'unit': 'uS'},
        'In': {'min': 0, 'max': 999.9999, 'decimal': 3, 'unit': 'A'},
        'R0': {'min': 0, 'max': 999.99999, 'decimal': 5, 'unit': 'Ohm'},
        'R1': {'min': 0, 'max': 999.99999, 'decimal': 5, 'unit': 'Ohm'},
        'X0': {'min': 0, 'max': 999.99999, 'decimal': 5, 'unit': 'Ohm'},
        'X1': {'min': 0, 'max': 999.99999, 'decimal': 5, 'unit': 'Ohm'},
        'length': {'min': 0, 'max': 9999.999, 'decimal': 3, 'unit': 'Km'},
    },
    'DC-Line': {
        'In': {'min': 0, 'max': 999.9999, 'decimal': 3, 'unit': 'A'},
        'R1': {'min': 0, 'max': 999.99999, 'decimal': 5, 'unit': 'Ohm'},
        'X1': {'min': 0, 'max': 999.99999, 'decimal': 5, 'unit': 'Ohm'},
        'length': {'min': 0, 'max': 9999.999, 'decimal': 3, 'unit': 'Km'},
    },
    '2W-Transformer': {
        'Sr': {'min': 0, 'max': 99999.9, 'decimal': 1, 'unit': 'kVA'},
        'Vn0': {'min': 0, 'max': 999.999, 'decimal': 3, 'unit': 'kV'},
        'Vn1': {'min': 0, 'max': 999.999, 'decimal': 3, 'unit': 'kV'},
        'XHL': {'min': 0, 'max': 99.99999, 'decimal': 5, 'unit': '%'},
    },
    'PWM': {
        'Sr': {'min': 0, 'max': 99999.9, 'decimal': 1, 'unit': 'kVA'},
        'Vn0': {'min': 0, 'max': 999.999, 'decimal': 3, 'unit': 'kV'},
        'Vn1': {'min': 0, 'max': 999.999, 'decimal': 3, 'unit': 'kV'},
        'XHL': {'min': 0, 'max': 99.99999, 'decimal': 5, 'unit': '%'},
    },
    'DC-DC-Converter': {
        'Sr': {'min': 0, 'max': 99999.9, 'decimal': 1, 'unit': 'kVA'},
        'Vn0': {'min': 0, 'max': 999.999, 'decimal': 3, 'unit': 'kV'},
        'Vn1': {'min': 0, 'max': 999.999, 'decimal': 3, 'unit': 'kV'},
        'XHL': {'min': 0, 'max': 99.99999, 'decimal': 5, 'unit': '%'},
    },
    'AC-Load': {
        'P': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'Ohm'},
        'Q': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'Ohm'},
        'cosPhi': {'min': -1, 'max': 1, 'decimal': 4, 'unit': ''},
    },
    'DC-Load': {
        'P': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'Ohm'},
    },
    'PV': {
        'P': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'Ohm'},
    },
    'AC-Wind': {
        'P': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'Ohm'},
        'Q': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'Ohm'},
        'cosPhi': {'min': -1, 'max': 1, 'decimal': 4, 'unit': ''},
        'eff': {'min': 0, 'max': 1, 'decimal': 4, 'unit': ''},
    },
    'DC-Wind': {
        'P': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'Ohm'},
        'eff': {'min': 0, 'max': 1, 'decimal': 4, 'unit': ''},
    },
    'BESS': {
        'P': {'min': 0, 'max': 99999.999, 'decimal': 3, 'unit': 'Ohm'},
        'eff': {'min': 0, 'max': 1, 'decimal': 4, 'unit': ''},
        'cap': {'min': 0, 'max': 1, 'decimal': 4, 'unit': ''},
    },
}

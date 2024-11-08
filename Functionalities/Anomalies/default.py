anomalies = {
    'AC-PV': {
        'Hourly_Degradation': {
            'rate': 0.2
        },
        'Partial_Shading': {
            'scale': {
                'lambda_a': 3,
                'lambda_duration': 3,
                'is_fixed': False,
                'value': 0.7,
            }
        },
        'Dust': {
            '(-x+1) decrease': {
                'lambda_a': 1,
                'lambda_duration': 1.5,
                'is_fixed': False,
                'alpha': 1,
            }
        },
        'Hot_Spot': {
            'scale': {
                'lambda_a': 1,
                'lambda_duration': 4,
                'is_fixed': False,
                'value': 0.5,
            }
        }
    },

    'DC-PV': {
        'Hourly_Degradation': {
            'rate': 0.2
        },
        'Partial_Shading': {
            'scale': {
                'lambda_a': 3,
                'lambda_duration': 3,
                'is_fixed': False,
                'value': 0.7,
            }
        },
        'Dust': {
            '(-x+1) decrease': {
                'lambda_a': 1,
                'lambda_duration': 1.5,
                'is_fixed': False,
                'alpha': 1,
            }
        },
        'Hot_Spot': {
            'scale': {
                'lambda_a': 1,
                'lambda_duration': 4,
                'is_fixed': False,
                'value': 0.5,
            }
        }
    }
}

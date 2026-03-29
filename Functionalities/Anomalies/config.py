
import utils_using_xi as ut
import anomaly_using_xi as an
import copy

APPLY_AGING = True

# Anni di simulazione
NUM_YEARS = 5

# Lunghezza del segnale
N = 24*7 #24 * 365 * NUM_YEARS

SEED = 23

#     'type': 'scale', --> tipo di modifica da applicare al segnale
#     'lambda_a': n/m --> frequenza di occorrenza: n eventi ogni m ore
#     'lambda_duration': x --> durata media in ore
#     'is_fixed': False --> la durata è fissa o no?
#     'internal_params': {'value': 0.3} --> Dipende dal tipo di modifica da applicare al segnale in questo caso è la percentuale con cui viene 
#                                           ridotto il segnale di partenza
#     'internal_params': {'type': '-x+1', --> In questo caso è la curva di envelope
#                            'alpha': k/l} --> # Il segnale diventa k volte il suo valore iniziale in l ore
#     'internal_params': {'type': '1-exp', --> In questo caso è la curva di envelope
#                            'alpha': k*0.69} --> # Il segnale si dimezza all'istante k

# Parametri di default delle anomalie
DEFAULT_PARAMS_PV = {
    'Hourly_Degradation':
    {
        # 20% in 15 anni per il degrado (si assume che il degrado tenga conto anche della delaminazione)
        'rate': 0.2/ (15 * 365 * 24)
    },

    'Partial_Shading': {
        'type': 'scale',
        'lambda_a': 3/(24),
        'lambda_duration': 3,
        'is_fixed': False,
        'internal_params': {'value': 0.7}
    },

    # Si suppone che i pannelli vengano ripuliti ogni due mesi quindi possiamo supporre un evento ogni due mesi.
    # La durata è di 1.5 mesi
    'Dust': {
        'type': 'decrease',
        'lambda_a': 1/(2*30*24),
        'lambda_duration': 1.5*30*24,
        'is_fixed': False,
        # Riduzione del 100% in 2 anni se non vi è intervento
        'internal_params': {'type': '-x+1', 
                            'alpha': 1/(2*365*24)}
    },
    
    'Hot_Spot': {
        'type': 'scale',
        'lambda_a': 1/(1*365*24),
        'lambda_duration': 4*30*24,
        'is_fixed': False,
        'internal_params': {'value': 0.5}
    }
}

# Parametri di default delle anomalie
DEFAULT_PARAMS_WIND = {
    'Hourly_Degradation':
    {
        # 1.6% ogni anno 
        'rate': 0.016 / (365 * 24)
    },

    'Icing': {
        'type': 'scale',
        'lambda_a': 5/(1 * 365 * 24),
        'lambda_duration': 10,
        'is_fixed': False,
        'internal_params': {'value': 0.3}
    },
}

# Parametri di default delle anomalie
DEFAULT_PARAMS_FC = {
    'Hourly_Degradation':
    {
        # 1% ogni anno 
        'rate': 0.01 / (365 * 24)
    },  

    'Crepa_Membrana': {
        'type': 'decrease',
        'lambda_a': 1/(5*365*24),
        'lambda_duration': -1,
        'is_fixed': True,
        'internal_params': {'type': '1-exp', 
                            'alpha': 20 * 0.69}
    },

    'Foratura_Membrana': {
        'type': 'decrease',
        'lambda_a': 1/(5*365*24),
        'lambda_duration': -1,
        'is_fixed': True,
        'internal_params': {'type': '1-exp', 
                            'alpha': 5 * 0.69}
    },

    'Cross_Over_H2': {
        'type': 'decrease',
        'lambda_a': 1/(5*365*24),
        'lambda_duration': 20,
        'is_fixed': True,
        'internal_params': {'type': '-x+1', 
                            'alpha': 0.2/24}
    },

    'Agglomerazione_catalizzatore': {
        'type': 'decrease',
        'lambda_a': 1/(5*365*24),
        'lambda_duration': 20,
        'is_fixed': True,
        'internal_params': {'type': '-x+1', 
                            'alpha': 0.5/(2*30*24)}
    },

    'Contaminazione_catalizzatore': {
        'type': 'decrease',
        'lambda_a': 1/(5*365*24),
        'lambda_duration': 20,
        'is_fixed': True,
        'internal_params': {'type': '-x+1', 
                            'alpha': 0.5/(2*30*24)}
    },

    'Ossidazione_Supporto_Carbonioso': {
        'type': 'decrease',
        'lambda_a': 1/(5*365*24),
        'lambda_duration': 20,
        'is_fixed': True,
        'internal_params': {'type': '-x+1', 
                            'alpha': 0.5/(2*30*24)}
    },

    'Allagamento_catodo': {
        'type': 'decrease',
        'lambda_a': 1/(5*365*24),
        'lambda_duration': 24,
        'is_fixed': True,
        'internal_params': {'type': '-x+1', 
                            'alpha': 0.4/(24)}
    },
}

DEFAULT_PARAMS_BATTERY = {
    'Hourly_Degradation':
    {
        # 1.37% ogni anno 
        'rate': 0.0137 / (365 * 24)
    },  
    
}

DEFAULT_PARAMS_CONVERTER = {
    'Failure_Of_Internal_Components': {
        'type': 'set_values',
        'lambda_a': 1/(3*365*24),
        'lambda_duration': -1,
        'is_fixed': True,
        'internal_params': {'value': 0}
    },  
}

def create_anomaly(name, seed, params):
    """Crea un'anomalia in base ai parametri forniti"""
    return {
        'description': name,
        'seed': seed,
        'anomaly': an.Anomaly_with_params(
            params['type'],
            params['lambda_a'],
            params['lambda_duration'],
            params['is_fixed'],
            params['internal_params']
        )
    }

# Funzione per aggiornare i parametri dinamicamente in base all'input utente
def update_anomaly_params(input_params, default_params):
    """Aggiorna i parametri delle anomalie in base agli input dell'utente"""
    updated_params = copy.deepcopy(default_params)
    for anomaly, params in input_params.items():
        if anomaly in updated_params:
            updated_params[anomaly].update(params)
    return updated_params
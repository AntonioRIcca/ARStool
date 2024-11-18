import numpy as np
import Functionalities.Anomalies.utils_using_xi as ut
import matplotlib.pyplot as plt

N_MAX_ANOMALIES = 10000

class Anomaly:

    def __init__(self, type_anomaly, lambda_a, lambda_duration, is_fixed_duration=False):
        self.type_anomaly = type_anomaly
        self.lambda_a = lambda_a                        # N anomalie su K steps
        self.lambda_duration = lambda_duration          # Media della durata dell'anomalia
        self.is_fixed_duration = is_fixed_duration      # Indica se la durata va considerata fissa oppure come variabile aleatoria
        #self.mask = mask # TODO - inserire una maschera che indica dove è possibile inserire le anomalie
        
        self.do_round = False   # Effettua l'approssimazione agli interi

    def generate(self, n_anomalies, seed):
        np.random.seed(seed)     

        debug = False
        # Calcola i tempi tra due anomalie successive usando la distribuzione esponenziale
        inter_anomaly_times = np.random.exponential(scale=1/self.lambda_a, size=n_anomalies)
        
        if (self.do_round):
            # Arrotonda i tempi tra due anomalie a numeri interi
            inter_anomaly_times = np.round(inter_anomaly_times).astype(int)
        
        if (self.is_fixed_duration):
            durations = self.lambda_duration * np.ones((n_anomalies,))
        else:
            # Calcola le durate dei guasti usando la distribuzione esponenziale
            # TODO - verificare se scale = 1/duration o duration
            durations = np.random.exponential(scale=self.lambda_duration, size=n_anomalies)
            
            if (self.do_round):
                # Arrotonda le durate a numeri interi
                durations = np.ceil(durations).astype(int)
            
        if (debug):
            inter_anomaly_times 
            plt.hist(inter_anomaly_times)

        # Calcola gli istanti temporali di inizio dei guasti
        start_anomaly_times_all = np.cumsum(inter_anomaly_times)
        if (np.any(durations == -1)):
            end_anomaly_times_all = -1 * np.ones_like(start_anomaly_times_all)
        else:
            end_anomaly_times_all = start_anomaly_times_all + durations
        
        # Evita sovrapposizioni tra anomalie: se l'inizio di un'anomalia (i-esima) 
        # parte prima della fine della precedente anomalia (i-1 esima) 
        # allora sposta l'inizio dell'i-esima
        # for i in range(1, n_anomalies):
        #     if start_anomaly_times_all[i] < end_anomaly_times_all[i - 1]:
        #         start_anomaly_times_all[i] = end_anomaly_times_all[i - 1]:

        # Evita sovrapposizioni tra anomalie: se l'inizio di un'anomalia (i-esima) 
        # parte prima della fine della precedente anomalia (i-1 esima) 
        # allora elimino l'i-esima anomalia
        # TODO -  questo andrebbe fatto considerando tutte le anomalie successive e non solo la prima dopo
        for i in range(1, n_anomalies):
            if start_anomaly_times_all[i] < end_anomaly_times_all[i - 1]:
                start_anomaly_times_all[i] = -100
                end_anomaly_times_all[i] = -100
        
        start_anomaly_times_all = start_anomaly_times_all[start_anomaly_times_all!=-100]
        end_anomaly_times_all = end_anomaly_times_all[end_anomaly_times_all!=-100]

        if (self.do_round):
            start_anomaly_times_all = np.round(start_anomaly_times_all).astype(int)
            end_anomaly_times_all = np.round(end_anomaly_times_all).astype(int)

        return start_anomaly_times_all, end_anomaly_times_all
    
class Anomaly_with_params(Anomaly):
     def __init__(self, type_anomaly, lambda_a, lambda_duration, is_fixed_duration=False, params=None):

        # Chiama il costruttore della classe base (Anomaly) per inizializzare i parametri ereditati
        super().__init__(type_anomaly, lambda_a, lambda_duration, is_fixed_duration)
        
        # Inizializza il nuovo parametro params
        self.params = params

# Genera le posizioni di inizio e fine di una certa anomalia
def generate_anomaly_positions(anom: Anomaly, descr : str, key: str, observation_window: int, idx_min: int, idx_max: int, an_vct: np.array, seed: int):
    #Se l'anomalia successiva si sovrappone alla precedente non deve essere inserita
    n_anomalies = N_MAX_ANOMALIES       # Numero massimo di anomalie da generare
    start_anomaly_times_all, end_anomaly_times_all = anom.generate(n_anomalies, seed)
    
    # Considera solo le anomalie che cadono nella finestra di osservazione.
    # Nel caso in cui la finestra di osservazione è più piccola, adatto opportunamente 
    # l'inizio e la fine dell'anomalia
    orig_start_anomaly_times = []
    orig_end_anomaly_times = []
    for k in zip(start_anomaly_times_all, end_anomaly_times_all):
        _start = k[0]
        _end = k[1]
        if (_end == -1):
            _end = idx_max

        if ((_end < idx_min) | (_start > idx_max)):
            continue
        else:
            if ((_start >= idx_min) & (_end <= idx_max)):
                orig_start_anomaly_times.append(_start)
                orig_end_anomaly_times.append(_end)
            elif ((_start >= idx_min) & (_end > idx_max)):
                orig_start_anomaly_times.append(_start)
                orig_end_anomaly_times.append(idx_max)
            elif ((_start < idx_min) & (_end <= idx_max)):
                orig_start_anomaly_times.append(idx_min)
                orig_end_anomaly_times.append(_end)
            elif ((_start < idx_min) & (_end > idx_max)):
                orig_start_anomaly_times.append(idx_min)
                orig_end_anomaly_times.append(idx_max)

    
    # In alcuni casi è possibile che la selezione sulla finestra di osservazione faccia perdere
    # la fine di un evento (quando l'evento originario è oltre la finestra di osservazione). 
    # In questo caso si fa in modo che l'ultimo evento finisca proprio alla finestra di osservazione
    if (len(orig_end_anomaly_times) < len(orig_start_anomaly_times)):
        D = len(orig_start_anomaly_times) - len(orig_end_anomaly_times)
        orig_end_anomaly_times = np.append(orig_end_anomaly_times, observation_window*np.ones(D,))
    
    idx_start_anomaly_times = np.floor(orig_start_anomaly_times).astype(int)
    idx_end_anomaly_times = np.floor(orig_end_anomaly_times).astype(int)
    
    dict_anomalies = []

    i_event = 1
    for i in range(0, len(idx_start_anomaly_times)):
        index_end = int(min(observation_window-1, idx_end_anomaly_times[i]) + 1)
        real_end = min(observation_window, orig_end_anomaly_times[i])

        if (idx_start_anomaly_times[i] == index_end):
            sub_vct = an_vct[idx_start_anomaly_times[i]]
        else:
            sub_vct = an_vct[idx_start_anomaly_times[i] : index_end]
        
        # Gestione della sovrapposizione tra anomalie successive
        # Se almeno uno dei data point nel sub vector non è 0, ovvero per quel data point
        # già fa parte di un'anomalia, allora l'anomalia corrente viene eliminata
        if (np.all(sub_vct==0)):
            print(descr + ' ' + anom.type_anomaly + ' FROM ' + str(orig_start_anomaly_times[i]) + ' TO ' + str(real_end))
        
            an_vct[idx_start_anomaly_times[i]:index_end] = key
            event = {
                    'descr': descr,
                    'orig_start' : float(orig_start_anomaly_times[i]), 
                    'orig_end' : float(real_end), 
                    'idx' : np.array(range(idx_start_anomaly_times[i], index_end)).tolist() }
            dict_anomalies.append({'event' + str(i_event) : event})
            i_event += 1
        else:
           print(descr + ' [' + anom.type_anomaly + '] FROM ' + str(orig_start_anomaly_times[i]) + ' TO ' + str(real_end) + ' - NOT INSERTED')

    return an_vct, dict_anomalies


# Applica le perturbazioni al segnale
def generate_anomalies(anom: Anomaly_with_params, key: str, an_vct: np.array, N: int, x_i: np.array, b_i: np.array):
 
    sequences = ut.find_sequences_of_number(an_vct, key)
    type_anomaly = anom.type_anomaly
    params = anom.params
    
    x_i_new = x_i.copy()
    b_i_new = b_i.copy()

    if (len(sequences)>0):
        for seq in sequences:
            a_time_start = seq[0]

            # Il più uno è dovuto al fatto che le funzioni di modifica del segnale non considerano l'ultimo valore
            a_time_end = seq[-1]+1
            
            # print (np.array(range(a_time_start, a_time_end)))
            # TODO - [Possibilità] Parametri come Variabili Aleatorie
            # TODO - Definire un clipping - extreme value o shift o trend o noise, il picco non può superare il picco massimo osservato nel vettore

            print('[Time: ' + str(a_time_start) + ' to ' + str(a_time_end-1) + ']- [Type: ' + str(key) + '-' + type_anomaly + ']')
            if (type_anomaly == 'set_values'):
                value = params['value']
                x_i_tmp, b_i_tmp = ut.set_values(N, timestamps_start=[a_time_start], timestamps_stop=[a_time_end], values = [value])
            
            elif (type_anomaly == 'scale'):
                value = params['value']
                x_i_tmp, b_i_tmp = ut.scale(N, timestamp_start=a_time_start, timestamp_stop=a_time_end, value = value)

            elif (type_anomaly == 'shift'):
                value = params['value']
                x_i_tmp, b_i_tmp = ut.add_shift(N, timestamp_start=a_time_start, timestamp_stop=a_time_end, value = value)
            
            elif (type_anomaly == 'trend'):
                slope = params['slope']
                x_i_tmp, b_i_tmp = ut.add_trend(N, timestamp_start=a_time_start, timestamp_stop=a_time_end, slope=slope)
            
            elif (type_anomaly == 'noise'):
                sigma = params['sigma']
                x_i_tmp, b_i_tmp = ut.add_noise(N, timestamp_start=a_time_start, timestamp_stop=a_time_end, sigma=sigma)
            
            elif (type_anomaly == 'decrease'):
                type = params['type']
                alpha = params['alpha']
                x_i_tmp, b_i_tmp = ut.modulate_signal(N, timestamp_start=a_time_start, timestamp_stop=a_time_end, type = type, alpha = alpha)

            elif (type_anomaly == 'oscillation'):
                sigma = params['sigma']
                A = params['A']
                freq = params['freq']
                x_i_tmp, b_i_tmp = ut.add_oscillation(N, t0=a_time_start, f0=freq, sigma=sigma, A=A)
            else:
                print ('ERROR')
                return -1,-1
            
            x_i_new = x_i_new * x_i_tmp
            b_i_new = b_i_new * x_i_tmp + b_i_tmp

    return x_i_new, b_i_new

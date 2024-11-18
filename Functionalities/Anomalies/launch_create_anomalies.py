import copy

import yaml
import copy as cp
import time

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import Functionalities.Anomalies.utils_using_xi as ut
import Functionalities.Anomalies.anomaly_using_xi as an

import Functionalities.Anomalies.config_anomaly as cfg

from variables import *

# DATA_DIR = 'F:\\Work\\PTR22-24-AnomalyDetection\\DATA\\'
# FILE_NAME = 'test4.yml'
# PLOT_FIGURE = False
#
# with open(DATA_DIR + FILE_NAME, 'r') as file:
#     v = yaml.safe_load(file)
# v_new = cp.deepcopy(v)

# grid = cp.deepcopy(v['_grid_'])
# del v['_grid_']


def lauch_create_anomalies():
    PLOT_FIGURE = False
    # v_new = cp.deepcopy(v)

    N = grid['profile']['points']

    anom_nodes = cfg.find_nodes_with_anom(v)

    for node_name, anom_content in anom_nodes.items():
        print("--------------------------------------------------")
        print(f"\nNode: {node_name}")
        anomalies = anom_content['par']['anomalies']

        ANOMALIES = []
        for anom_id in anomalies:
            # Usa un valore intero derivato dal tempo
            SEED = int(time.time() * 1000000) % (2**32)

            current_anomaly = anomalies[anom_id]
            print(current_anomaly)
            key_current_anomaly = list(current_anomaly.keys())[0]
            perturbation = current_anomaly[key_current_anomaly]

            key_perturbation = list(perturbation.keys())[0]
            input_params = list(perturbation.values())[0]
            output_params = cfg.adapt_config_from_ARS_TOOL(key_perturbation, input_params)
            print(output_params)
            print('SEED: ' + str(SEED))

            anomaly_to_create = cfg.create_anomaly(key_current_anomaly, SEED, output_params)

            ANOMALIES.append(anomaly_to_create)

        positive_constraint = True
        negative_constraint = False
        max_threshold = False
        min_threshold = False

        if (anom_content['par'].__contains__('Hourly_Degradation')):
            APPLY_AGING = True
        else:
            APPLY_AGING = False

        if (APPLY_AGING):
            input_hourly_degradation = anom_content['par']['Hourly_Degradation']['rate']
            # Riporto l'hourly degradation al valore orario
            HOURLY_DEGRADATION = input_hourly_degradation / (365 * 24)
            # Aging fisiologico
            x_aging, b_aging = ut.modulate_signal(N, 0, -1, type = '-x+1', alpha=HOURLY_DEGRADATION)
            print('Hourly Degradation - yearly rate: ' + str(input_hourly_degradation) + '; hourly: ' + str(HOURLY_DEGRADATION))
        else:
            x_aging = np.ones((N,))
            b_aging = np.zeros((N,))

        an_vct = np.zeros((N,))
        dict_anomalies = {}
        #Se l'anomalia successiva si sovrappone alla precedente non deve essere inserita
        i_key = 1
        for key in ANOMALIES:
            descr = key['description']
            seed = key['seed']
            anom = key['anomaly']
            type_anomaly = key['anomaly'].type_anomaly

            N_min = 0
            N_max = N
            an_vct, dict_anomaly = an.generate_anomaly_positions(anom, descr, str(i_key), N, N_min, N_max, an_vct, seed)
            dict_anomalies[str(i_key)] = dict_anomaly
            i_key += 1

        # TODO - Inserire il constraint sulle stagioni. Alcuni tipi di anomalie non possono verificarsi
        # in certe stagioni - o constraint sulle condizioni ambientali --> devo avere un profilo meteorologico (temperatura, umidità)

        if(positive_constraint & negative_constraint):
            print ('WARNING - Verify the imposed constraints')

        x_tot = x_aging
        b_tot = b_aging
        i=0
        for key in ANOMALIES:
            print ('[' + str(i) + ']')
            anom = key['anomaly']
            x_tot, b_tot = an.generate_anomalies(anom, key, an_vct, N, x_tot, b_tot)
            i+=1

        if (PLOT_FIGURE):
            fig = plt.figure(figsize=(20,3))
            plt.subplot(3,1,1)
            plt.stem(x_tot)
            plt.title(node_name + ' xi')
            plt.subplot(3,1,2)
            plt.title('beta')
            plt.stem(b_tot)
            plt.subplot(3,1,3)
            plt.stem(an_vct)
            plt.title('Vettore delle anomalie')
            plt.show()

        anomalies_txt = {}
        if (APPLY_AGING):
            anomalies_txt['hourly_degradation'] = 'Modulation - Type: -x+1, alpha=' + str(HOURLY_DEGRADATION)

        # Post processing
        if (positive_constraint):
            # I valori possono essere solo positivi
            x_tot[x_tot<0]=0

        if (negative_constraint):
            # I valori possono essere solo negativi
            x_tot[x_tot>0]=0

        if (max_threshold):
            # I valori non possono superare un certo valore
            max_value = 1
            x_tot[x_tot>max_value]=max_value

        if (min_threshold):
            # I valori non possono essere inferiori ad un certo valore
            min_value = 0
            x_tot[x_tot<min_value]=min_value

        # Create vectors
        an_vct_using_string = []
        for i in range (0, len(an_vct)):
            if (an_vct[i] == 0):
                an_vct_using_string.append('normal')
            else:
                an_vct_using_string.append('anomaly'+str(int(an_vct[i])))

        xi_tot_string = []
        for i in range (0, len(x_tot)):
            xi_tot_string.append(float(x_tot[i]))

        b_tot_string = []
        for i in range (0, len(b_tot)):
            b_tot_string.append(float(b_tot[i]))

        dict_anomalies_to_save = dict_anomalies.copy()
        for key in dict_anomalies.keys():
            dict_anomalies_to_save['anomaly' + str(key)] = dict_anomalies[key]
            del dict_anomalies_to_save[key]

        result = {'a_vct': an_vct_using_string,
                'xi' : xi_tot_string,
                'beta' : b_tot_string,
                'a_dict': dict_anomalies_to_save}

        #yaml_config_new[KEY_STR]['anomaly']=result
        #yaml_config_new[KEY_STR]['anomaly']['anomalies']=anomalies_txt

        # v[node_name]['anom'] = {'res': result}
        v[node_name]['anom']['res'] = copy.deepcopy(result)

        # FILE_NAME_CREATED = FILE_NAME + '_with_anomalies'
        # with open(DATA_DIR + FILE_NAME_CREATED + '.yml', 'w') as file:
        #     output = yaml.dump(v_new, file) #, default_flow_styl=False)
        #     if (output == None):
        #         print ('Dictionary Updated')
        #     else:
        #         print ('Error in updating Dictionary')
        #

    return anom_nodes



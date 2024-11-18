# import Functionalities.Anomalies.utils_using_xi as ut
import Functionalities.Anomalies.anomaly_using_xi as an
import copy

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

def adapt_config_from_ARS_TOOL(key_perturbation, input_params):
    output_params = {}

    if (key_perturbation.__contains__(' ')):
        splitted_key_perturbation = key_perturbation.split(' ')
        type_of_perturbation = splitted_key_perturbation[1]
        subtype_of_perturbation = splitted_key_perturbation[0]
    else:
        type_of_perturbation = key_perturbation

    output_params['type'] = type_of_perturbation
    # Riporto gli eventi/anno in eventi/ora
    output_params['lambda_a'] = input_params['lambda_a'] / (365 * 24)
    output_params['lambda_duration'] = input_params['lambda_duration']
    output_params['is_fixed'] = input_params['is_fixed']
    output_params['internal_params'] = {}
    
    if (type_of_perturbation == 'scale'):
        output_params['internal_params']['value'] = input_params['value']
    elif (type_of_perturbation == 'decrease'):
        output_params['internal_params']['type'] = subtype_of_perturbation
        if (subtype_of_perturbation == '-x+1'):
            # Riporto il decrease da percentuale di decrease in 1 anno nel decrease orario
            output_params['internal_params']['alpha'] = input_params['alpha'] / (365 * 24)
        else:
            # Quando uso il tipo di decrease 1-exp: alpha = -log(1-b)*t dove b è la percentuale di decrescita
            # e t sono il numero di ore necessarie per osservare quella decrescita indicata
            output_params['internal_params']['alpha'] = input_params['alpha']
    else:
        return -1

    return output_params

def find_nodes_with_anom(yaml_data):
    nodes_with_anom = {}
    
    for node_name, node_content in yaml_data.items():
        if isinstance(node_content, dict) and 'anom' in node_content:
            nodes_with_anom[node_name] = node_content['anom']
            
    return nodes_with_anom
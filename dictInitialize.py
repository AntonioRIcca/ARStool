import yaml

from variables import *


attr_dict = yaml.safe_load(open(mainpath + "/_util/attributes_template.yml"))


def dict_initialize(el, cat):
    v[el] = dict()
    for sub in ['top', 'par', 'lf', 'rel']:
        v[el][sub] = dict()
    v[el]['category'] = cat  # la nomenclatira esatta della categoria deriva dal dizonario "variables.c"
    v[el]['top']['conn'] = []

    if cat in mc['Load'] + mc['Generator']:
        profile_initialize(el)

    lf_initialize(el)
    rel_initialize(el)
    if cat in ['AC-PV', 'DC-PV', 'AC-Wind', 'DC-Wind', 'AC-BESS', 'DC-BESS', ]:
        anom_initialize(el)
    onr_initialize(el)


# Inizializzazione del sottodizionario del profilo dei parametri ("Par") per l'elemento "el"
def profile_initialize(el):
    v[el]['par']['profile'] = {
        'curve': 1,
        'name': None,
    }


# Inizializzazione del sottodizionario rella Reliability ("rel") per l'elemento "el"
def rel_initialize(el):
    v[el]['rel']['par'] = dict()
    for p in ['t_preg', 'Pi_E', 'Pi_Q', 'alfa', 'beta']:
        #v[el]['rel']['par'][p] = None
        v[el]['rel']['par'][p] = attr_dict[v[el]['category']]['reliability'][p]

    v[el]['rel']['results'] = dict()
    if v[el]['category'] in mc['Load']:
        v[el]['rel']['results']['load_rel'] = None
    for p in ['lambda', 'MTBF_ore', 'MTBF_anni', 'Pi_Si']:
        v[el]['rel']['results'][p] = None

def anom_initialize(el):
    v[el]['anom'] = {'par': {'anomalies': {}}, 'res': {}}

# Inizializzazione del sottodizionario del loadFLow ("lf") per l'elemento "el"
def lf_initialize(el):
    params = ['i', 'v', 'p', 'q']

    if v[el]['category'] in mc['Transformer'] + mc['Line']:
        for p in params:
            v[el]['lf'][p] = dict()
            v[el]['lf'][p][0] = []
            v[el]['lf'][p][1] = []
    else:
        for p in params:
            v[el]['lf'][p] = []

def onr_initialize(el):
    v[el]['ONR'] = {
        'lf_pre': {},
        'lf_post': {},
        'par': {'zone': None},
        # 'info_switch': None,
    }

    if v[el]['category'] in mc['Load']:
        v[el]['ONR']['par']['numcust'] = 1
    # elif v[el]['category'] in mc['Generator'] + mc['Vsource']:
    #     v[el]['ONR']['par']['numcust'] = 1
    #     v[el]['ONR']['par']['lambda'] = 0.1
    #     v[el]['ONR']['par']['mu'] = 3
    else:
        v[el]['ONR']['par']['lambda'] = 0.1
        v[el]['ONR']['par']['mu'] = 3

    for sd in ['lf_pre', 'lf_post']:
        for p in ['i', 'v', 'p', 'q']:
            if v[el]['category'] in mc['Line'] + mc['Transformer']:
                v[el]['ONR'][sd][p] = {
                    0: 0,
                    1: 0,
                }
            else:
                v[el]['ONR'][sd][p] = 0

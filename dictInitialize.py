from variables import *


def dict_initialize(el, cat):
    v[el] = dict()
    for sub in ['top', 'par', 'lf', 'rel']:
        v[el][sub] = dict()
    v[el]['category'] = c[cat]  # la nomenclatira esatta della categoria deriva dal dizonario "variables.c"
    v[el]['top']['conn'] = []

    lf_initialize(el)
    rel_initialize(el)


# Inizializzazione del sottodizionario rella Reliability ("rel") per l'elemento "el"
def rel_initialize(el):
    v[el]['rel']['par'] = dict()
    for p in ['Pi_E', 'Pi_Q', 'alfa', 'beta']:
        v[el]['rel']['par'][p] = None

    v[el]['rel']['results'] = dict()
    if v[el]['category'] in mc['Load']:
        v[el]['rel']['results']['load_rel'] = None
    for p in ['lambda', 'MTBF_ore', 'MTBF_anni', 'Pi_Si']:
        v[el]['rel']['results'][p] = None


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
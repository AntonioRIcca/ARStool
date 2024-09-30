import datetime
from variables import *

timesteps = {
    15: {'jump': 1, 'unit': 'h', 'scale': 4},
    30: {'jump': 2, 'unit': 'h', 'scale': 2},
    60: {'jump': 4, 'unit': 'h', 'scale': 1},
    180: {'jump': 12, 'unit': 'day', 'scale': 8},
    360: {'jump': 24, 'unit': 'day', 'scale': 4},
    1440: {'jump': 96, 'unit': 'day', 'scale': 1},
}


def defaultProfileImport(elem, prof_name):
    mcat = ''
    prof_cat = ''
    for cp in ['load', 'gen']:
        for p in bench['profiles'][cp]:
            if prof_name == bench['profiles'][cp][p]:
                mcat = cp
                prof_cat = p
                break

    file = open(mainpath + '/_benchmark/_data/_profiles/' + mcat + '_year.txt')
    head = file.readline().removesuffix('\n').split('\t')

    data = {
        'year': [],
        'month': [],
        'weekday': [],
        'day': [],
    }

    col = head.index(prof_cat) - 1
    for line in file.readlines():
        data['year'].append(float(line.split('\t')[col + 1]))

    for p in ['month', 'weekday', 'day']:
        file = open(mainpath + '/_benchmark/_data/_profiles/' + mcat + '_' + p + '.txt')
        line = file.readline()
        for line in file.readlines():
            data[p].append(float(line.split('\t')[col]))

    # m, i = 0, 0
    # m = 0
    # file = open(mainpath + '/_benchmark/_data/_profiles/' + mcat + '_day.txt')
    # line = file.readline()
    # for line in file.readlines():
    #     m += float(line.split('\t')[col])
    #     i += 1
    #     if i == self.timesteps[grid['profile']['step']]['jump']:
    #         data['day'].append(m / self.timesteps[grid['profile']['step']]['jump'])
    #         m, i = 0, 0

    datastart = datetime.datetime(grid['profile']['start'][0], grid['profile']['start'][1],
                                  grid['profile']['start'][2], grid['profile']['start'][3],
                                  grid['profile']['start'][4])
    dataend = datetime.datetime(grid['profile']['end'][0], grid['profile']['end'][1],
                                grid['profile']['end'][2], grid['profile']['end'][3],
                                grid['profile']['end'][4])

    t = datastart

    prof = []
    m, i, j = 0, 0, 0
    while t <= dataend:
        m += (data['year'][t.year - 2010] * data['month'][t.month - 1] * data['weekday'][t.weekday()]
              * data['day'][int(t.hour * 4 + t.minute / 15)])
        t = t + datetime.timedelta(minutes=15)
        i += 1
        if i == timesteps[grid['profile']['step']]['jump']:
            prof.append(m / timesteps[grid['profile']['step']]['jump'])
            m, i = 0, 0
    if i != 0:
        prof.append(m / i)

    # print('righe', self.ui.profileTW.rowCount())
    # if self.ui.profileTW.rowCount() > 0:
    #     print('agg')
    #     self.plot_profile()
    #     self.table_fill()
    #     self.cat = None

    name = elem + '_' + prof_cat
    return name, prof

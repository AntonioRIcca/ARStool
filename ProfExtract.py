import datetime

# file = open('./_benchmark/_data/_profiles/GenProfiles.txt')
# lines = file.readlines()
#
# myline = lines[0]
# for myline in lines:
#     params = myline.split('[')[0]
#     name = params.split(' ')[1].split('.')[1]
#     elem = myline.split('[')[1].split(']')[0].split(' ')
#
#     datas = []
#     for e in elem:
#         if e not in ['', ' ']:
#             datas.append(float(e))
#
#     # print(params)
#     # print(name)
#     # print(datas)
#     # print(len(datas))
#     # print('\n')
#     print(name, datas[120*24:120*24+23], max(datas))
#
#     mm = []
#     for i in range(365):
#         mm.append(max(datas[24*i:24*i+23]))
#     print(name, mm)
#
#
# t = 0
# m = 0
# for i in range(len(datas)):
#     if datas[i] > m:
#         m = datas[i]
#         t = i
#
# print(t/24, m)


d = datetime.datetime.today()
nd = d + datetime.timedelta(-2)

genProf = dict()
file = open('./_benchmark/_data/_profiles/Gen_year.txt')

head = file.readline().removesuffix('\n').split('\t')
file.close()
for h in head:
    genProf[h] = {
        'year': [],
        'month': [],
        'weekday': [],
        'day': [],
    }

for p in ['year', 'month', 'weekday', 'day']:
    file = open('./_benchmark/_data/_profiles/Gen_' + p + '.txt')
    head = file.readline().removesuffix('\n').split('\t')

    for l in file.readlines():
        r = l.split('\t')
        for i in range(len(head)):
            genProf[head[i]][p].append(float(r[i]))

daystart = datetime.datetime(2024, 1, 1, 0, 0)
# dayend = datetime.datetime(2024, 1, 30, 23, 45)
dayend = datetime.datetime(2024, 12, 31, 23, 45)

day = daystart
dataset = []

while day <= dayend:
    # print(len(dataset))
    hour = int(day.hour * 4 + day.minute / 15)
    dataset.append(genProf['PV']['year'][int(day.year - genProf['Year']['year'][0])] * genProf['PV']['month'][day.month - 1] *
                   genProf['PV']['weekday'][day.weekday()] * genProf['PV']['day'][hour])
    day = day + datetime.timedelta(minutes=15)

print(dataset)
print(len(dataset))

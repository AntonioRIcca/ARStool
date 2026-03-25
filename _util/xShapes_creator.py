import yaml


filename = 'CityArea.yml'
v = yaml.safe_load(open(filename))

print(v['_grid_']['name'])

del v['_grid_']

f = open('Load_profiles.txt', 'w')
f.write('')

print('\nLoads:')
for el in v.keys():
    if v[el]['category'] in ['AC-Load', 'DC-Load']:
        if v[el]['par']['profile']['name']:
            s = f'New Loadshape.{el}_profile npts=8760 interval=1.000000 mult=['
            for val in v[el]['par']['profile']['curve']:
                s += f'{val}     '
            s = s[:-5] + ']\n\n'
            print(s)
            f.write(s)

f.close()


f = open('Gen_profiles.txt', 'w')
f.write('')

print('\nGENERATORS:')
for el in v.keys():
    if v[el]['category'] in ['AC-BESS', 'DC-BESS', 'AC-Wind', 'DC-Wind', ', AC-PV', 'DC-PV', ]:
        if v[el]['par']['profile']['name']:
            s = f'New Loadshape.{el}_profile npts=8760 interval=1.000000 mult=['
            for val in v[el]['par']['profile']['curve']:
                s += f'{val}     '
            s = s[:-5] + ']\n\n'
            print(s)
            f.write(s)
f.close()


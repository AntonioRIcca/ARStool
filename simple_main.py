from variables import c, vdss, v, mc
import yaml
import opendss

import csv

dss = opendss.OpenDSS()

# -- Apertida del file DSS --------------------------------------------------------
filename = 'C:/Users/anton/PycharmProjects/ARStool/CityArea.dss'
dss.open(filename)
# ---------------------------------------------------------------------------------

# -- Risoluzione puntuale ---------------------------------------------------------
# t = 1       # tempo (0-23.75) a cui calcolare il loadflow
t = None    # inserire None se si vogliono ognorare i profili
dss.write_all(t)
dss.solve()
# ---------------------------------------------------------------------------------

# # -- Risoluzione dei profili ------------------------------------------------------
# dss.solve_profile()
#
# # ---- scruttura del file CSV per i profili --------------
# categories = mc['Vsource'] + mc['Load'] + mc['Generator']
#
# with open('CityArea.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file, delimiter=';')
#     mylist = []
#     for elem in v:
#         if v[elem]['category'] in categories:
#             mylist.append(elem)
#     writer.writerow(mylist)
#
#     for i in range(96):
#         line = []
#         for elem in mylist:
#             line.append(v[elem]['lf']['p'][i])
#         writer.writerow(line)
# # --------------------------------------------------------
# # -----------------------------------------------------------------------------------


# -- Salvataggio della libreria -----------------------------------------------------
with open('CityArea.yml', 'w') as file:
    yaml.dump(v, file)
    file.close()
# -----------------------------------------------------------------------------------

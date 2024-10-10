
import pandas as pd
import numpy as np
import polars as pl
import numpy as np
import csv
import random

a = ['i', 'p', 'q', 'v']
# with open('_temp/test.csv', 'w', newline='') as csv_file:
#     csv_writer = csv.writer(csv_file, delimiter='\t')
#     csv_writer.writerow(a)
#     # csv_file.close()


csv_file1 = open('_temp/test1.csv', 'a', newline='')
csv_file2 = open('_temp/test2.csv', 'a', newline='')
csv_writer1 = csv.writer(csv_file1, delimiter='\t')
csv_writer2 = csv.writer(csv_file2, delimiter='\t')
csv_writer1.writerow(a)
csv_writer2.writerow(a)

#     csv_writer.writerow(a)
# with open('_temp/test.csv', 'a', newline='') as csv_file:
# csv_writer = csv.writer(csv_file, delimiter='\t')
for row in range(10):
    b = []
    for i in range(4):
        b.append(random.randint(0, 99))
    print(row)
    csv_writer1.writerow(b)

    b = []
    for i in range(4):
        b.append(random.randint(0, 99))
    print(row)
    csv_writer2.writerow(b)
csv_file1.close()
csv_file2.close()

# # np_dates = np.zeros((5, 10))
# np_dates = np.array([[1, 2, 3, 4],
#                     [5, 6, 7, 8],
#                     [9, 10, 11, 12]])
# np_dates[2, 1] = 100
#
# print(np_dates)
# print(np_dates[1, 3])
# #
# #
#
# dates = pd.DataFrame(np.random.rand(15000, 4), index=list(range(15000)), columns=list('ipqv'))
# df = pl.DataFrame({
#     'i': list(float(0) for i in range(1500)),
#     'p': list(float(0) for i in range(1500)),
#     'q': list(None for i in range(1500)),
#     'v': list(None for i in range(1500)),
# })
#
# df[23, 'i'] = 12.258
# # df[3, 'p'] = 12.258
#
# path = '_temp/elements/file.csv'
#
# df.write_csv(path, separator='\t')
#
#
# print(df)
#
# aaa = pl.read_csv(path, separator='\t')
# aaa[0, 'p'] = 9999
# print(aaa)
#
# # dates.loc[2, 'q'] = 100
# #
# # print(dates)
# #
# # dates.to_csv('test_pandas.csv', sep='\t')


import pandas as pd
import numpy as np
import polars as pl


dates = pd.DataFrame(np.random.rand(15000, 4), index=list(range(15000)), columns=list('ipqv'))
df = pl.DataFrame({
    'i': list(float(0) for i in range(1500)),
    'p': list(float(0) for i in range(1500)),
    'q': list(None for i in range(1500)),
    'v': list(None for i in range(1500)),
})

df[23, 'i'] = 12.258
# df[3, 'p'] = 12.258

path = '_temp/elements/file.csv'

df.write_csv(path, separator='\t')


print(df)

aaa = pl.read_csv(path, separator='\t')
aaa[0, 'p'] = 9999
print(aaa)

# dates.loc[2, 'q'] = 100
#
# print(dates)
#
# dates.to_csv('test_pandas.csv', sep='\t')

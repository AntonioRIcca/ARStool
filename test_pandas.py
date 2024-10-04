
import pandas as pd
import numpy as np


dates = pd.DataFrame(np.random.rand(15000, 4), index=list(range(15000)), columns=list('ipqv'))

dates.loc[2, 'q'] = 100

print(dates)

dates.to_csv('test_pandas.csv', sep='\t')

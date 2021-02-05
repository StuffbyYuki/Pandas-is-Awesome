'''
You can create your own dataframe
'''
import pandas as pd
import numpy as np

a = np.random.rand(3,3)  # generate random numbers 3 by 3
df = pd.DataFrame(a, columns=['a', 'b', 'c'])  # create df
print(df.head())

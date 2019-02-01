import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randan(6,4), columns = ['one' , 'two', 'three', 'four'] , index = list('abcdef'))
print df
print df.ix[[1,2,4]]
print df.reindex([1,2,4])


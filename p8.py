import numpy as np
sequence = np.arange(10,26,4)
print("sequence:",sequence)
indexof_18=np.where(sequence==18)[0][0]
print("index of 18",indexof_18)
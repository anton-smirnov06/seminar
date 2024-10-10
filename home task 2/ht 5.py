import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv('BTC_data.csv')
q=[]
for i in range(0,1457):
    q.append(df['time'][i][:10])
plt.plot(q,df['close'])
plt.xticks(np.arange(0,1458,1))
plt.show()

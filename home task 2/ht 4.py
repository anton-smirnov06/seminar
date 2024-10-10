import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('iris_data.csv')
plt.plot(df['SepalLengthCm'],df['SepalWidthCm'])
plt.show()
df = pd.read_csv('iris_data.csv')
plt.plot(df['SepalLengthCm'],df['PetalLengthCm'])
plt.show()
df = pd.read_csv('iris_data.csv')
plt.plot(df['SepalLengthCm'],df['PetalWidthCm'])
plt.show()
df = pd.read_csv('iris_data.csv')
plt.plot(df['PetalLengthCm'],df['PetalWidthCm'])
plt.show()
df = pd.read_csv('iris_data.csv')
plt.plot(df['PetalLengthCm'],df['SepalWidthCm'])
plt.show()
df = pd.read_csv('iris_data.csv')
plt.plot(df['PetalLengthCm'],df['SepalLengthCm'])
plt.show()



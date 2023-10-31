


import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd

#Reading data from a CSV file

df=pd.read_csv("COVID19.csv")
#print(df)

#converting a column into a list
N1 = df['NewCasesN'].values.tolist()   #list with null values
print(N1)

#Eliminating nulls and converting the float values into int
N=df['NewCasesN'].dropna().astype(int).tolist()
print(N)

R=df['RecoveredR'].dropna().astype(int).tolist()
print(R)

D=df['DeathsD'].dropna().astype(int).tolist()
print(D)

#Extracting Days
df1=df.loc[8:33,['Day']]
#print(df1)
Days = df1['Day'].values.tolist()
print(Days)

plt.plot(Days, N, 'b', label='New Cases', linewidth=5)
plt.plot(Days, R, 'g', label='Recovered', linewidth=4)
plt.plot(Days, D, 'r', label='Deaths',    linewidth=2)

plt.title("Corona Virus Realtime Updates")
plt.xlabel("Day Wise")
plt.ylabel("Cases Count")

plt.legend()
plt.grid(True, color='0')
plt.show()









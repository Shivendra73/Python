
#Converting df to csv,excel and json

import pandas as pd

df = pd.read_csv('C:data\emp1.csv')

print(df)

df.to_csv('emp1.csv')

df.to_excel('emp4.xlsx')

df.to_json('emp2.json')

#installing cx_Oracle module:
'''
C:\Python39\Scripts>pip install cx_Oracle
Collecting cx_Oracle
  Downloading cx_Oracle-8.1.0-cp39-cp39-win_amd64.whl (207 kB)
     |████████████████████████████████| 207 kB 1.3 MB/s
Installing collected packages: cx-Oracle
Successfully installed cx-Oracle-8.1.0 '''

import cx_Oracle

con=cx_Oracle.connect("scott","tiger",'localhost')

cur1=con.cursor()

cur1.execute("select * from dept")

for p in cur1:
    print(p)



f=open("emp.txt","r+")  #r+ mode wont remove the previous data

print(f.read())
f.write(" Manager Hyderabad ")
f.seek(0)
print(f.read())

f.close()

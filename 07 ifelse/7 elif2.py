#Accepting marks of 5 Subjects and compute the total and percentage and also compute the
#the class or Grade awarded

s1=90 ; s2=80; s3=70; s4=60; s5=50

tot=s1+s2+s3+s4+s5
per=(tot/500)*100

print("TOTAL=",tot)
print("PERCENTAGE=",per)

if(per>=70):
    print("FIRST CLASS WITH DISTINCTION")
elif(per>=60):
    print("FIRST CLASS")
elif(per>=50):
    print("SECOND CLASS")
elif(per>=40):
    print("THIRD CLASS")
else:
    print("FAIL")



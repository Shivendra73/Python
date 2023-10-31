
#break stmt: If break stmt is used within a loop then ctrl comes out of that loop and
#            stmts after the break are not executed.

x=1
while(True):
    print("hello")
    if(x==5):
        break
        print("hi")
    x=x+1
print("end")
    

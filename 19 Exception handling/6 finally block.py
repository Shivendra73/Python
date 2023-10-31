#finally block:

                                    # I-Iteration     II-Iteration(exception)       III-Iteration
                                     #(no exception) (Exception occured&handled)   (Exception occured
try:                                 #                 (zeroDivisionError)          & not handled)
    x=int(input("Enter First No:"))   #200              100                           100
    y=int(input("Enter Second No:"))  #100              0                             two
    z=x/y
    print(z)

except(ZeroDivisionError):
    print("2nd No cannot be zero") 

print("welcome to Python World!!!......")#o/p :Welcome to   o/p: 2nd No cannot          o/p:Abnormal Termination 
                                   #    Pythonworld!!!.......    be zero
                                                                 #welcome to Python.

#but in all the above 3 situations, I want to display "welcome to Python world!!!......",
#then use finally block
                                   
#finally block:The block of stmts which will executed always,whether exception occured or
#not occured or exception handled or not handled, but these stms will be executed always.

#   I-situation                     II- situation                               III-situation
#    try:                           try:                               try:
#       fileopen--->success           fileopen--->success                  fileopen-->success
#       operations->success           operations-->error                   operations-->error
#so it wont go to except block      ctrl goes to except block&handles  ctrl goes to except block&not handled
# f.close()---->will be executed    f.close()---->will be executed     Abnormal Termination,
#                                                                      f.close()--->is not executed.

#so here in all the 3 situations ,keep f.close()(file closing stmt)in finally block so it executes in
#all 3 situations

#file closing stmts(Resource releasing stmts) and database connection closing stmts are recommended to
#represent by using finally block.
        
                                   
                                   

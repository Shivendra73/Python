
#Nested Blocks:
#In try block--->I can have try,except,finally blocks
#in except block--->I can have try,except,finally blocks
#in finally block--->I can have try,except,finally blocks


try:
    print("in try1...")
    try:
        print("in try2.....")
    except:
        print("in except2...")
    finally:
        print("in finally2...")
except:
    print("in except1...")
    try:
        print("in try3.....")
    except:
        print("in except3...")
    finally:
        print("in finally3...")
finally:
    print("in finally1...")
    try:
        print("in try4.....")
    except:
        print("in except4...")
    finally:
        print("in finally4...")

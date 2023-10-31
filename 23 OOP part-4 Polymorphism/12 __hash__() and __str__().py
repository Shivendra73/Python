ex:
    class A:
        def m1(self):
            print("from m1.....")
    a1=A()



    Here 2 objects are created--->class A object and object class object

    object class object has 2 methods
    1)__hash__(self)
    2)__str__(self)

    object class object __hash_() method ,which returns hash value,
    this hash value is converted into hexadecimal by another method
    called __str__()method
    so python interpreter calls __str__( )method and
    __str__()method calls __hash__()method and takes hashvalue and converts
    into hexadecimal value.


#Modules:

-Every Python program or a file by default is a module.

-A Module consists of
 1)Executable stmts
 2)Global variables
 3)Functions
 4)Classes

 Main module: If we execute any module,by default it is treated as main  module

 we can import the properties of one module into another module using import stmt.
 
 sub-mododule:If a module imported another module then the imported module is called as sub-module


          sample.py                                     Test.py
    .......................                       ......................... Here Test.py is the main module
    .......................                       ......................... and sample.py is the sub module
    .......................-------import------>   ......................... Test.py can access the properties
    .......................                       ......................... of both sample.py and Test.py
    .......................                       .........................
    .......................                       .........................

1) When we execute the main module(sample.py) then the entire code of sample.py will be converted
    into an intermediate code called as byte code(sample.pyc) and later this byte code is converted
    into machine code and is executed, once the execution is completed then the byte code(sample.pyc)
    will be deleted automatically.

2) when we execute the main module(Test.py) then 2 .pyc files will be generated for main module
   and sub-module respectively i.e Test.pyc and sample.pyc.
   If sub-module.pyc(Sample.pyc) is already available, it wont be generated  again untill or unless if
   there is a change in the source code of sub-module(sample.py)
   once the execution is completed then the main-module.pyc(Test.pyc) will be deleted automatically
   where as the sub-module.pyc(sample.pyc) still remains permanently in the disk.

3) if we execute the main module(Test.py) for the 2nd time then only one .pyc file will be
   generated i.e mainmodule.pyc(Test.pyc) but sub-module.pyc(sample.pyc) wont be generated
   as it is already available

4) Before executing the main-module(Test.py) for the 3rd time, if we modify the sub-module(sample.py)
   then 2 .pyc files are generated i.e Test.pyc and sample.pyc

5) if we execute the main module then all the executable stmts of sub-module also will be executed
   automatically

6)while accessing the properties(variable,function,class) of sub-module always we need to use
  sub-module name before the propertyname
  ex: sample.x
      sample.display()
  





    
 

#patterns:

#1. Floyd's triangle
'''
1
22
333
4444
55555
666666
7777777
88888888
999999999 '''

#solution:
for i in range(1,10):      #no of rows
    for j in range(1,i+1): #no of values in each row
        print(i,end="")
    print()




#2.
'''
1
12
123
1234
12345
123456
1234567
12345678
123456789 '''

#solution:
for i in range(1,10):      #no of rows
    for j in range(1,i+1): #no of values in each row
        print(j,end="")
    print()


#3.
'''
*
**
***
****
*****
******
*******
********
********* '''

#solution:
for i in range(1,10):      #no of rows
    for j in range(1,i+1): #no of values in each row
        print("*",end="")
    print()

#4.
'''
A
BB
CCC
DDDD
EEEEE
FFFFFF
GGGGGGG
HHHHHHHH
IIIIIIIII
'''
#solution:
for i in range(1,10):      #no of rows
    for j in range(1,i+1): #no of values in each row
        print(chr(i+64),end="")
    print()

#or
for i in range(65,74):
    for j in range(65,i+1):
        print(chr(i),end="")
    print()

#ASCII
'''
A-65
B-66
C-67
.
.
.
Z-90 '''

#5.
'''
A
AB
ABC
ABCD
ABCDE
ABCDEF
ABCDEFG
ABCDEFGH
ABCDEFGHI'''

#solution:
for i in range(1,10):      #no of rows
    for j in range(1,i+1): #no of values in each row
        print(chr(j+64),end="")
    print()

#6. Pascal triangle
'''
         *
        * *
       * * *
      * * * *
     * * * * *
    * * * * * *
   * * * * * * *
  * * * * * * * *
 * * * * * * * * * '''

#solution

n=40
for i in range(1,11):
    print(' '*n,end="")
    print('* '*i)
    n=n-1

#7.
'''
1
22
333
4444
55555
666666
55555
4444
333
22
1
'''
#8.
'''
1
12
123
1234
12345
123456
12345
1234
123
12
1
'''

#9.
'''
123456789
12345678
1234567
123456
12345
1234
123
12
1
'''

#10.
'''
999999999
88888888
7777777
666666
55555
4444
333
22
1
'''

#11.
'''
987654321
98765432
9876543
987654
98765
9876
987
98
9
'''

#12.
''''
AAAAAAAAA
BBBBBBBB
CCCCCCC
DDDDDD
EEEEE
FFFF
GGG
HH
I
'''

#13.
'''
ABCDEFGHI
ABCDEFGH
ABCDEFG
ABCDEF
ABCDE
ABCD
ABC
AB
A
'''

#14.
'''
55555
 4444
  333
   22
    1
'''
#15.
'''
12345
 1234
  123
   12
    1
'''
#16.
'''
ABCDE
 ABCD
  ABC
   AB
    A
'''
#17.
'''
555555555 -9TIMES
 4444444  -7TIMES
  33333   -5TIMES
   222    -3TIMES
    1
'''

#18.
'''
999999999
 7777777
  55555
   333
    1
'''
#19.
'''123456789
    1234567
     12345
      123
       1
'''














    





























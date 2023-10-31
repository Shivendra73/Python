
#Bitwise Operators:
#bitwise operators are used to perform operations on bits.
#The integers are first converted into binary and then operations are performed on
#bit by bit, hence the name bitwise operators.
#Then the result is again returned in decimal format.

#Bitwise opertors works only on integers.

OPERATOR	DESCRIPTION	        SYNTAX
&	        Bitwise AND	        x & y
|	        Bitwise OR	        x | y
^	        Bitwise XOR	        x ^ y
<<	        Bitwise left shift	x<<
>>	        Bitwise right shift	x>>


1 byte =8bits =========>0000 0000
#-----------------------------------------------------------------------------------------------------
#Converting a decimal number to Binary

x=7 ------->decimal---->its Binary Equivalent is------>0111
x=10 ---------------------------->1010
x=17 ---------------------------->10001

#Converting a Binary to decimal
Binary           decimal
1101 -----------> 13 =>1*pow(2,0)+0*pow(2,1)+1*pow(2,2)+1*pow(2,3)
                          1      +    0     +   4      +  8    =13
0011 ----------->  3
101010----------> 42

----------------------------------------------------------------------------------------------------
'''
       a      b       a&b     a|b    a^b
       1      1        1       1      0
       1      0        0       1      1
       0      1        0       1      1
       0      0        0       0      0

'''

#------------------------------------------------------------------------------------------------------
#1)Bitwise and(&): Returns 1 if both bits are 1 else it returns 0
#ex:
a=10
b=7
find(a&b)
a = 10 = 1010 (Binary)
b = 7 =  0111 (Binary

    a = 1 0 1 0
           &           
    b = 0 1 1 1
a & b = 0 0 1 0
      = 2 (Decimal)
#----------------------------------------------------------------------------------------------------
#2)Bitwise or : Returns 1----->if any one of the bit is 1  or both the bits are 1 else returns 0.

#Ex:

a = 10 = 1010 (Binary)
b = 7 =  0111 (Binary

    a = 1 0 1 0
           |
    b = 0 1 1 1
a | b = 1 1 1 1
      = 15(Decimal)
#------------------------------------------------------------------------------------------------------
#Bitwise xor operator: Returns 1 if one of the bit is 1 and other is 0 else returns false.
                       # It returns 0 if both the bits are 1 or if both the bits are 0 


Example:

a = 10 = 1010 (Binary)
b =  7 = 0111 (Binary

a ^ b = 1 0 1 0
           ^
        0 1 1 1
      = 1 1 0 1
      = 13 (Decimal)


#----------------------------------------------------------------------------------------------------         
#-----------------------------------------------------------------------------------------------------
#5)Bitwise left shift: Shifts the bits of the number to the left and fills 0 on right
#ex:
a = 10 = 0000 1010 (Binary)
a<<2 ----> removes 2bits from the left side and adds 2 0's at the right side
a<<2 ---->0010 1000 =40

#------------------------------------------------------------------------------------------------------
#6)Bitwise right shift: Shifts the bits of the number to the right and fills 0 on left
#ex:
a = 10 = 0000 1010 (Binary)
a>>2 ----> removes 2bits from the right side and adds 2 0's at the left side
a>>2 ---->0000 0010 =2
#-----------------------------------------------------------------------------------------------------



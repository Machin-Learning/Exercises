# 1. AND(&) Bitwise operators
# biwtwise operator sets each bit to 1 if both bits are 1.
# 10 = 1010n
# 11 = 1011b
print(10&11) #1&1=1,0&0=0,0&1=0 so output is 1010=10


# 2. Bitwise Or(|) operator
# biwtwise operator sets each bit to 1 if one of two bits are 1.
# 10 = 1010
# 12 = 1100
# 1 | 1 =1,1|0=1,0|0 =0
print(10 | 12) #1110 = 14

# 3. XOR(^) operator
# sets each bit to 1 if only one of two bits is 1
print(12^2) #1100^0010=1110=14

# 4. NOT(~) operator
# inverts all the bits
print(~11) #~1011 
print(~10) #~1010 

# 5. Left Shift (<<) operator
# move the left oprand's values to the left by the number of bits specified by the right oprand!

print(12<<2) #12=1100,2=0010 and 1100<<0010 = 110000

# 5. Right Shift (>>) operator
# move the left oprand's values to the right by the number of bits specified by the right oprand!
print(12>>3)

print(10 and 7)
print(10 & 7)
                                        #         #Set
                                # 1. Set in python is immuttable/non changeable and does not show duplicate
                                # 2. Set are collection of element  seprated by comma inside {,}
                                # 3. Set can't be indexed or slice
                                # 4. Set can't add/concat or scale/multiply
                                # 5. we can use set to store multiple items in one variable
                                # 6. set are itrator




s = {1,2,3,4}
print(s)

#set are immuttable
# s[0]= 5 #TypeError: 'set' object does not support item assignment
# print(s)

#TypeError: 'set' object is not subscriptable
#Indexing :left to right [0][1][2][3][.][n]
#          right to left [-1][-2][-3][-.][-n]

# print(s[0]) #TypeError: 'set' object is not subscriptable


# print(s[0:3])

s1 = {1,2,5,6}

# Operation on set

# print(s+s1) #TypeError: unsupported operand type(s) for +: 'set' and 'set'

# print(s*s1) #TypeError: unsupported operand type(s) for *: 'set' and 'set'

print(s.intersection(s1)) #--->{1, 2}

print(s.difference(s1)) #--->{3, 4}

print(s1.difference(s)) #--->{5, 6}

print(s.union(s1)) #--->{1, 2, 3, 4, 5, 6}

print(s.pop()) 
print(s)
print(s.pop())
print(s)
print(s.pop())
print(s)

print(s1)
print(s1.remove(5))
print(s1)
print()
print(s1.discard(2))
print(s1)
print()
print(s1.symmetric_difference(s))


s2 = {1,2,1,5,4,4,6,8,7,8}

print(s2)
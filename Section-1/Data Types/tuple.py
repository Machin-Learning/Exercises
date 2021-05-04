                                        #         #Tuple
                                # 1. Tuple in python is immuttable/non changeable
                                # 2. Tuple are collection of element (unOrder and unindex) seprated by comma inside () or without ()
                                # 3. Tuple can be indexed or slice
                                # 4. Tuple can add/concat or scale/multiply
                                # 5. we can use Tuple to store multiple items in single variable
                                # 6. we can get the size of List using sys.getsizeof(tu) in bytes
                                # 7. List are itrator


tu = (1,2,3,4,5,6,6,7,1,6) #tuple ()
tu_unb = 1,2,3,4,5,6,7,8

tu_mixed = (1,-2,"Masum",3.14,-3.14,"a")
tu_nested = ((1,2,3),(4,5,6),(7,8,9))
tu_list = ([1,2,3],[4,5,6],[7,8,9])

print(tu,tu_unb,tu_mixed,tu_nested,tu_list)

#Tuple are immuttable
# tu[0]= 5 TypeError: 'tuple' object does not support item assignment

#Indexing :left to right [0][1][2][3][.][n]
#          right to left [-1][-2][-3][-.][-n]


print(tu_mixed[0])
print(tu[-1])
print(tu_nested[0])
print(tu_nested[0][0])
print(tu_list[0])
print(tu_list[0][0])

#Slicing on tuple: [start,stop+1,step]

print(tu[0:5])

print(tu_list[0:1])

print(tu_mixed[0:5])

print(tu[::-1])

print(tu[::2])

# operation on tuple
print()
print(tu.count(6))

print(tu.index(1))


print()
print(tu+tu_mixed)


print(tu*2)


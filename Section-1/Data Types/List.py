                                        #         #List
                                # 1. List in python is muttable/changeable
                                # 2. List are collection of element  seprated by comma inside []
                                # 3. List can be indexed or slice
                                # 4. List can add/concat or scale/multiply
                                # 5. we can use List to store multiple items in single variable
                                # 6. we can get the size of List using sys.getsizeof(ls) in bytes
                                # 7. List are itrator

ls_num = [1,2,3,4,5,6,7]

ls_nnum = [-1,-2,-3,-4,-5,-6,-7]

ls_str = ["Muzmmil","Mudassir","Masum"]

ls_char = ["a","b","c","d","e"]

ls_flo = [1.25,3.14,8.45,12.5]

ls_nflo = [-1.25,-3.14,-8.45,-12.5]

ls_mixed = [1,-2,"Masum","d",8.45,-12.5]

ls_nested = [[1,2,3],[4,5,6],[7,8,9]]

ls_tuple = [(1,2,3),(4,5,6),(7,8,9)]

print(ls_num,ls_nnum,ls_str,ls_char,ls_flo,ls_nflo,ls_mixed,ls_nested,ls_tuple)

# List in python support item assignment
print("List in python is mutable/changeable")
ls_str[0] = "Muzammil khan"
print(ls_str)

#Indexing on list
#Indexing :left to right [0][1][2][3][.][n]
#          right to left [-1][-2][-3][-.][-n]
print()
print(ls_num[0])
print(ls_num[-1])
print(ls_nested[0])
print(ls_nested[0][0])

# Sliceing on list: [start,stop+1,step]

print(ls_num[0:5])

print(ls_nnum[0:])

print(ls_char[0][0:3])

print(ls_num[0::-1])

print(ls_num[::2])


#operation on list
print()
ls = []

print(ls.append(0))
print(ls.append(1))
print(ls.append(2))

print()

print(ls.extend(ls_num[2:]))

print()
print(ls.pop())
print(ls.pop(0))

print()
print(ls.reverse())

print()
print(ls.count(1))

print()
print(ls.insert(0, -1))

print()
print(ls.index(5))

print()
print(ls)
ls_copy = ls.copy()
print(ls_copy)

print()
print(ls.sort())
print(ls)

print()
print(ls.clear())
print(ls)

print()
print(ls_flo+ls_char)

print()
print(ls_flo*2)


#Type Casting

#suppose we have string "55" and want to cast/convert it into integer 55
x = "55"
print(x)
print(type(x))
print()


y = int(x)
print(y)
print(type(y))
print(float(x))
print()

# Similarly its apply to all posible casting in python 

z = "3.14"
print(float(z))
# print(int(z)) # Error: ValueError: invalid literal for int() with base 10: '3.14'

sl = "123456"
print(tuple(sl))
print(list(sl))
print(set(sl))
# print(dict(sl)) Error:ValueError: dictionary update sequence element #0 has length 1; 2 is required
print()

l = 123456
# print(tuple(l)) TypeError: 'int' object is not iterable
# print(list(l))
# print(set(l))

#to make a spaced tab comma seprated string to list we use split

nums1 = "1,2,3,4,5,6,7"
nums2 = "1 2 3 4 5 6 7"
nums3 = "1   2   3   4   5   6   7"

print(nums1.split(","))
print(nums2.split(" "))
print(nums3.split("   "))
print()

number = 54
print(str(number))
print(float(number))

print()
frac = 1.333546

print(str(frac))
print()

lst = [1,2,3,4,5,6]

print(str(lst))


#etc
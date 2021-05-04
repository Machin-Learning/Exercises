import math
# eval(source) func evaluates the string like like a python exprassion and return the result as integer
x = eval(input("Enter a number:"))
print(eval("x**2+x*2-2"))
# print(type(x))

# len(o) returns the number of items in objects
numbers = [4,76,2,34,12,9]
print(len(numbers))

# factorial() func in the math module help us to compute the factorial of a number without writing the whole code
print(math.factorial(5))

# sort() func sorts the elements of an objects in a specified ascending or descending order.

runs = [45,10,150,76,28,90,200]
runs.sort(reverse=True)
print(runs)
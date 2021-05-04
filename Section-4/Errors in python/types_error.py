#Types of Error

            # 1. Sentax Error
            # 2. indentationError
            # 3. Type Error
            # 4. value Error
            # 5. name Error
            # 6. Zero Division Error
            # 7. Index Error
            # 8. Attribute Error
            # etc

a=4
b=0

# print(a/b)  #ZeroDivisionError: division by zero

# print(a + c)  #NameError: name 'c' is not defined

s ="Hello"

# print(a + s)  #TypeError: unsupported operand type(s) for +: 'int' and 'str'

l = [1,2,3,4,5]

# print(l[5])  #IndexError: list index out of range

# def add(a,b):
# print(a+b)   #IndentationError: expected an indented block

# s.gun()    #AttributeError: 'str' object has no attribute 'gun'
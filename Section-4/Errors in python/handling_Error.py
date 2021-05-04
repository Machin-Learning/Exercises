# 1. ZeroDivisionError: division by zero 
#Lets handale

a = 4
b = 0

# try:
#     c = a / b
#     print(c)
# except ZeroDivisionError:
#     print("Can not divide by Zero")

# except:
#     print("Something else went wrong")

# try:
#     c = a / 2
#     print(c)

# except ZeroDivisionError:
#     print("Can't Divide by Zero")

# else:
#     print("Noting went wrong")


try:
    c = a / b
    print(c)

except:
    print("Something went wrong")

finally: #most of the time used in badabase or file handling 
    print("The Try Except is finished")
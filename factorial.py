import random
def factorial():
    num = random.randint(1,10)
    factorial = 1
    for i in range(num,0,-1):
        factorial *= i

    return (num,factorial)


print(factorial())

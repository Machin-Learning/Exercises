import random

def calculate_length():
    count = 0
    n = random.randint(1,5000)
    for i in str(n):
        count+=1
    return (n,count)

print(calculate_length())

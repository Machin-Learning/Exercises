import random
def sum_digits():
    n = random.randint(100,300)
    total = 0
    for i in str(n):
        total += int(i)

    return n,total

print(sum_digits())

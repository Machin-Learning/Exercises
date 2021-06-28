import random

def fibonacchi():
    n = random.randint(5, 10)
    l = [0,1]
    for i in range(n):
        l.append(l[i]+l[i+1])

    return n,l[:n]

print(fibonacchi())
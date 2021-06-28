def prime_num(num):
    p = []
    for i in range(1,num+1):
        if num%i == 0:
            p.append(i)
    if p == [1,num]:
        result = True
    else:
        result = False
    return (result)

print(prime_num(5))
print(prime_num(4))

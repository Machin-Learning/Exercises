def check_division(a,b):
    if a>b:
        if (a+b)%b == 0:
            return a+b


print(check_division(25,5))

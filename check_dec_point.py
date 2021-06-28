def check_division(num):
    if num == int(num):
        result = True
    else:
        result = False
    return num,result

print(check_division(4/2))

print(check_division(25/4))

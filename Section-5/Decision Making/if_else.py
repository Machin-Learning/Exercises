a = 10
b = 5
c = 15

if a > b:
    print("a greater than b")
else:
    print("b greater than a")

if (a>b) and (a>c):
    print("a is greatest")
else:
    if (b>a) and (b>c):
        print("b is greatest")

    else:
        print("c is greatest")
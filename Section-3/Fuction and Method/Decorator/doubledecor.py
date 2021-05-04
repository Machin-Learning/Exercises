def decor(fun):
    def inner():
        result = fun()
        return result*2
    return inner

@decor
def num():
    return 5

# resultfunc = decor(num)

print(num())
def scope():
    a = 5
    def outer():
          
        b = 10
        return (res1+b)
        nonlocal def inner():
            c = 15
            return (c)
      
        res1 = inner()
    res2 = outer()
    return (res2+a)

print(scope())
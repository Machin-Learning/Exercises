def booleans(x,y,z):
    result = True
    if x==y==z:
        result = True
    elif x==y:
        result = True
    elif y==z:
        result = True
    elif x ==z:
        result = True
    else:
        result = False
    return (x,y,z,result)

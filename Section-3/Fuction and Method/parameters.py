# Default Parameters

def addition(x=0,y=0):
    return print(x+y)

#*args parameters

def add(*args):
    return print(sum(args)) 

#**kwargs parameter
def userInfo(**kwargs):
    for key,value in kwargs.items():
        print(f"{key} : {value}")

#pass function 
def temp():
    pass
addition()
addition(4,4)
add(1,2,3,4)
userInfo(name="Muzmmil",age=26)
temp()
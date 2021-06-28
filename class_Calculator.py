class Calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def add(self):
        value_add = round((self.x+self.y),2)
        return self.x,self.y,value_add
    
    def sub(self):
        value_sub = round((self.x-self.y),2)
        return self.x,self.y,value_sub

    def mul(self):
        value_mul = round((self.x*self.y),2)
        return self.x,self.y,value_mul
    
    def div(self):
        value_div = round((self.x/self.y),2)
        return (self.x,self.y,value_div)


cal = Calculator(2,2)

print(cal.add())
print(cal.sub())
print(cal.mul())
print(cal.div())
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def compare(self,other):
        if self.age > other.age:
            return f'{other.name} is younger than me'
        elif self.age < other.age:
            return f'{other.name} is older than me'
        else:
            return f'{other.name} is same age as me'  


p1 = Person('Nancy',45)
p2 = Person('Maya',36)
p3 = Person('Allen',45)

print(p1.compare(p2))
print(p2.compare(p1))
print(p1.compare(p3))
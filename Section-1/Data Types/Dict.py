                                                #         #Dictionary
                                # 1. Dict in python is muttable/changeable and does not show duplicate
                                # 2. Dict are unorder and unindex collection of items and each item has keys:value paire  seprated by comma inside {k:v,}
                                # 3. Dict can't be indexed or slice
                                # 4. Dict can't add/concat or scale/multiply but we can update()
                                # 5. we can use Dict to store multiple k:v items in one variable
                                # 6. Dict are itrator


d = {"name":"Muzmmil Khan","age":26}


print(d)
print(d.keys())
print(d.values())
print(d.items())
print(enumerate(d))
print(len(d))

print(d["name"])
print(d["age"])
print()

# dictionary in python support item assignment
d["name"] = "Muzammil Pathan"

print(d)

# print(d[0]) #KeyError: 0

print(d.pop("age"))
print(d)
print(d.popitem())
print(d)

Dict = {"a":1,"b":2,"c":3}

print(Dict)

print(Dict.get("a"))

print(Dict.fromkeys("a"))
print(Dict)

print(Dict.update({"d":4}))
print(Dict)

print(Dict.clear())
print(Dict)


print()
a = {"a":1,"b":2}
b = {"c":3,"d":4}

# print(a+b) #TypeError: unsupported operand type(s) for +: 'dict' and 'dict'

# print(a*2) #TypeError: unsupported operand type(s) for *: 'dict' and 'dict'
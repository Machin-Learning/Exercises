import json

x = {"name":"muzmmil","age":26,"email":"muzmmilpathan@gmail.com","port":(8000,8080),"Active":True}

j = '{"name": "muzmmil", "age": 26, "email": "muzmmilpathan@gmail.com", "port": [8000, 8080], "Active": true}'
# y = json.dumps(x)
y = json.loads(j)

print(y)
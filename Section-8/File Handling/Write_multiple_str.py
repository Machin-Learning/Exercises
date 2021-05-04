f = open("multiple_str.txt","w")
print("Enter Text (to End writing enter #)")
s = ''

while s != '#':
    s = input()
    f.write(s+"\n")

f.close()
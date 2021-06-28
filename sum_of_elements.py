l = [5,7,1,2,8,4,3]
o = []
for i in range(len(l)):
    for j in range(len(l)):
        if l[i]+l[j] == 10 and l[i] != l[j]:
            if [l[j],l[i]] not in o:
                o.append([l[i],l[j]])


print(o)

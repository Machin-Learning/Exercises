set1 = {2,4,6,8,9,10}
set2 = {1,3,5,7,9,11}

for i in set2:
    if i not in set1:
        set1.add(i)
    
print(set1)

o = set1.difference_update(set2)
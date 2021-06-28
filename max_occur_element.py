l = [1,13,3,3,3,4,5,6,6,3,3,3,8]
me = 0
position = 0
d = {1:12,2:14,5:4,6:45}
count = {}
print(max(d))

for i in l:
    count[i] = l.count(i)
print(count)
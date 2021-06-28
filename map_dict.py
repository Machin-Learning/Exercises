def map_lists(list1,list2):
    return (dict(zip(list1,list2)))

list1 = [1,2,3,4,5]
list2 = [6,7,8,9,10]
print(map_lists(list1,list2))
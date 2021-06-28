def return_index(input_list,target):
    index_num = 0
    if target in input_list:
        index_num = input_list.index(target)
    else:
        for i in input_list:
            if i>target:
                break
            else:
                index_num += 1
    return (index_num)

l = [0,1,5,7,8]
t = 6
print(return_index(l,t))

def remove_zero(input_list):
    modified_input_list = []
    for i in input_list:
        if i == 0:
            pass
        else:
            modified_input_list.append(i)
    return (modified_input_list)

d = [1,2,3,0,4,0,5,8,0,0]
print(remove_zero(d))
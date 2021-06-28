def replace_value(input_list):
    modified_input_list = []
    for i in input_list:
        if i == 'd':
            modified_input_list.append('c')
        else:
            modified_input_list.append(i)
            
    return (modified_input_list)

d = ['a','c','d','d','f','k']
print(replace_value(d))
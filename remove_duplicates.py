def remove_duplicates(input_dict):
    output_list = []
    for value in input_dict.values():
        if value in output_list:
            continue
        else:
            output_list.append(value)
    
    return output_list

d = {'Box1':'Apple','Box2':'Mango','Box3':'Orange','Box4':'Apple','Box5':'Orange','Box6':'Orange','Box7':'Stoberry','Box8':'Apple'}
print(remove_duplicates(d))
res = list(set({val for val in d.values()}))

print(res)
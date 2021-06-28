def dict_sort(input_dict):
    inv_dict = {value:key for key,value in input_dict.items()}
    sorted_dict = {}
    for key in sorted(inv_dict):
        sorted_dict[key] = inv_dict[key]
    sorted_dict = {value:key for key,value in sorted_dict.items()}
    return (sorted_dict)
d = {'Apple':10,'Bannana':6,'Mango':12,'Orange':5}
print(dict_sort(d))
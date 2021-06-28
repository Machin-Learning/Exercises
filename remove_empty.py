def remove_empty(input_dict):
    output_dict = {}
    for key,value in input_dict.items():
        if value == ' ':
            continue
        else:
            output_dict[key] = value
    return (output_dict)


d = {'Box1':'Apple','Box2':'Mango','Box3':'Orange','Box4':' ','Box5':' '}

print(remove_empty(d))


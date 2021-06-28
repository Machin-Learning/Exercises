def invert_dict(input_dict):
    output_dict = {}
    for key,value in input_dict.items():
        output_dict[value] = key
    return output_dict
d = {'Box1':'Apple','Box2':'Mango'}

print(invert_dict(d))
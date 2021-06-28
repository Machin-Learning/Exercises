import string
def to_dict(input_list):
    ascii_upper = [x for x in string.ascii_uppercase]
    ascii_lower = [x for x in string.ascii_lowercase]
    ascii_upper_dict = {x:ascii_upper.index(x)+65 for x in ascii_upper}
    ascii_lower_dict = {x:ascii_lower.index(x)+97 for x in ascii_lower}
    ascii_upper_dict.update(ascii_lower_dict)
    output_list = [{x:ascii_upper_dict[x]} for x in input_list]
    return output_list

l = ['P','y','t','h','o','n']

print(to_dict(l))


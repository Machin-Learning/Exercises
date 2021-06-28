import string
def convert_to_hex(input_string):
    ascii_upper = [x for x in string.ascii_uppercase]
    ascii_lower = [x for x in string.ascii_lowercase]
    # ascii_upper.insert(index, object)
    ascii_upper_dict = {x:ascii_upper.index(x)+65 for x in ascii_upper}
    ascii_lower_dict = {x:ascii_lower.index(x)+97 for x in ascii_lower}
    ascii_upper_dict.update(ascii_lower_dict)
    hexd = ''
    for i in input_string:
        hexd += hex(ascii_upper_dict[i])
    hex_code = hexd.replace('0x',' ').strip()
    
    return hex_code

print(convert_to_hex('Python'))
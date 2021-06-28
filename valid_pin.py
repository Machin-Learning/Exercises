import re
def valid_pin(input_string):
    result = True
    if  input_string.isdigit():
        x = re.findall("[0-9]", input_string)
        if len(x) == 5:
            result = True
        else:
            result = False
    else:
        result = False
    return result

print(valid_pin("123abc"))
def string_to_bool(input_string):
    i = input_string.lower()
    if i == 'true':
        return True
    elif i == 'false':
        return False
    else:
        return 'Invalid input'


print(string_to_bool('TRUE'))
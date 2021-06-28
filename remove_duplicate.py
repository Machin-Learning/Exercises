def remove_duplicate(input_string):
    output_string = ''
    for i in input_string:
        if i not in output_string:
            output_string += i
    return output_string


print(remove_duplicate('bookkeeper'))


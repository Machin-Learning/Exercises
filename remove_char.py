def remove_char(input_string,char):
    output_string = ''
    for letter in input_string:
        if letter != char:
            output_string += letter
            
    return (output_string)

print(remove_char('technique', 'e'))
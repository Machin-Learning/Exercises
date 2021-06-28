def remove_spaces(input_string):
    l = input_string.split(' ')
    output_string = ''
    for i in l:
        output_string += i
        
    return (output_string)

print(remove_spaces('A B C'))
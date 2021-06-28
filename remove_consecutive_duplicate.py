def remove_duplicates(input_string):
    out = ''
    for i in range(len(input_string)-1):
        if input_string[i] == input_string[i+1]:
            continue
        else:
            out += input_string[i]
    output_string = out+input_string[-1]
    return (output_string)

print(remove_duplicates('mississauga'))


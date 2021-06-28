def reverse_string(input_string):
    o = input_string.split()[::-1]
    out = ''
    for i in o:
        out += i+' '
    output_string = out.strip()
    return (output_string)

print(reverse_string(" I am Fine"))
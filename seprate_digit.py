def separate_digits(num):
    num = str(num)
    output_list = []
    for i in num:
        output_list.append(int(i))
        
    return (output_list)

print(separate_digits(1234))
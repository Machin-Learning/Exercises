def num_to_list(num):
    num = str(num)
    output_list = []
    for i in num:
        output_list.append(int(i))
        
    return (output_list)

print(num_to_list(1234))
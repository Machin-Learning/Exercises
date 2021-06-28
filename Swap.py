def swap_bits(num):
    b = bin(num).replace('0b','00')
    l = list(b)
    l[2],l[6] == l[6],l[2]
    output_str = ''
    for i in l:
        output_str += i
    output_num = int(output_str,2)
    return output_num

print(swap_bits(40))

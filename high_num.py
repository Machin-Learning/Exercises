def high_num(input_list):
    input_list.sort(reverse=True)
    highest_num = input_list[0]
    return (highest_num)

l = [9,6,45,67,12]
print(high_num(l))
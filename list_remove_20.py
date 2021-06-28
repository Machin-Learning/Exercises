
def remove_20(input_list):
    l = []
    for i in input_list:
        if i == 20:
            continue
        else:
            l.append(i)
    input_list = l
    return input_list


l = [20,50,40,70,9,20]
print(remove_20(l))

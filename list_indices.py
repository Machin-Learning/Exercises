def indices(input_list,element):
    output_list = []
    for i in range(len(input_list)):
        if input_list[i] == element:
            output_list.append(i)
            
    return output_list
l = [10,6,7,10,9,1,-1,10]


print(indices(l,10))
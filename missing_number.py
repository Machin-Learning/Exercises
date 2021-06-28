def missing_number(input_list):
    input_list.sort()
    out_list = [x for x in range(input_list[-1]+1)]
    missing_num = 0
    for i in out_list:
        if i not in input_list:
            missing_num = i
            
    return missing_num


l = [0,3,2,1,5]
print(missing_number(l))
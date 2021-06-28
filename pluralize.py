def pluralize(input_list):
    output_list = []
    count_d = {}
    for i in input_list:
        count_d[i] = input_list.count(i)
    for key,value in count_d.items():
        if count_d[key]>1:
            output_list.append(key+'s')
        else:
            output_list.append(key)
    output_list = list(set(output_list))
    return output_list


l = ['table','chair','chair','chair','desk','desk']
print(pluralize(l))
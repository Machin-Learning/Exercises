def word_sort(input_list):
    sorted_list = sorted(input_list,key=lambda elem:elem[1])
    return sorted_list

l = ['coral','real','mustard','blue voilet','maroon','indigo','white','lime','navy']

print(word_sort(l))


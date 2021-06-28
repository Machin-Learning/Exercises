def kth_largest_element(input_list,k):
    input_list.sort(reverse=True)
    output = input_list[k-1]
    return output

l = [301,279,205,175,161,116,111,70,13,6]
print(kth_largest_element(l,1))
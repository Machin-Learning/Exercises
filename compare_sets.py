def compare_sets(set1,set2):
    output_set = set1.difference(set2)
    return (output_set)


set1 = {2,4,6,8,9,10}
set2 = {1,3,5,7,9,11}


print(compare_sets(set1,set2))
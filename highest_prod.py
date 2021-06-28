def highest_prod(input_list):
    input_list.sort(reverse=True)
    prod = input_list[0]*input_list[1]*input_list[2]
    return (prod)

l = [20,7,3,6,-1,0,9]

print(highest_prod(l))

def multiple_elements(input_list):
    product = 1
    for i in input_list:
        product *= i
    return (product)

l = [1,2,3,4,5,6,6,5]

print(multiple_elements(l))
def divide_by_15():
    import random
    input_list = [random.randint(0,100) for i in range(10)]
    output_list = [x for x in input_list if x%15==0]
    return input_list,output_list

print(divide_by_15())

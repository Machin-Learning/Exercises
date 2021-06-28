def concat(*n):
    output_list = []
    for i in n:
        output_list.extend(i)
        
    return (output_list)
a = [1,2,3],[4,5,6],[7,8],[9]

print(concat(*a))
print()
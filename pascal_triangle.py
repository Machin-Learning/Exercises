n = 4

output_list = []
for i in range(n):
    temp_list = []
    for j in range(i+1):
        if j==0 or j == i:
            temp_list.append(1)
        else:
            temp_list.append(output_list[i-1][j-1] + output_list[i-1][j])
    output_list.append(temp_list)


print(list1)
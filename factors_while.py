def factors(num):
	output_list = []
	i = 1
	while i<=num:
		if num%i == 0:
			output_list.append(i)
		i +=1
	return output_list	



print(factors(26)) 

def decimal_part(num):
	if type(num) == int:
		return 'INTEGER'
	else:
		return round(num-int(num),2)


print(decimal_part(1.9))

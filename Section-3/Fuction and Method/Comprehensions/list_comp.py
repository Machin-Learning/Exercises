my_list = [2,3,4,5,6]
#square the my_list using comprehension

sq_list = [val**2 for val in my_list]

even_list = [val for val in my_list if val%2==0]
print(sq_list)
print(even_list)
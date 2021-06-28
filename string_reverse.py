def string_reverse(first_name,last_name):
    ## Your code here
    s = first_name+' '+last_name
    new_string = s[::-1]
    return (new_string)

print(string_reverse('Muzammil', 'Khan'))
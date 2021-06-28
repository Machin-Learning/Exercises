def find_substring(main_string,sub_string):
    num = main_string.count(sub_string)
    position = [main_string.find(sub_string),main_string.rfind(sub_string)]
    return (num,position)

m = 'Let it be,let it be,let it be'
s = 'let it be'
print(find_substring(m, s))
def str_first2_last2_char(input_string):
    output_string = input_string[:2]+input_string[-2:]
    return output_string

print(str_first2_last2_char('Python'))
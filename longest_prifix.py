def longest_prefix(s1,s2,s3,s4):
    output_string = ''
    if s1[0] == s2[0] == s3[0] == s4[0]:
        for i in s2:
            if i in s1:
                output_string += i
    return output_string


print(longest_prifix('floor', 'float', 'floral', 'follow'))
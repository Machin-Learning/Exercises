def count_case(sample_string):
    count = 0
    for i in sample_string:
        if i.isupper():
            count += 1
    return (count)
    

print(count_case("Python Is Supper Easy"))
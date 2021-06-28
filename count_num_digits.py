import datetime
print(datetime.datetime.now())
def count_num_digits(input_string):
    count = 0
    for i in input_string:
        if i.isdigit():
            count+=1
    return count

print(count_num_digits('abcd12345'))
print(count_num_digits('xyz457'))

for i in range(5):
    print("Hello")

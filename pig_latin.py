def pig_latin(input_string):
    c = ['a','e','i','o','u']
    for i in input_string:
        if i in c:
            a = input_string.find(i)
            break
    output_string = input_string[a:]+input_string[:a]+'ay'
    return (output_string)

print(pig_latin('scream'))
def count_vowels(input_string):
    l = ['a','e','i','o','u','A','E','I','O','U']
    vowels = 0
    for letter in input_string:
        if letter in l:
            vowels += 1
            
    return vowels

print(count_vowels('dolphin'))
import random


string = "I Love Python" # Str of senteance

l = [1,2,3,4,5,6,7,8,9,10] # list of numbers from 1 to 10

t = (1,2,3,4,5,6,7,8,9,10) # tuple of numbers from 1 to 10

s = {1,2,3,4,5,6,7,8,9,10,} # Set of numbers from 1 to 10

d = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10
}           # Dict of keys values paire keys from a-j and values from 1-10


#let's loop through the string
i = 0
while i < len(string):
    print(string[i])
    i += 1

print()

i = 0
ls_str = string.split(" ")
while i < len(ls_str):
    print(ls_str[i])
    i += 1

print()

#lets loop through the list

i = 0
while i < len(l):
    print(l[i])
    i += 1


#let's loop through the tuple

i = 0
while i < len(t):
    print(t[i])
    i += 1

print()
#let's loop through the set
i = 0
while i < len(s):
    #print(s[i]) #TypeError: 'set' object is not subscriptable
    print(s.pop())
    i += 1

#let's loop through the dictionary

item = list(d.items())

i = 0
while i < len(item):
    print(item[i])
    i += 1

i = 0
key = list(enumerate(d))

while i < len(key):
    print(key[i])
    i += 1

keys = list(d.keys())
values = list(d.values())
i = 0
while i < len(keys):
    print(keys[i],values[i])
    i += 1

#let's print even

i = 0

while i < 11:
    if i%2 == 0:
        print(i)
    i += 1

print()
#let's print odd numbers
i = 0

while i < 11:
    if i%2 != 0:
        print(i)
    i += 1

#Nested while loop
print()
mx = [[1,2,3],[4,5,6],[7,8,9]]

i = 0
j = 0
while i < len(mx):
    while j < len(mx[i]):
        print(mx[j])
        j += 1
    i += 1

#user input
# user = input("Enter N:")
# i = 0
# while i < int(user)+1:
#     print(i,end=" ")
#     i += 1

# # Break in while loop
# x = random.randint(1, 6)

# while True:
#     guess = int(input("guess a number between 1 to 6: "))
#     if guess == x:
#         print("You Guessed Correct")
#         break
#     elif guess < x:
#         print("guess is low")
#     else:
#         print("guess is high")


# continue in while loop 

i = 0

while i < 11:
    if i == 5:
        break
    else:
        print(i)
    i += 1

#COntinue
print()

i = 0

# while i < 11:
    
#     if i == 5:
#         continue
#     else:
#         print(i)
#     i += 1
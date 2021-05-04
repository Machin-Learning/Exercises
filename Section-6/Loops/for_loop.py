string = "I Love Python" # Str of senteance

l = [1,2,3,4,5,6,7,8,9,10] # list of numbers from 1 to 10

t = (1,2,3,4,5,6,7,8,9,10) # tuple of numbers from 1 to 10

s = {1,2,3,4,5,6,7,8,9,10} # Set of numbers from 1 to 10

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

#lets loop on strings

for char in string:
    print(char)

print()
for word in string.split(" "): #split(" ") convert the list of spaced word into  list ['I','Love','Python'] 
    print(word)

#lets try to loop through list
print()
for data in l:
    print(data) 

#let's loop through tuple
print()
for data in t:
    print(data)

#let's loop through the set
print()
for item in s:
    print(item)


#let's loop through the dictionary
print()
for key,value in d.items():
    print(f"{key}:{value}")

for index,value in enumerate(d):
    print(f"{index}:{value}")

for key in d.keys():
    print(key)

for value in d.values():
    print(value)

for key in zip(d.items()):
    print(key,value)

for i in range(1,11): # range genrate 1 to 10 value yield/genrator
    print(i) 
    
#lets print even nubmber 

for even in range(1,11):
    if even%2 == 0:
        print(even)
print()
for i in range(0,11,2):
    print(i)
#let's print odd numbers
print()
for odd in range(1,11):
    if odd%2 != 0:
        print(odd)

print()
for i in range(1,11,2):
    print(i)


#Nested for loop
print()
mx = [[1,2,3],[4,5,6],[7,8,9]]

for m in mx:
    for l in m:
        print(l)

ls_l = []
for i in range(1,4):
    for j in range(1,4):
        ls_l.append(j)
print(ls_l)
#Loops and userInput

user = input("Enter N:")

for i in range(1,int(user)+1):
    print(i,end=" ")


#for lop with else

for i in range(4):
    print(i)

else:
    print("Loop Completed")


# break and continue
#Break
print()
for i in range(1,10):
    print(i)
    if i == 5:
        break

#continue
print()
for i in range(1,10):
    if i == 5:
        continue
    print(i)


for i in "movie":
    if i == "o":
        pass
    print(i)
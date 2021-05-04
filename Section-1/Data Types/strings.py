                                #         #String
                                # 1. string in python is immutable/non changeable but can be modify by using replace(),join(),split()
                                # 2. string are sequence of charector
                                # 3. string can be indexed or slice
                                # 4. string can add or scale/multiply
                                # 5. we can use string to store sentances also chars
                                # 6. we can get the size of string using sys.getsizeof(string) in bytes
                                # 7. strings are itrator         


string = "python is easy to learn"

print(string)
print(type(string))

# string in python does not support item assignment
# string[string.find("easy")] = "Hard" TypeError: 'str' object does not support item assignment
print(string) 


#Indexing :left to right [0][1][2][3][.][n]
#          right to left [-1][-2][-3][-.][-n]

#Let's see
print(string[0])
print(string[5])
print()
print(string[-1])
print(string[-5])
print()
# print(string[0][1]) #IndexError: string index out of range


#Slicing on string: [start,stop+1,step]
print(string[0:6]) # note : stop value not include the i.e it's print from 0 to 6-1=5

print(string[0:]) # to print all the string from 0 to end
print(string[:])

print(string[0:10]) # to print specifide index i.e 0 to 10-1

print(string[::-1]) # to print string in revers step

print(string[::2]) # to print string in step of 2
print()
#Operation on string 
    # 1. Concatination of string
    # 2. Split the string
    # 3. reverse the string
    # 4. convert into upper,lower,title,capitalize,
    # 5. join the string
    # 6. scale/multiply the string
    # 7. trim the string from left right
    # 8. count the charector in  the string
    # 9. insert into the string
    # 10. replace the word letter in string
    # 11. find the char,word,letter in string from left ,right side
    # 12. length of a string
    # 13. check wether isupper, islower,isalnum,isalpha ..etc
                #etc

s = "  I Love Python   "

print(string + s)

print(string.split())

print(s[::-1])

print(s.upper())

print(s.lower())

print(s.title())

print(s.capitalize())

date = "dmy"

print("/".join(date))
print("-".join(date))

print(s*3)
print()
print(s)
print(s.lstrip())
print(s.rstrip())

print(len(s))
print(s.count("o"))

print(string+"Inserting at the end")
print("Inserting at the Begining "+string)
print(s[0] + " Very much "+s[2:])

print()
print(s.replace("Love", "Hate"))

print()
print(string.find("easy"))

print()
print(s.isalpha())
print(s.isalnum())
print(s.isupper())
print(s.islower())
print()

print(s.partition(","))

print(s.startswith("I"))

print(s.zfill(2))

print(s.swapcase())

print(s)

#Formating a string

#before python v3.5

name = "Muzmmil"
age = 26
death = 100 
print("Welcome {} .Your age is {} and you are eligible to see this contant".format(name,age))

print("your living time is ={}".format(death-age))
#After python v3.6 and above

print(f"Welcome {name} .Your age is {age} and you are eligible to see this contant") # i love this type of formatinfg


#Escape Carector
print("I love python \nFuture is Machin Learning")

print()

print("I have knowlege of programming:\t python")

print("I need \"Job\" in Machin Learning")

print('I\'m an Engineer')

print("Users are in /home")
print("Linex path of file uses forword slash / and windows uses \\")

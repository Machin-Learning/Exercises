def new_letter(s,t):
    letter = ''
    for i in t:
        if i not in s:
            letter += i
            
    return letter

print(new_letter('Python', 'thonbPy'))
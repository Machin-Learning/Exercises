import string
def pangram(sample_string):
    a = [x for x in string.ascii_lowercase]
    b = []
    for i in sample_string.lower():
        if i not in b:
            b.append(i)
    c=sorted(b)
    c.remove(' ')
    resutl = True
    if a == c:
        result = True
    else:
        result = False
    return (result)

print(pangram("The quick brown fox jumps over the lazy dog"))
print(pangram("The quick brown fox umps over the lazy dog"))

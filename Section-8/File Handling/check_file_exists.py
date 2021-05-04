import os,sys

if os.path.isfile("multiple_str.txt"):
    f = open("multiple_str.txt","r")
    s = f.read()
    print(s)
    f.close()

else:
    print("File Do's Not Exist")
    sys.exit()
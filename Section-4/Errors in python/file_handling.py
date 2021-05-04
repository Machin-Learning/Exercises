try:
    f = open("file1","a")
    a,b = [int(x) for x in input("Enter two Numbers:").split()]
    c = a/b
    f.write(f"Writeing {c} in file\n")

except ZeroDivisionError:
    print("Zero Division are not allowed")
    print("Please Enter Non Zero number")
except ValueError:
    print("Invalid Input")
else:
    print("Division operation done Sucessfuly")
finally:
    f.close()
    print("File Close")
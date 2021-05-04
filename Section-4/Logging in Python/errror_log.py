import logging
try:
    logging.basicConfig(filename="Divi.log",level=logging.DEBUG)
    a,b = [int(x) for x in input("Enter two Numbers:").split()]
    c = a/b
    logging.info("Division is Processing")

except ZeroDivisionError:
    print("Zero Division are not allowed")
    print("Please Enter Non Zero number")
    logging.error("Zero Division Error")
except ValueError:
    print("Invalid Input")
else:
    print("Division operation done Sucessfuly")
finally:
    print("logging")
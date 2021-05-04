class TooYoungException(Exception):
    def __init__(self,msg):
        self.msg = msg

class TooOldException(Exception):
    def __init__(self,msg):
        self.msg = msg


age = int(input("Enter Your Age:"))

if age<18:
    raise TooYoungException("You are not Eligible")
elif age > 90:
    raise TooOldException("Younare not Eligible")
else:
    print("You are Eligible")



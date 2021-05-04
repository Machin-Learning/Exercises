try:
    num = int(input("Enter a Even Number:"))

    assert num%2==0,"You have enter a invalid number or Odd number"
except AssertionError as obj:
    print(obj)

print("Code after the error")
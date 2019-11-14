#write a program to accept a value and fint it's even or odd.
num=int(input("enter number to check whether it is odd or even"))
if num == 0:
    print("this is Zero")
elif num < 0:
    print("This is negative number")
elif num%2 == 0:
    print("it is even")
else:
    print("it is odd")

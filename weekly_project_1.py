# Make a calculator.
name = input("Enter your name ")
while name.isalpha()==False or len(name)<3:
    name=input('Wrong !!!! Enter again')
age = input("Enter your age")
while age.isdigit()==False or int(age)<18 or int(age)>120 :
    age=input("Input your correct age ")
mobile = input("Enter your mobile number ")
while len(mobile) != 10 or mobile.isalpha == True:
    mobile = input("Enter correct mobile number ")
password=input("Enter the password to use calculator..!")
while password != "aman":
    password = input("Enter the correct password")
print("Welcome to the calculator...!")
print("Select Operation")
print("1.Addition")
print("2.Subtraction")
print("3.Division")
print("4.Multiplication")
print("5.Squares")
print("6.Cube")
print("7.Square Root")
choice = int (input("Enter choice(1/2/3/4/5/6/7): "))
if choice == 1:
    num1 = int(input("Enter your first number to add"))
    num2 = int(input("Enter your second number to add"))
    print("your sum is ",num1+num2)
elif choice ==2:
    num1 = int(input("Enter first number to subtract"))
    num2 = int(input("Enter Second number to subtract"))
    print("The subtraction is ",num1-num2)
elif choice == 3:
    num1 = int(input("Enter your Dividend"))
    num2 = int(input("Enter your divisor"))
    print("The division is ",num1/num2)
elif choice == 4:
    num1 = int(input("Enter your first number to multiply"))
    num2 = int(input("Enter your second number to multiply"))
    print("The product is ",num1*num2)
elif choice == 5:
    num1 = int(input("Enter number to find squares"))
    print ("The square is ",num1*num1)
elif choice == 6:
    num1 = int(input("Enter number to find Cube"))
    print("The cube is ",num1*num1*num1)
elif choice == 7:
    num1 = int(input("Enter number to find Square Root"))
    print("The square root is ",num1**(1/2))
else:
    print("Invalid input")

# wrote a program menu driven calculator
print("selecet operation")
print("1.add")
print("2.subtract")
print("3.multiply")
print("4.divide")
choice = int(input("enter choice(1/2/3/4): "))
if choice == 1:
    num1 = int(input("enter first number"))
    num2 = int(input("enter second number"))
    num3 = num1+num2
    print(num3)
elif choice ==2:
    num1 = int(input("enter first number"))
    num2 = int(input("enter second number"))
    print(num1-num2)
elif choice ==3:
    num1 = int(input("enter first number"))
    num2 = int(input("enter second number"))
    print (num1*num2)
elif choice ==4:
    num1 = int(input("enter first number"))
    num2 = int(input("enter second number"))
    print(num1/num2)
else:
    print("invalid input")
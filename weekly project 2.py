def calc():
    def add():
        num1=int(input("Enter first number "))
        num2=int(input("Enter second number "))
        print("The sum of %s and %s is %s " %(num1,num2,num1+num2))
        again=input("Enter yes to do again. \nEnter any to skip")
        while again==("yes"):
            add()
        else:
            calc()
    def sub():
        num1=int(input("Enter first number "))
        num2=int(input("Enter second number "))
        print("The Difference is %s"%(num1-num2))
        again=input("Enter yes to do again. \nEnter any to go to calculator")
        while again==("yes"):
            sub()
        else:
            calc()
    def mul():
        num1 = int(input("Enter first number "))
        num2 = int(input("Enter second number "))
        print("The Product is %s" % (num1 * num2))
        again = input("Enter yes to do again. \nEnter any to go to calculator")
        while again == ("yes"):
            mul()
        else:
            calc()
    def div():
        num1 = int(input("Enter first number "))
        num2 = int(input("Enter second number "))
        print("The Division is %s" % (num1 * num2))
        again = input("Enter yes to do again. \nEnter any to go to calculator")
        while again == ("yes"):
            div()
        else:
            calc()
    print("Welcome to the calculator")
    choice=input("Enter choice ")
    if choice==("add"):
        add()
    if choice==("subtract"):
        sub()
    if choice==("mul"):
        mul()
    if choice==("div"):
        div()
calc()

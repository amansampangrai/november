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
    choice=input("Enter add, subtract, multiply, divide ")
    if choice==("add"):
        add()
    if choice==("subtract"):
        sub()
    if choice==("multiply"):
        mul()
    if choice==("divide"):
        div
def calc2():
    def sqrt():
        num1=int(input("Enter number to find square"))
        print("The square of %s is %s" %(num1,num1**0.5))
        again=input("If you want to do again then type yes or type any to go to calculator")
        while again==("yes"):
            sqrt()
        else:
            exit()
    def square():
        num1=int(input("Enter any number to find square"))
        print("The square of %s is %s" %(num1,num1**2))
        again=input("Enter yes if you want to do again or type any to go to calculator")
        while again==("yes"):
            square()
        else:
            exit()
    choice=input("Enter squareroot or square")
    if choice==("squareroot"):
        sqrt()
    if choice==("square"):
        square()
if __name__=='__main__':
    select=input("Enter 1 for simple calculator and 2 for advanced calculator")
    if select==("1"):
        calc()
    if select==("2"):
        calc2()

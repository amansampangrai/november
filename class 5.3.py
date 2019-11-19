#write a function to test if a number entered by the user is armstrong or not. eg: 371,   3^3+7^3+1^3=371
#This is only just for 3digit.
'''def armstrong():
    a=int(input("Enter first digit"))
    b=int(input("Enter second digit"))
    c=int(input("Enter third digit"))
    d=a**3
    e=b**3
    f=c**3
    g=a*100+b*10+c
    if d+e+f==g:
        print("IT is armstrong")
    else:
        print("It is not armstrong number")
armstrong()'''

def armstrong():
    num=int(input("Enter number to check armstrong number"))
    a=num
    sum=0
    while a>0:               # a=371
        b=a%10              #   b=1
        c=b**3              #c=1**3=3
        sum=sum+c           #sum=0+3=3
        d=a//10                #d=371//10=37
        a=d                     #a=37
    if sum==num:
            print("It is armstrong number")
    else:
            print("It is not armstrong number")
armstrong()

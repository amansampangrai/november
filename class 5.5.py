# write a program to find factorial.
'''# change the value for a different result
num = 3
# To take input from the user
#num = int(input("Enter a number: "))
factorial = 1
# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)'''
'''def factorial():
    num=int(input("Enter number to find factorial"))
    fact=1
    for x in range(1,num+1):
            fact=fact*x
    print("The factorial is ",fact)
factorial()'''

def factorial():
    num=int(input("Enter the number"))
    fact=1
    a=num
    while a>0:
        fact=fact*a
        a=a-1
    return fact
a=factorial()
print("The factorial is ",a)
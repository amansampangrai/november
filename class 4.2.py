# write a program to print multiplication table of the number entered by the user.
num=int(input("Enter number to find multiplicaton table"))
for x in range(1,11):
    print("The Product of %s * %s = %s" %(num,x,num*x))
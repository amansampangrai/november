#write a function pow(a,b). the function should return the value a raised to the power of b.(a^b).
def pow(a,b):
    a=int(input("Enter number to find power"))
    b=int(input("Enter power"))
    c=a**b
    return c

a=0
b=0
num=pow(a,b)
print("The answer is ",num)
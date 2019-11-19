# reverse string

'''def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


s = input("Enter any words to reverse")

print("The original string  is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))'''







def reverse(s):
    str=""
    for i in s:     #s=aman, i=a,m,a,n
        str=i+str       #str=a, ma,ama,nama
    return str
s=input("Enter any words to find reverse ")
#print("The reverse of %s is %s"%(s,reverse(s)))
a=reverse(s)
print(a)

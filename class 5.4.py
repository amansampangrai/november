# write a function to check if a number is reverse of the number. i.e palindrome eg: 12321 is a palindrome.

def palindrome():
    num=int(input("Enter number to check palindrome "))
    a=num
    sum=""
    while a>0:               #a=12321
        b=a%10                  #b=1
        sum = sum + str(b)      #sum=1
        c=a//10              #c=1232
        a=c                  #a=1232
    sum=int(sum)
    if sum==num:
            print("THe number is palindrome")
    else:
            print("The number is not palindrome")
palindrome()


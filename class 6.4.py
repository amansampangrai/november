# write a program to find prime number from 1 to 2500 using list comprehension.

'''def prime():
  #  num=int(input("Enter number"))
    for num in range(1,250):
        a=num
        if a>0:
            if a%2!=0 and a%3!=0 and a%5!=0 and a%7!=0:
                primeno=a
                print(primeno)
            else:
                continue
prime()'''

'''def prime():
    num=int(input("Enter any number to check prime number"))
    if num%2==0 or num%3==0 or num%5==0 or num%7==0:
        print("It is prime number")
    else:
        print("It is not prime number")
prime()'''

# the correct answer

lst=[x for x in range(2,100)if all (x%y !=0 for y in range(2,x))]
print(lst)

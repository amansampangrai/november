# write a program to ask user to enter the name, age and mobile number using validation.
'''mobile number should be numerice, name should be alphabet only age should be greater than 18
hint: use isdigit(), isalpha(), isnull()'''
name = input ("Enter your name")
#if name.isalpha()==False:
if name.isdigit()==True or len(name)<=2:
    print("your name should be alphabet and more than two character")
   # name=input("Enter your name")
else:
    age = int(input("Enter your age"))
    if age < 18:
        print("Your age should be more than 18")
      #  age = int(input("Enter your age"))
    else:
        mobile = input("Enter your  mobile number")
        if len(mobile) !=10:
            print("you havenot enter 10digit mobile number")
            mobile = input("Enter your  mobile number")
            if mobile.isalpha()==True:
                print("do not enter alphabet")




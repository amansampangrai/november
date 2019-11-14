# write a program to take name age and mobile number from user..which should be valid.
name = input("Enter your name")
if name.isdigit()==True or len(name)<=2:
    print ("your name should be character and more than 2 digit")
else:
    age=int(input("Enter you age"))
    if age < 18:
        print("Your age should be more than 18")
    else:
        mobile=input("Enter your mobile number")
        if len(mobile)!=10 or mobile.isalpha==True:
            print("Your number should be 10 digit and should not have character")
        print("Yor name is ",name)
        print("your age is ",age)
        print("your mobile number is ",mobile)
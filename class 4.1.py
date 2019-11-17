#write a program to take name age and mobile number from user which should be valid.
name = input("Enter your name ")
while name.isalpha()==False or len(name)<3:
    name=input('Wrong !!!! Enter again')
age = input("Enter your age ")
while age.isdigit()==False or int(age)<19 or int(age)>120 :
    age=input("Input your correct age")
mobile = input("Enter your mobile number ")
while len(mobile) != 10 or mobile.isalpha == True:
    mobile = input("Enter correct mobile number")
print("Your name is ",name)
print("Your age is ",age)
print("Your mobile number is ",mobile)
#suppose your passing marks are 40, write a program to accept marks from the user and show pass or fail.
marks=int(input("enter your obtained marks"))
if marks>=40 and marks < 100:
    print("you have been passed")
elif marks>100:
    print("your input marks is wrong")
else:
    print("you have been failed")
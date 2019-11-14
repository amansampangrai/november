#write a program for grading the students based on the marks.
'''90-100-A
70-90-B
40-70-C
Below 40 - fail'''

marks = int(input("enter your obtained marks"))
if marks>0 and marks <40:
    print("you are failed")
if marks>=40 and marks <70:
        print("you have got grade c")
if marks >= 70 and marks <90:
    print("you have got grade B")
if marks >=90 and marks < 100:
    print("you have got Grade A")
if marks>100 or marks < 0:
    print("your input marks is incorrect")


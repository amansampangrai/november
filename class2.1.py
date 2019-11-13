# take five marks input from the user and then input it into the list and then print the sum of all marks.
markslist=[]        #creatring an empty list
n=int(input("enter the total subject: "))                  #number of subjects as input
for i in range(0,n):            #iterating till the range
        print("Enter number at location", i, ":")       #for loop should be in same gap
        item = int(input())
        markslist.append(item)   #adding new data
print(markslist)
print(sum(markslist))       #it will sum the marks in list

#finding the max and minimum value
maximum = max(markslist)
minimum = min(markslist)
print(maximum)
print(minimum)

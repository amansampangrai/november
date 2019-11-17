#ask the user to enter 10number using only one input statement and add them to the list.
#num=int(input("Enter the number"))
'''x = list(map(int, input("Enter a multiple value: ").split()))
print("List of students: ", x)'''

list = [int(list) for list in input("Enter multiple value: ").split()]
print("Number of list is: ", list)
even=[]
for x in list:
    if x%2==0:
        even.append(x)
print("The even number is ",even)




'''num=int(input("Enter multiple number"))
split = num.split()
print("Number of list is ",split)'''

'''name='santis my name'
print(name.split())'''

'''num=input("Enter multiple number")
print(num.split())'''

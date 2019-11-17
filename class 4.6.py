#from a list ask the user the number he wants to remove from the list and then print the list.
list = [11,42,23,14,5,16,37,8]
print(list)
num=int(input("Enter number to remove"))
for x in list:
    if x==num:

        list.pop()
print(list)
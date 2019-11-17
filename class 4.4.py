#from a list of numbers make a new list containing only the even numbers.
list = [1,2,3,4,5,6,7,8,1,2,3,1,1,1]
even=[]
for x in list:
    if x%2==0:
       even.append(x)
print("The list of even number is ",even)

list1=[1,2.0,"hi",34,11,12,13,1,0,1,0,1,1,1,7.5]    #adding some data in list1, list1 is same as array
print (list1)           #printing list1
list2=[3,4,7,2]         #adding some data in list2
print(list1+list2)      #adding string of list1 and list2 and printing it
list1.append(3)         # append is used to add the data in last place
print(list1)            #printing list1
list2.pop(1)            #pop is used to delete the data, it delete data of address 1
print(list2)            #printing list2
list2.sort()            #sort is used to arrange the data in ascending order
print(list2)            #printing lsit2
list2.sort(reverse=True)    #it will arrange the data in descending order
print(list2)            #printing list2
print(list1.count(1))       #it will count the number of 1 in list1
list1.extend(list2)     #list1  and list2 are added, list1+list2
print(list1)            #print list1
name="my name is aman"  #declaring variable name
print(name[4])      #it is used to print address 4
print(name[1:6])    #it is used to print from address 1 to 5
print(name[0: ])    #it is used to print all from variable name
print(list1[1:10:2])  # start=address1, end=address10 and jump=2

name2="sushma godawari collage"  #declaring new variable name2
print(name2)            #printing name2
#name2.pop(1)        #we cannot pop,count,extend etc in string

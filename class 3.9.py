# write a program to accept length and breadth, to check it is square of a rectangle
'''length=int(input("enter length"))
breadth=int(input("Enter breadth"))
if length == breadth:
    print("it is square")
if length != breadth:
    print("it is rectangle")'''
l1=int(input("Enter length of first side"))
l2=int(input("Enter length of second side"))
l3=int(input("Enter length of third side"))
l4=int(input("Enter length of fourth side"))
if l1!=l2 and l1!=l3 and l1!=l4 and l2!=l3 and l2!=l4 and l3!=l4:
    print("it is polygon")
if l1==l3 and l2==l4 and l1!=l2 and l3!=l4:
    print("it is rectangle")
if l1==l2==l3==l4:
    print("it is square")

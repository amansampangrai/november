# write a function to find the area of a circle . the value of the radius must be enterd by the user.
def circle():
    radius=int(input("Enter radius of the circle to find its area "))
    area=3.17*radius**2
    circumferance= 2*3.17*radius
    return area,circumferance
ar,cir=circle()
print('The area and circumferance of circle is ',ar,cir)


# write a program that uses map to convert a list of temp in ferhenheit to celcius.


'''def cube(c):
    return c**3
lst=[2,4,6,8]
lst1=list(map(cube,lst))
print(lst1)'''


'''def cube(c):
    return c**3
for num in range(10):
    num=list[num]
cube_num=list(map(cube,num))
print(cube_num)'''


'''for i in range(1,10):
    print(i,end=" ")'''


def converter(c):
    return (c*9/5)+32
temp = [32,33,34,35,36,37,38]
ferhenheit=list(map(converter,temp))
print(ferhenheit)

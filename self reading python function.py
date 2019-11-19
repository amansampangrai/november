'''def aman():
    print("Hello aman")
aman()'''
'''def add():
    num1=int(input("Enter any number"))
    num2=int(input("Enter any two number"))
    sum=num1+num2
    print(sum)
add()'''

'''def add(a):
    print(a+2)
add(3)'''


'''def address(country="Nepal"):
    print("I am from",country)
address()
address("India")'''

'''def my_function(*kids):
  print("The youngest child is " + kids[3])

my_function("Emil", "Tobias", "Linus","Aman")
def astrick_function(*a):
     print(a[1])
astrick_function(1,2,3,4,5)'''



'''def myfunction():
    print("aman")
    pass
    print("hello")
myfunction()
print("aman")'''

'''def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)'''


#python lambda

'''x = lambda a : a + 10
print(x(5))'''

'''x=lambda a,b : a*b
print(x(4,5))'''

'''x=lambda a,b,c:a*b*c
print(x(4,5,6))'''

'''def myfunc(n):
  return lambda a : a * n '''

'''def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))'''

'''def fun(n):
    return lambda a : a*n
mytripler = fun(3)
print(mytripler(11))'''



#python arrays

'''name=["aman","bibek","milan"]
print(name)'''

x=cars[0]
cars[0]="toyota"
print(x)

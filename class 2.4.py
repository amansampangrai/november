#replace a word from the string and convert the string into uppercase(). hint= use function but you need to find which one..
'''string = input ("enter any sentence")           #input string from user
string1 = input ("input some string to change")
string2= input ("input string to be replaced")
print (string.isupper())            #check whether the string is upper or not
print (string.islower())            #check whether the string is lower or not
print (string.lower())              # change string into lower
print (string.upper())              #change string into upper
print (string2.replace(string1,string2))'''
string=input("enter any sentence")
replacedword= string.replace(input("enter string to be replaced"),input("replaced by"))
print(replacedword)
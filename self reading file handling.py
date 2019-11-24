# file handling
#reading from file and printing
'''file=open("aman.txt",'r')
for a in file:
    print(a)'''



'''file=open('aman.txt','r')
print (file.read())'''





'''file=open('aman3.txt','w')
file.write("This is my first write\n")
file.write("This is my second write")
file.close()'''


'''with open("aman3.txt",'a') as file:
    file.write("\nThis is my first append using with")
    file.close()'''


# python code to illustrate split function

'''with open('aman3.txt','r') as file:
    data=file.readlines()
    for line in data:
        word=line.split()
        print(word)'''



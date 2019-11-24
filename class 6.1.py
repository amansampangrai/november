#FILE HANDLING


#this code is for writing and creating a new file
'''file=open('aman.txt','w')
file.writelines('This is my first file.\n hello world')
file.close()'''

#this is code for reading file
'''file=open('aman.txt','r')
text=file.read()
#file.close()
print(text)'''

'''with open('aman.txt','r') as file:
    text=file.read()
print(text)'''


#this is code for append text.

'''file=open('aman.txt','a')
file.writelines("\n hahahha \n banana \n cow")
file.close()'''

'''file=open('aman.txt','a')
a='hgvfhjv'
b='hgujyhvfguyhj'
c=a+b
file.writelines(c)
file.close()
'''

#code to write unlimited
'''file=open('aman1.txt','w')
text=input("write to the file... write exit to stop")
while text!='exit':
    file.write(text+'\n')
    text=input()
print("your document is saving")
file.close()'''

'''file=open('aman1.txt','w')
file.writelines("aeroplane")
file.seek(1)
file.writelines("lion")
file.close()'''

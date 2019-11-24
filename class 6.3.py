# write a program that corrects: Hello-This-is-a-text-file.


'''with open('text.txt','w+') as file:
    file.write("Hello-This-is-a-text-file.")
    file.close()
data=file.readlines()
    for line in data:
        word=line.split()
        print(word)


with open('text.txt','r') as file2:
    word=file2.read()
    for line in word:
        while line== "-":
            line == " "
            new=line
    print(new)'''


file=open("text.txt",'w+')
file.writelines("Hello-This-is-Python-class.")
text=file.readline()
text2= text.replace('-',' ')
print(text2)
file.close()

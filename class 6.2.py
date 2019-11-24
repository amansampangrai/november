# write a program that copies content of one file to another file.



with open("aman.txt") as file1:
    with open("aman1.txt", "a") as file2:
        for line in file1:
            file2.write(line)



'''with open('aman.txt','r') as file1:
    with open('aman1.txt','w') as file2:
        for line in file1:
            file2.write(line)'''
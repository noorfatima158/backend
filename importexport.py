# file handling 

a= open("testfile.txt")           # to open a file 
print(a.read())
a.close()                   #closing file

#using of with keyword
with open("testfile.txt") as a:
     print(a.read())
a.close()

a=open("testfile.txt")
print(a.read(4))           #printing first 4 characters of file 
a.close()


a=open("testfile.txt")
print(a.readline())          #will return first line of file 
a.close()

a=open("testfile.txt")
for  x in a:                    #loop through files lines
     print(x)
a.close()
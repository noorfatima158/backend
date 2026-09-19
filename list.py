x =[7,12,9,4,11]
minvalue= x[0]     #finding min value in list
for i in x:
    if i < minvalue:
        minvalue=i
print('lowest', minvalue)

x.append(3) # adding element in list 
x.remove(12) #removing element (by exact element name )
x.pop(3 )  #to remove by using index
print(x)
x.sort()    #sorting element 
print(x)

y=[1, 'hello', 3.1419,36, 8738, True]  # value of different datatype 
z=[43,48,91,31,37,28,72]
print(z)

print(z[2])                                     #accessing element in list
print(z[2:6])                              #range of index (will print 2nd , 3rd 4th and fifth element)

print(z[-1])                                 #negative indexing -1 means last element
print(z[-3])
print (z[-5:-2])                              #neagtive indexing range 

#repalcing elemnt in list 
z[3]=44
print(z[3])

#replacing three new elements with index 2 
z[2:3]=[33,43,53]
print(z)

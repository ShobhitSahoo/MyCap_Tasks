#Assigning elements to different lists
a = []
b = []
c = []

# Assigning elements to list a
a.append(5)
a.append(2)

# Assigning elements to list a
b.append(6)
b.append(7)

# Assigning elements to list a
c.append(3)
c.append(0)

print(a, b, c)

#Accessing elements from a tuple
t = (2,3,5,8,32,7,11)

print(t[2]) #will print 3rd element bcoz index starts from 0
print(t[5]) #will print 2nd element

#Deleting different dictionary elements
obj = {1:11, 2:22, 3:33, 4:44, 5:55}
obj.pop(1)  
obj.pop(3)
print(obj)
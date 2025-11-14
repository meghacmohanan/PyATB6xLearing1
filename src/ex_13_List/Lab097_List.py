my_list=[1, 2, 3]
my_list[0] ="Megha"
print(my_list)

for item in my_list:
    print(item)

for i in range(10,15):
    print(i)
#indexing
print("element at index: ", my_list[0])
#append- append object at the end of he list

my_list.append('a')
print(my_list)

my_list.append('a')
print(my_list)

#extend - Append a new list
my_list.extend([4,5])
print(my_list)

# insert()- insert an item into perticular index
my_list.insert(1,'b')
print(my_list)

my_list.insert(0,'A')
print(my_list)

#remove
my_list.remove('a')
print(my_list)

#copy
my_list_copy = my_list[:]
print(my_list_copy)

my_list_copy.remove('Megha')
print(my_list_copy)








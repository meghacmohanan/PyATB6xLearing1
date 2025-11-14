
squares= [1,4,9,16,25]
print("First", squares)

print(squares.pop())
print("Second",squares)


print(squares.pop(1))
print("Third",squares)

squares.clear()
print("Fourth",squares)


# index- (element,start,end)

numbers= [10,12,56,40,46]
print("Index:", numbers.index(40))

#count - count of perticular element


numbers= [10,98,56,40,46]
print("Count:", numbers.count(40))

#sort

numbers.sort()
print("Sorting",numbers)

# reverse - reverse the ;isy in place
numbers.reverse()
print("Reverse order",numbers)

#max(), min(),/sum

print("Maximum: ", max(numbers))
print("Minimum: ", min(numbers))
print("Average: ", sum(numbers)/len(numbers))


#slicing

print(numbers)
print(numbers[1:4])
print(numbers[-1])

print("apple" in numbers)
print(10 in numbers)

# List creation and  comprehension

l= list(range(1,5))
print(l)

# nested list
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("matrix is: ",matrix[2][2])

#del-  delete statement - deletes an element

numbers= [10,98,56,40,46]
del numbers[0]
print(numbers)






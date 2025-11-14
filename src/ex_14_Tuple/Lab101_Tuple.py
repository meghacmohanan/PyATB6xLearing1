from operator import index

cities= ("London", "New York", "Paris", "Los Angels")
print(len(cities))

print("London" in cities)
print("New" in cities)

t= (12, 34,56)
# t.append(2)- append s is not possible

env_api_urls= tuple(["abc.com/get" ,"xyz.com/post", "qa.com/put"])

print(env_api_urls)

colors= ("red", "green", "blue")
for color in colors:
    print(color)

numbers= "Megha " *3
print(numbers)
numbers= (1,2)*3
print(numbers)
print("--------------------")

nums= (1,2,2,3,2)
print(nums)
print(len(nums))
print("Total count is: ",nums.count(2))
print("index is:", nums.index(2))
print("index is:", nums.index(3))

my_list= [1,2,3,4,15]
my_tuple= tuple(my_list)
print(my_tuple)

back_to_list= list(my_tuple)
print(back_to_list)


print(max(my_list))

print(my_tuple[0:2])


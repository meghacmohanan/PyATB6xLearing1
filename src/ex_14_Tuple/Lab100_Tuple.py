
my_tuple= ("sta.com","sdet.live")
print("Tuple: ",my_tuple)
my_api_list= list(my_tuple)
my_api_list.append("2")
print("List", my_api_list)
my_tuple2= tuple(my_api_list)
print("Tuple2", my_tuple2)

API_urls= ("urls1","urls2","urls3")
print(API_urls[0])
print(API_urls[1])

print(API_urls[2])
# emply tuple and lost
t= tuple()
print(t)
li= list()
print(li)

#convertion list to tuple
t1= tuple(["Megha", "Mohanan", True])
print(t1)

hero1= ("Bats", "Bruce")
hero2= ("wonder", "Diana Prince")
new_tuple= (hero1, hero2)
print(new_tuple)
print(new_tuple[0])
print(new_tuple[1])
print(new_tuple[0][0])
print(new_tuple[1][1])
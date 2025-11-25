
keys= ["name", "age", "job"]
values= ["Megha", "32", "QA"]
my_dict = dict(zip(keys, values))
print(my_dict)
# Merge

dict1= {"a":1, "b":2}
dict2= {"c":3, "d":4}
zip_dict= dict(zip(dict1, dict2))
print(zip_dict)
merged_dict= dict1| dict2
print(merged_dict)


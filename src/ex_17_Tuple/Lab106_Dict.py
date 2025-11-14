my_dict = {
    "name": "Megha",
    "age": 22,
    "role": "QA",
    "exp": 3,
}
print(my_dict)
print(type(my_dict))
my_dict["role"] = "QA Automation"
print(my_dict)

del my_dict["age"]
print(my_dict)

for k, v in my_dict.items():
    print(k, v)

# check any value present or not
print("age" in my_dict)
print("role" in my_dict)


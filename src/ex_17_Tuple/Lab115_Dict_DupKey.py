# Remove duplicate values


my_dict= {"a":1,"b":2, "c":3, "d": 1,"e":5}
 # o/p= my_dict= {"a":1,"b":2, "c":3, "e"=5}
unique_val= set()
result= {}

for key, val in my_dict.items():
    if val not in unique_val:
        result[key] = val
        unique_val.add(val)

print(result)


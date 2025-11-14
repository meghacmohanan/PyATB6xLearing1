student_info1 = {
    "name": "Megha",
    "age": 22,
    "age":32,
    "job": "Engineer",
    "address": "KA"
                }
student_info2 = {
    "name": "Mohanan",
    "age": 22,
    "age":32,
    "job": "Engineer",
    "address": {
        "city": "San Jose",
        "state": "CA",
    }
     }

student_info3 = {
    "name": "Mohanan",
    "age": 22,
    "address": {
        "city": "Sidney",
         "state": "56"}

}

student_list= [student_info1, student_info2, student_info3]
print(student_list)
print("First Data: ",student_list[0])
print("Second Data: ",student_list[1])
print("First element: ",student_list[0]["name"])
print("Second element: ",student_list[1]["name"])
print(student_list[1]["address"]["city"])
print(student_list[1]["address"]["state"])
print(student_info3 )
print(student_list[2]["address"]["city"])




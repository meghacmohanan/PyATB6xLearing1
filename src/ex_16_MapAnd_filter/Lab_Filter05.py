from queue import PriorityQueue

# remove a empty string

name= ["QA", "Test", "" ," ","selenium"]

non_empty= list(filter(None, name))
print(non_empty)

# Can use function as well
def non_empty(x):
    if x!= "":
        return True
    return None


non_empty_list= list(filter(non_empty, name))
print(non_empty_list)
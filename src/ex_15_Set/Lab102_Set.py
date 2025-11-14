
list_of_unique_items= {1,2,2,3}
print(list_of_unique_items)

list1= [45, 33,33, 2,2]
set1= set(list1)
print(set1)

tuple2= ("Test","for","for","QA","qa")
set2= set(tuple2)
print(set2)

empty=set()
print(empty)

mixed={3, 2, "Megha",2, True}
for item in mixed:
    print(item)

mixed.add(1)
print(mixed)

mixed.add(5)
print(mixed)

mixed.remove(2)
print(mixed)

mixed1={1, 2, "Megha",2, True,False}
print(mixed1)
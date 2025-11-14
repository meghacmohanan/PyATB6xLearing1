
# union

a= {1,2,3,4}
b= {3,5,6,7}
union= a.union(b)
print(a|b)
print(union)
intersection= a.intersection(b)
print(a & b)
print(intersection)

difference= a.difference(b)
print(a - b)
print(b-a)

symmetric_difference= a.symmetric_difference(b)
print(symmetric_difference)
print(a^b)
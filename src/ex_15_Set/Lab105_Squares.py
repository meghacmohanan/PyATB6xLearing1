# squares= { x**2 for x in range(1,10) }
# print(squares)

squares= {}

for i in range(1,11):
    squares[i] =i**2
    print(squares[i])

    # frosenset- immutable set
    # A frosenset cannptn be changed after the creation

fset= frozenset([1,2,3])
print(fset)
#fset.add(4)- Attribute error









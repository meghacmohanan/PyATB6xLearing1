numbers= [1,2,3,4,5]

def even_numbers(x):
    return x % 2== 0

even_numbers= list(filter(even_numbers, numbers))
print(even_numbers)





list_student= [50, 51, 45, 55, 12]

def keep(x):
    if x>50:
        return True

all_students= list(filter(keep, list_student))
print(all_students)
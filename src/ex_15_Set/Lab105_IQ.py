# Find the first non repeated character in a string
#swiss-
s= set()
def first_no_repating(string):
    for char in string:
        if(string.count(char)==1):
            s.add(char)
            print(s)
            return char
    return None


print(first_no_repating("eewiss"))








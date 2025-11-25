
#frquency of character in string
# write a program to count the frequncy

string= input("Enter a string: ")
char_count= {}
# for char in string:
#     if char in char_count:
#         char_count[char] += 1
#     else:
#         char_count[char] = 1
# print(char_count)

#another way

# for char in string:
#     char_count[char] = char_count.get(char,0)  + 1

for char in string:
    print(f"Processing:{char}")
    print(f"Current count:{char_count.get(char,1)}")
    char_count[char] = char_count.get(char,0)  + 1
    print(f"Updated count:{char_count}")

print(char_count)

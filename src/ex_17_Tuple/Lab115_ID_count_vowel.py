# find the vowles in a string

input_string= "Hello World IO"
vowels= "aeiouAEIOU"

vowels_count= 0
result= []


for char in input_string:
    if char in vowels:
        vowels_count+=1
        result.append(char)
print(result)
print("vowels count:",vowels_count)
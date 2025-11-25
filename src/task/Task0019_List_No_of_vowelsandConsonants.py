
# Count vowels and consonants in a String

def vowels_consonant_count(text):
    vowels= "aeiouAEIOU"
    vowels_count=0
    consonants_count=0
    vowels_list=[]
    consonants_list=[]
    for char in text:
       if char in vowels:
        vowels_list.append(char)
        vowels_count+=1
       else:
        consonants_list.append(char)
        consonants_count+=1
    return vowels_count,consonants_count,vowels_list, consonants_list


input_string= input("Enter a string: ")

result_v, result_c,result_vowels,result_con = vowels_consonant_count(input_string)
print(result_v)
print(result_c)
print("Vowels are: ", result_vowels)
print("Consonants are: ",result_con)



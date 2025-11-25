
# Question - ✅Palidrome of String

def check_palindrome(text):
    text=text.replace(' ','').lower()
    return text==text[::-1]

check_text= input("Enter a string: ")
if check_palindrome(check_text):
    print("Its a palindrome.")
else:
    print("It is not a palindrome.")






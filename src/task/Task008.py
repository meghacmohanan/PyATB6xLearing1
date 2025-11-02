
"""
Write a program to check whether a web page loads withtin 3 secons
(Performance test condition)

load_time= 4.2
: ⚠️ Page load too slow-
"""

try:
    page_load_time = float(input("Enter page load time: "))
    if page_load_time < 3:
        print("load_time is 4.2")
    else:
        print("⚠️ Page load too slow")

except ValueError:
    print("Enter valid page load time")

"""
Write a program to print *

**

***

****

*****
"""


j=0
for i in range(6):
    if (i<j):
        print("* " * i, end=" \n")
        j=j+1
    i=i+1




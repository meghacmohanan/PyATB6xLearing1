
"""
Question 3 :

Simulate a page loading check using a while loop.
If page_loaded becomes True within 5 seconds, print success; else timeout.

Hint: Use a counter (like wait_time) and break condition.
"""


wait_time= int(input("Enter your wait time "))
page_load= False
while wait_time<5:
    page_load=True;
    if page_load==True and wait_time<5:
        print("Success")
        break

else:
    print("Timeout")
    wait_time+=1


"""
Question 3 :

Simulate a page loading check using a while loop.
If page_loaded becomes True within 5 seconds, print success; else timeout.

Hint: Use a counter (like wait_time) and break condition.
"""
import time
import random


wait_time= 0
page_loaded= False

def api_response():
    return random.choice([False,True])
while wait_time<5:
    page_loaded=api_response();
    if page_loaded:
        print("Page loaded successfully")
        break
    else:
        print(f"checking seconds....{wait_time+1}")
        time.sleep(wait_time)
        wait_time += 1
    if not page_loaded:
        print("Timeout!, page failed to load within 5 seconds")



"""

An API sometimes fails due to network delays.

Write a program to retry the API call 3 times until the response code becomes 200.
If it still fails after 3 tries, print a failure message.

Hint: Use a while loop with a counter.
Hint: Use a while loop with a counter.

Expected Output Example:
Attempt 1: Response 500

Attempt 2: Response 200

✅ Test Passed

"""

attempt=1;
max_attempts=3;
while attempt <=max_attempts:
    response_code = int(input("Enter your response code: "))
    if response_code ==200:
        print("✅ Test Passed")
        break
    else:
        print(f"Your attempt is {attempt}")
        if attempt == max_attempts:
            print("Sorry!, Your attempt is over")
            break
        else:
            attempt += 1
            continue






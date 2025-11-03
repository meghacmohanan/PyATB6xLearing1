
"""
Check if the user can log in based on correct username and password
username: "admin"
password: "1234"
Login successfull
other u/p - Invalid crdentilas
"""
attempts=3
while attempts > 0:
    try:
        username = input("Enter your username: ")
        password = int(input("Enter your password: "))
        if username == "admin" and password == 1234:
            print("✅ Login successful")
            break;
        else:
            attempts -= 1
            print(f"{attempts} attempts left")


    except ValueError:
        attempts -= 1
        print(f"{attempts} attempts left")
        print("password must be anumber")

if attempts == 0:
    print("🔒 Account locked! Too many failed attempts.")







print("Enter which test you want to run:n")
test_type = input("Enter the Test Type: API, UI, Performace. Security\n")

match test_type:
    case "API":
        print("We are running a Postman Testcase")
    case "UI":
        print("We are running a Selenium Testcase")
    case "Performace":
        print("We are running a Performace Testcase")
    case "Security":
        print("We are running a Security Testcase")
    case _:
        print("Invalid TestType")



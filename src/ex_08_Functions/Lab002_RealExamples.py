def validate_status_code(response_code):
    if response_code == 200:
        print("Response is success")
    else:
        print("Response is failure")

validate_status_code(200)
validate_status_code(response_code=400)
validate_status_code(int(input("Enter Response code")))
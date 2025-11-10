from functools import wraps


def add_security(fun):
    def wrapper():
        print("1. Before the function is called")
        print("2. Add Helmet, Dashcad,gloves, knee gurds")
        fun()
        print("3. After the function is called")
        print("4. Secure Driving ,Leave all the items")
    return wrapper()

@add_security
def drive_ola_scooter():
    print("Driving ola scooter")


@add_security
def drive_zypp_scooter():
    print("Driving zypp scooter")


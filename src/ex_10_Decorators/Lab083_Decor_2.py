
def decorator1(fun):
    def wrapper():
        print("Testing decorator_1")
        fun()

    return wrapper

def decorator2(fun):
    def wrapper():
        print("Testing decorator_2")
        fun()

    return wrapper



@decorator1
@decorator2
def say_hello():
    print("Hello World!!!!!!!")


say_hello()
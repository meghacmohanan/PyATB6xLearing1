import time

def print_logs(fun):
    def wrapper():
        print("Start of the logs")
        fun()
        print("End of the logs")
    return wrapper()

def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time= time.time()
        print("Start of the decorator", start_time)
        func()
        end_time = time.time()
        print("End of the decorator", end_time)
    return wrapper()

@time_decorator

def test_ui_1():
    print("Testing ui_1")
    time.sleep(1)
@print_logs
def test_ui_2():
    print("Testing ui_2")
    time.sleep(1)
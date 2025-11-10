from functools import wraps
def Before_After_test(fun):
    def wrapper():
        print("Before test")
        fun()
        print("After test")
    return wrapper()

@Before_After_test
def test_ui():
    print("Testing ui")


@Before_After_test
def test_performance():
    print("Testing performance")
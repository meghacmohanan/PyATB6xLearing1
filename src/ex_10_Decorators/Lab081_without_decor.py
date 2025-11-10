from tokenize import endpats


def start():
    print("Before Running UI Test")
    print("Start the Browser")
def stop():
    print("After Running UI Test")
    print("Stop the Browser")
def test_ui():
    print("Testing ui")


start()
test_ui()
stop()
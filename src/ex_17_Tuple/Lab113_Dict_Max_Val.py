
def max_val(dictionary):
    return max(dictionary.values())


def min_val(dictionary):
    return min(dictionary.values())

def max_keys(dictionary):
    return max(dictionary.keys())

print(max_val({"a":1, "b":3}))
print(min_val({"a":1, "b":3}))
print(max_keys({"name":1, "job":3}))
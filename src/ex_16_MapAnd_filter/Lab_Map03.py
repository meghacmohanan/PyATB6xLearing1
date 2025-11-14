response_time= [1200, 1500, 1800]

def mil_sec(x):
    return x/1000

# response_time= list(map(mil_sec, response_time))
# print(response_time)
response_time= list(map(lambda x: x/1000, response_time))
print(response_time)
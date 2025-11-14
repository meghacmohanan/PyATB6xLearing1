
test_results= ["PASS", "FAIL", "PASS", "SKIP", "PASS"]

pass_give= list(filter(lambda x: x=="PASS", test_results))
print(pass_give)
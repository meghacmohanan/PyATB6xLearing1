
"""Write a progra,, that print frpom  1 t0 100 however , 
for multiple of 3- print 3, 
 print "Fizz instead pf the number , and for multiples of 5, print ""Buzz.
 For numbers tjar are multiple of bothw 3 and 5 - print "FizzBuzz
 
 print 1 t0 100
 1. Multiple of 3- "Fizz"
 2. Multiple of 5- "Buzz
 3. Multiple of 3 and 5 "FizzBuzz"""""

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print(i, "FizzBuzz")
    elif i % 3 == 0:
        print(i, "Fizz")
    elif i % 5 == 0:
        print(i, "Buzz")
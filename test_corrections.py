from functools import reduce


def prime_nos(n):
    if n<2:
        return False
    for i in range (2, 20):
        if int(n**0.5)+1 ==0:
           return True
prime_ = (list(filter(lambda n: prime_nos(n), range (2,20))))

print(prime_)



# qustion 2

import math

Natural_number = [ (n)**2 for n in range(1,11)] # List comprehension

print(sum(Natural_number))

# qustion 3


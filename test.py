# question 1
from functools import reduce

def prime_nos(n):
    if n<2:
        return False
    for i in range (2, 20):
        if n % i ==0:
           return True
prime_ = (list(filter(lambda x: prime_nos(x), range (2,20))))

print(prime_)



# qustion 2
from functools import reduce

Natural_numbers = reduce(lambda x,y: x+(y ** 2) , range(1,11))

print(Natural_numbers)


# Question 3

words = ["hello" , "world" , "python" ]

uppercase = list(map(lambda x: x.upper(), words))

print(uppercase)


# Question 4

from functools import reduce

numbers = [4,8,2,5,10,3]

maximum = reduce(max, numbers)

print(maximum)


# Question 5

list = [(123),(321),(890),
        (456),(654),(102),
        (789),(987),(333)]

print(list)
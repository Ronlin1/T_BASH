""" NUMBER 1 """
from functools import reduce

# Define a function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Use filter and lambda to generate a list of the first 20 prime numbers
primes = list(filter(lambda x: is_prime(x), range(2, 100)))

# Use reduce to find the sum of the list of prime numbers
prime_sum = reduce(lambda x, y: x + y, primes[:20])

# Print the sum of the first 20 prime numbers
print(prime_sum)

""" NUMBER 2 """
from functools import reduce

# Define a lambda function to compute the square of a number
square = lambda x: x**2

# Use reduce and lambda to compute the sum of squares of the first 10 natural numbers
sum_of_squares = reduce(lambda x, y: x + y, map(square, range(1, 11)))

# Print the sum of squares of the first 10 natural numbers
print(sum_of_squares)

""" NUMBER 3 """
# Define a list of strings
my_strings = ["hello", "world", "py"]

# Use map and lambda to convert the strings to uppercase
uppercase_strings = list(map(lambda x: x.upper(), my_strings))

# Print the uppercase strings
print(uppercase_strings)

""" NUMBER 4 """
from functools import reduce

# Define a function to find the maximum of two numbers
def find_max(x, y):
    if x > y:
        return x
    else:
        return y

# Define a list of numbers
numbers = [4, 8, 2, 5, 10, 3]

# Use reduce and the find_max function to find the maximum value in the list
max_value = reduce(find_max, numbers)

# Print the maximum value
print(max_value)

""" NUMBER 5 """
M = [[1,2,3],
     [4,5,6],
     [7,8,9]]

MT = [[row[i] for row in M] for i in range(3)]
print(MT)

matrix_2by_2 = [[i+j for j in range(2)] for i in range(2)]
print(matrix_2by_2)

matrix_3_by_3 = [[i+j+k for k in range(3)] for j in range(3) for i in range(3)]
print(matrix_3_by_3)

#3D MATRIX
matrix_3D = [[[i+j+k for k in range(3)] for j in range(3)] for i in range(3)]
print(matrix_3D)

#4D MATRIX
matrix_4D = [[[[i+j+k+l for l in range(3)] for k in range(3)] for j in range(3)] for i in range(3)]
print(matrix_4D)

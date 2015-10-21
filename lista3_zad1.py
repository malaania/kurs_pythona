__author__ = 'malaania'
from math import sqrt
from itertools import count, islice

def is_prime(n):
    if n<2: return False
    return all(n%i for i in islice(count(2),int(sqrt(n)-1)))

def array_of_primes(n):
    return [i for i in range(0,n) if is_prime(i)]

def array_of_primes_f(n):
    return filter(is_prime,range(n))

for i in array_of_primes(25):
    print i
for i in array_of_primes_f(25):
    print i

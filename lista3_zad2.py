__author__ = 'malaania'

def is_perfect(n):
    sum = 0
    for i in xrange(1, n):
        if n % i == 0:
            sum += i
    return n == sum

perfect = lambda n: sum(i for i in xrange(1, n) if n % i == 0) == n

def array_of_perfect(n):
    return filter(perfect,range(n))

print is_perfect(28)
print is_perfect(22)
print perfect(23)
print perfect(8128)
for i in array_of_perfect(200)

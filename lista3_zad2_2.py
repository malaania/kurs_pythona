__author__ = 'malaania'
import time

def doskonale_skladana(n):
    return [i for i in range(2, n)
            if sum([j for j in range(1, i / 2 + 1) if i % j == 0]) == i]


def doskonale_funkcyjna(n):
    return filter(lambda n: sum(i for i in xrange(1, n) if n % i == 0) == n,
                  range(2, n))


print str(doskonale_skladana(1000))
print str(doskonale_funkcyjna(1000))
start = time.time()
doskonale_skladana(3000)
stop = time.time()
print "Lista skladana: "+ str(stop - start)
start = time.time()
doskonale_funkcyjna(3000)
stop = time.time()
print "Lista funkcyjna: "+ str(stop - start)



__author__ = 'malaania'

def pierwsze_skladana(n):
    zlozone = [zlozona for i in range(2, int(n**0.5)+1) for zlozona in range(i*2,n, i)]
    pierwsze = [pierwsza for pierwsza in range(2, n) if pierwsza not in zlozone]
    return pierwsze

def jest_pierwsza(n):
    return not any(n%i==0 for i in xrange(2, int(n**0.5)+1))
def pierwsze_funkcyjna(n):
    return filter(jest_pierwsza,range(2,n))

def jest_pierwsza2(n):
    return not bool(filter(lambda i: n%i == 0, range(2,int(n**0.5)+1)))
def pierwsze_funkcyjna2(n):
    return filter(jest_pierwsza2, range(2,n))


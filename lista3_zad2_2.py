__author__ = 'malaania'
import time

def pierwsze_skladana(n):
    zlozone = [zlozona for i in range(2, int(n**0.5)+1) for zlozona in range(i*2,n, i)]
    pierwsze = [pierwsza for pierwsza in range(2, n) if pierwsza not in zlozone]
    return pierwsze

start = time.time()
pierwsze_skladana(1000)
stop = time.time()
print stop - start
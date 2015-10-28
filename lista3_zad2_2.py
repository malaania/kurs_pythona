__author__ = 'malaania'

def doskonale_skladana(n):
    return [i for i in range(2, n) if sum([j for j in range(1, i/ 2 + 1) if i % j == 0]) == i]

print str(doskonale_skladana(1000))

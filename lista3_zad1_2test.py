__author__ = 'malaania'
from lista3_zad1_2 import *
import time

print str(pierwsze_skladana(30))
print str(pierwsze_funkcyjna(30))
print str(pierwsze_funkcyjna2(30))
start = time.time()
pierwsze_skladana(2000)
stop = time.time()
print "Lista skladana: "+ str(stop - start)
start = time.time()
pierwsze_funkcyjna(2000)
stop = time.time()
print "Lista funkcyjna: "+ str(stop - start)
start = time.time()
pierwsze_funkcyjna2(2000)
stop = time.time()
print "Lista funkcyjna2: "+ str(stop - start)

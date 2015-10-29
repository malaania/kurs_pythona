__author__ = 'malaania'
from lista3_zad1_2 import *
import time

class PierwszeIter:
    def __init__(self):
        self.licznik = 2
    def __next__(self):
        while 1:
            self.licznik+=1
            if not any(self.licznik%i==0 for i in xrange(2, int(self.licznik**0.5)+1)):
                return self.licznik

def pierwsze_iter(n):
    lista_pierwszych=[]
    iter = PierwszeIter()
    while iter.licznik<n:
        lista_pierwszych.append(iter.licznik)
        iter.__next__()
    return lista_pierwszych

def space_gen(n):
    space=""
    for i in range(n):
        space+=" "
    return space

def sprawdz_f(n):
    start = time.time()
    pierwsze_funkcyjna(n)
    stop = time.time()
    return str("%.4f" % (stop-start))
def sprawdz_s(n):
    start = time.time()
    pierwsze_skladana(n)
    stop = time.time()
    return str("%.4f" % (stop-start))
def sprawdz_i(n):
    start = time.time()
    pierwsze_iter(n)
    stop = time.time()
    return str("%.4f" % (stop-start))

def porownaj(lista_arg):
    dl_arg =[len(str(i)) for i in lista_arg]
    max_dl_arg = max(dl_arg)
    print space_gen(max_dl_arg)+" | funkcyjna | skladana | iterator"
    for arg in lista_arg:
        print str(arg) +" | " + sprawdz_f(arg) +" | " +sprawdz_s(arg)+" | " + sprawdz_i(arg)


porownaj([50,3100,123])
__author__ = 'malaania'
from lista3_zad1_2 import *
from itertools import islice,count
import time

class PierwszeIter:
    def __iter__(self):
        self.licznik = 2
        return self
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

def pierwsze_it():
    zlozone = {}
    yield 2
    for q in islice(count(3),0,None,2):
        p = zlozone.pop(q,None)
        if p is None:
            zlozone[q*q]=q
            yield q
        else:
            x= q + 2*p
            while x in zlozone:
                x+=2*p
            zlozone[x]=p

def pierwsze_iteracyjna(n):
    it = pierwsze_it()
    tab =[]
    temp = next(it)
    while temp<=n:
        tab.append(temp)
        temp = next(it)
    return tab

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
    pierwsze_iteracyjna(n)
    stop = time.time()
    return str("%.4f" % (stop-start))

def porownaj(lista_arg):
    max_dl = max([len(str(i)) for i in lista_arg])
    print space_gen(max_dl)+" | funkcyjna | skladana | iterator"
    for arg in lista_arg:
        print space_gen(max_dl-len(str(arg)))+str(arg) +\
              " |    " + sprawdz_f(arg) +\
              " |   " +sprawdz_s(arg)+\
              " |   " + sprawdz_i(arg)


porownaj([50,3100,123,12])
#print str(pierwsze_iteracyjna(25))
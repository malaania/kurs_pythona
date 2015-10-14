__author__ = 'malaania'
import time

class Licz():
    @classmethod
    def silnia_rek(cls, n):
        if n==1:
            return 1
        else:
            return n*Licz.silnia_rek(n-1)

    @classmethod
    def silnia_wyj(cls, n):
        wynik=1
        while n>0:
            wynik*=n
            n-=1
        raise Exception(wynik)

    @classmethod
    def fib_rek(cls, n):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return Licz.fib_rek(n-1)+Licz.fib_rek(n-2)

    @classmethod
    def fib_wyj(cls, n):
        if n==0:
            raise Exception(0)
        i=0
        przedost = 0
        wynik=1
        while i<(n-1):
            i+=1
            temp_wynik=wynik
            wynik +=przedost
            przedost=temp_wynik
        raise Exception(wynik)


print Licz.silnia_rek(5)
try:
    print Licz.silnia_wyj(5)
except Exception as e:
    print e.message

t_przed_rek = time.time()
Licz.silnia_rek(700)
t_po_rek = time.time()
print "silnia rekurencyjnie:"
print t_po_rek-t_przed_rek
t_przed_wyj = time.time()
try:
    print Licz.silnia_wyj(700)
except Exception as e:
    pass
t_po_wyj = time.time()
print "silnia z wyjatkiem:"
print t_po_wyj - t_przed_wyj
print "Liczby Fibonacciego rekurencyjnie:"
t_przed_rek = time.time()
Licz.fib_rek(20)
t_po_rek = time.time()
print(t_po_rek-t_przed_rek)
t_przed_wyj = time.time()
try:
    print Licz.fib_wyj(200)
except Exception as e:
    pass
t_po_wyj = time.time()
print "Liczby Fibonacciego z wyjatkami:"
print(t_po_wyj-t_przed_wyj)






__author__ = 'malaania'
import time
import timeit

class Licz():
    @classmethod
    def silnia_rek(cls, n):
        if n==1:
            return 1
        else:
            return n*Licz.silnia_rek(n-1)

    @classmethod
    def silnia_wyj(cls, n):
        try:
            Licz.silnia_acc(n,1)
        except Exception as e:
            return e.message

    @classmethod
    def silnia_acc(cls,n, acc):
        if n==0:
            raise Exception(acc)
        else:
            return Licz.silnia_acc(n-1,n*acc)

    @classmethod
    def fib_rek(cls, n):
        if n==0 or n==1:
            return n
        else:
            return Licz.fib_rek(n-1)+Licz.fib_rek(n-2)

    @classmethod
    def fib_wyj(cls,n):
        if n == 0:
            return 0
        else:
            try:
                Licz.fib_acc(0,1,n)
            except Exception as e:
                return e.message

    @classmethod
    def fib_acc(cls,prev,curr,n):
        if n==1:
            raise Exception(curr)
        else:
            Licz.fib_acc( curr, curr+prev,n-1)

print Licz.silnia_wyj(5)
print Licz.silnia_rek(5)
print Licz.fib_rek(7)
print Licz.fib_wyj(7)
t_przed = time.time()
for i in range(0,1000):
    Licz.silnia_rek(50)
t_po = time.time()
print "Silnia rekurencyjna: " + (t_po-t_przed).__str__()
t_przed = time.time()
for i in range(0,1000):
    Licz.silnia_wyj(50)
t_po = time.time()
print "Silnia z wyjatkiem: " + (t_po-t_przed).__str__()
t_przed = time.time()
for i in range(0,1000):
    Licz.fib_rek(15)
t_po = time.time()
print "Fibonacci rekurencyjnie: " + (t_po-t_przed).__str__()
t_przed = time.time()
for i in range(0,1000):
    Licz.fib_wyj(15)
t_po = time.time()
print "Fibonacci z wyjatkiem: " + (t_po-t_przed).__str__()






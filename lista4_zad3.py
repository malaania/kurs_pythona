__author__ = 'malaania'
from itertools import imap
import collections

class PrzetwarzajStrumien():

    def __init__(self,zrodlo):
        f = self.open_file(zrodlo)
        self.linie = f.readlines()
        self.licznik = 0

    def open_file(self,zrodlo):
        try:
            f = open(zrodlo,'r')
        except IOError:
            f=None
            print "File you are trying to open does not exist"
        return f


    def __iter__(self):
        return self

    def next(self):
        if self.licznik<len(self.linie):
            i = self.licznik
            self.licznik+=1
            return self.linie[i]
        else:
            raise StopIteration()

def korekta(zdanie):
    zdanie = zdanie.strip()
    if(zdanie[len(zdanie)-1]!="."):
        zdanie +="."
    return zdanie.capitalize()

def koryguj_strumien(iter):
    return imap(korekta,iter)

#ps = PrzetwarzajStrumien("/home/malaania/Documents/text")
#print isinstance(ps, collections.Iterable)
#print "|"+korekta("ania lalalalala    \n")+"|"
#for i in koryguj_strumien(ps):
#    print i
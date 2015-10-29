__author__ = 'malaania'
from itertools import imap

class PrzetwarzajStrumien():
    def __init__(self,zrodlo):
        f = open(zrodlo,'r')
        self.linie = f.readlines()
        self.licznik = 0
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
    zdanie = zdanie.rstrip()
    if(zdanie[len(zdanie)-1]!="."):
        zdanie +="."
    return zdanie.capitalize()

def koryguj_strumien(iter):
    return imap(korekta,iter)

ps = PrzetwarzajStrumien("/home/malaania/Documents/text")
print "|"+korekta("ania lalalalala    \n")+"|"
for i in koryguj_strumien(ps):
    print i
__author__ = 'malaania'
class PierwszeIter:
    def __init__(self):
        self.licznik = 1
    def __next__(self):
        self.licznik+=1
        while 1:
            for i in range(1, int(self.licznik**0.5)+1):
                if(self.licznik%i==0):
                    break
            else:
                break
        return self.licznik
class PierwszeKolekcja:
    def __iter__(self):
        return PierwszeIter()

pierwsze = PierwszeIter()
print pierwsze.__next__()
__author__ = 'malaania'
class ObiektyDodawalne:
    def __add__(self, other):
        if isinstance(other,ObiektyDodawalne) or issubclass(type(other),ObiektyDodawalne):
            wszystkie_pola = self.__dict__.copy()
            for key, value in other.__dict__.iteritems():
                if key in self.__dict__:
                    print ("Ta sama nazwa pola! Z dwoch wartosci <%s, %s> wybrano <%s> " % (self.__dict__[key],other.__dict__[key], self.__dict__[key]))
                else:
                    wszystkie_pola[key]=value
            polaczona_klasa = ObiektyDodawalne()
            for key, value in wszystkie_pola.iteritems():
                setattr(polaczona_klasa, key, value)
            return polaczona_klasa
        else:
            raise TypeError("Proba dodania obiektu niedodawalnej klasy!")

class PunktDodawalny(ObiektyDodawalne):
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z

class KoloDodawalne(ObiektyDodawalne):
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r

class Niedodawalna:
    def __init__(self,x):
        self.x=x

punkt = PunktDodawalny(1,2,3)
kolo = KoloDodawalne(4,5,7)
print (punkt + kolo).__dict__
cos_tam = Niedodawalna(12)
kolo + cos_tam





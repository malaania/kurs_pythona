from itertools import imap

# Class that reads from the stream.
class PrzetwarzajStrumien():

    def __init__(self, zrodlo):
        f = self.open_file(zrodlo)
        self.linie = f.readlines()
        self.licznik = 0

    def open_file(self, zrodlo):
        """
        Opens a file specified in the path.
        :param zrodlo: path to the file
        :return: opened file or None
        """
        try:
            f = open(zrodlo, 'r')
        except IOError:
            f = None
            print "File you are trying to open does not exist."
        return f

    def __iter__(self):
        return self

    def next(self):
        """
        :return: next element of the iterator
        """
        if self.licznik < len(self.linie):
            i = self.licznik
            self.licznik += 1
            return self.linie[i]
        else:
            raise StopIteration()


def korekta(zdanie):
    """
    This functions checks if sentences have a correct form.
    Correct sentence should start with capital letter and end
    with a dot.
    :rtype: String
    :param zdanie: sentence as a String
    :return: sentence as a String, capitalized, with dot in the end
    """
    zdanie = zdanie.strip()
    if (zdanie[len(zdanie) - 1] != "."):
        zdanie += "."
    return zdanie.capitalize()

def koryguj_strumien(iter):
    """
    This function corrects all the sentences in the iterator.
    :param iter: not corrected iterator
    :return: iterator with correct sentences
    """
    return imap(korekta, iter)

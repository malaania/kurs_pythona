#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import sys
from zad8_kontakt import Kontakt

def checkTableExists(dbcon, tablename):
    dbcur = dbcon.cursor()
    dbcur.execute("""
        SELECT COUNT(*)
        FROM information_schema.tables
        WHERE table_name = '{0}'
        """.format(tablename.replace('\'', '\'\'')))
    if dbcur.fetchone()[0] == 1:
        dbcur.close()
        return True

    dbcur.close()
    return False

class BazaKontaktow():

    def __init__(self):
        self.con = mdb.connect('localhost', 'testuser', 'blabla11hop', 'testdb')
        with self.con:
            self.cur = self.con.cursor()
            if not checkTableExists(self.con, "Kontakty"):
                self.cur.execute('''CREATE TABLE Kontakty(
                    Id INTEGER PRIMARY KEY AUTO_INCREMENT,
                    Nazwa VARCHAR(50),
                    Nr_tel VARCHAR(15),
                    Mail VARCHAR(50),
                    Ostatnie_wyswietlenie DATE)''')
            self.kontakty = []
            self.cur.execute("SELECT * FROM Kontakty");
            for i in range(self.cur.rowcount):
                row = self.cur.fetchone()
                self.kontakty.append(Kontakt(row[0],row[1],row[2],row[3],row[4]))

    def display_all_contacts(self):
        for kontakt in self.kontakty:
            print "Kontakt "+ kontakt.id
            print kontakt.nazwa
            print kontakt.nr_tel
            print kontakt.mail
            print kontakt.ostatnie_wyswietlenie

    def add_contact(self, nazwa, nr, mail):
        



baza =  BazaKontaktow()

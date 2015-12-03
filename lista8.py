#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import time
from lista8_kontakt import Kontakt

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
            self.update_contacts()

    def update_contacts(self):
        self.kontakty = []
        self.cur.execute("SELECT * FROM Kontakty");
        for i in range(self.cur.rowcount):
            row = self.cur.fetchone()
            self.kontakty.append(Kontakt(row[0],row[1],row[2],row[3],row[4]))

    def display_all_contacts(self):
        for kontakt in self.kontakty:
            print "Kontakt "+ str(kontakt.id)
            print kontakt.nazwa
            print kontakt.nr_tel
            print kontakt.mail
            print kontakt.ostatnie_wyswietlenie
            print ""

    def add_contact(self, nazwa, nr, mail):
        self.cur.execute(
            "INSERT INTO Kontakty(Nazwa,Nr_tel,Mail,Ostatnie_wyswietlenie) "
            "VALUES(%s,%s,%s,%s)",
            (nazwa,nr,mail,time.strftime('%Y-%m-%d')))
        self.con.commit()
        self.update_contacts()

    def delete_contact(self,id):
        self.cur.execute("DELETE FROM Kontakty WHERE Id=%s",id)
        self.con.commit()
        self.update_contacts()

    def update_contact(self,id,new_contact):
        pass

    def update_last_view(self,id):
        self.cur.execute(
            "UPDATE Kontakty SET Ostatnie_wyswietlenie=%s WHERE Id=%s",
            (time.strftime('%Y-%m-%d'),id))
        self.con.commit()
        self.update_contacts()

    def end_connection(self):
        self.con.close()
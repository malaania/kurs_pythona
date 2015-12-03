import gtk
from lista8 import BazaKontaktow

# INSERT INTO Kontakty(Nazwa,Nr_tel,Mail,Ostatnie_wyswietlenie)
# VALUES("Bla bla bla","12134","ho@ho.hu","1999-11-09");

class MyContactWindow(gtk.Window):
    def __init__(self,name,number,mail):
        gtk.Window.__init__(self)
        self.set_default_size(600,100)
        k_box = gtk.HBox()
        self.add(k_box)
        text = "        "+name+ "           Nr telefonu:  "+number+"             E-mail:  "+mail
        k_label=gtk.Label(text)
        k_box.pack_start(k_label,False,False,0)
        k_box.show()


class MyEditWindow(gtk.Window):
    def __init__(self,id,name,number,mail):
        gtk.Window.__init__(self)
        self.set_default_size(600,100)
        editContactBox= gtk.HBox()
        self.add(editContactBox)

        nameLabel= gtk.Label('Nazwa:')
        nameEntry = gtk.Entry()
        nameEntry.set_text(name)
        numberLabel= gtk.Label('Nr. tel:')
        numberEntry = gtk.Entry()
        numberEntry.set_text(number)
        mailLabel= gtk.Label('E-mail:')
        mailEntry= gtk.Entry()
        mailEntry.set_text(mail)
        buttonAddContact=gtk.Button("Zapisz zmiany")
        editContactBox.pack_start(nameLabel,False,False,0)
        editContactBox.pack_start(nameEntry,False,False,0)
        editContactBox.pack_start(numberLabel,False,False,0)
        editContactBox.pack_start(numberEntry,False,False,0)
        editContactBox.pack_start(mailLabel,False,False,0)
        editContactBox.pack_start(mailEntry,False,False,0)
        editContactBox.pack_start(buttonAddContact,False,False,0)

        editContactBox.show()



class MyWindow(gtk.Window):

    def addContact(self,widget,nameEntry,numberEntry,mailEntry):
        name = nameEntry.get_text()
        number = numberEntry.get_text()
        mail = mailEntry.get_text()
        print name
        print number
        print mail
        self.baza_kontaktow.add_contact(name,number,mail)
        nameEntry.set_text("")
        numberEntry.set_text("")
        mailEntry.set_text("")

    def openContact(self,widget,id,name,number,mail):
        self.baza_kontaktow.update_last_view(id)
        win = MyContactWindow(name,number,mail)
        win.connect("delete-event", gtk.main_quit)
        win.show_all()
        gtk.main()

    def removeContact(self,widget,id):
        self.baza_kontaktow.delete_contact(id)

    def editContact(self,widget,id,name,number,mail):
        win = MyContactWindow(id,name,number,mail)

    def __init__(self):
        gtk.Window.__init__(self)
        self.set_default_size(600,250)
        self.baza_kontaktow = BazaKontaktow()

        # VBox z lista kontaktow
        box = gtk.VBox()
        self.add(box)

        for kontakt in self.baza_kontaktow.kontakty:
            k_box = gtk.HBox()
            k_label = gtk.Label(kontakt.nazwa)
            k_label.set_width_chars(35)
            k_label.set_alignment(xalign=0,yalign=0.2)
            open_button = gtk.Button("Otworz kontakt")
            open_button.connect("clicked",self.openContact,kontakt.id,
                                kontakt.nazwa,kontakt.nr_tel,kontakt.mail)
            update_button= gtk.Button("Edytuj kontakt")
            update_button.connect("clicked",self.editContact,kontakt.id,
                                kontakt.nazwa,kontakt.nr_tel,kontakt.mail)
            remove_button= gtk.Button("Usun kontakt")
            remove_button.connect("clicked", self.removeContact,kontakt.id)
            k_box.pack_start(k_label,False,False,0)
            k_box.pack_start(open_button,False,False,0)
            k_box.pack_start(remove_button,False,False,0)
            box.pack_start(k_box,False,False,0)

        #HBox z dodawaniem kontaktow
        addContactBox= gtk.HBox()
        nameLabel= gtk.Label('Nazwa:')
        nameEntry = gtk.Entry()
        numberLabel= gtk.Label('Nr. tel:')
        numberEntry = gtk.Entry()
        mailLabel= gtk.Label('E-mail:')
        mailEntry= gtk.Entry()
        buttonAddContact=gtk.Button("Dodaj kontakt")
        addContactBox.pack_start(nameLabel,False,False,0)
        addContactBox.pack_start(nameEntry,False,False,0)
        addContactBox.pack_start(numberLabel,False,False,0)
        addContactBox.pack_start(numberEntry,False,False,0)
        addContactBox.pack_start(mailLabel,False,False,0)
        addContactBox.pack_start(mailEntry,False,False,0)
        addContactBox.pack_start(buttonAddContact,False,False,0)
        box.pack_start(addContactBox,False,False,0)
        buttonAddContact.connect("clicked", self.addContact,nameEntry,numberEntry,mailEntry)






if __name__=="__main__":
    win = MyWindow()
    win.connect("delete-event", gtk.main_quit)
    win.show_all()
    gtk.main()
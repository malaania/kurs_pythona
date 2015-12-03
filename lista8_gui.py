import gtk
from lista8 import BazaKontaktow

# INSERT INTO Kontakty(Nazwa,Nr_tel,Mail,Ostatnie_wyswietlenie)
# VALUES("Bla bla bla","12134","ho@ho.hu","1999-11-09");

class MyNotUsedContactsWindow(gtk.Window):
    def __init__(self,notUsedList):
        gtk.Window.__init__(self)
        self.set_default_size(100,600)
        k_box = gtk.VBox()
        self.add(k_box)
        list = gtk.List()
        k_box.pack_start(list,False,False,0)
        list.append_items([gtk.ListItem(kontakt.nazwa)for kontakt in notUsedList])
        list.show()

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

    def saveChanges(self,widget,nameEntry,numberEntry,mailEntry):
        baza = BazaKontaktow()
        baza.delete_contact(self.id)
        baza.add_contact(nameEntry.get_text(),
                         numberEntry.get_text(),
                         mailEntry.get_text())

    def __init__(self,id,name,number,mail):
        self.id =id
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
        buttonSaveChanges=gtk.Button("Zapisz zmiany")
        buttonSaveChanges.connect("clicked",self.saveChanges,nameEntry,numberEntry,mailEntry)
        editContactBox.pack_start(nameLabel,False,False,0)
        editContactBox.pack_start(nameEntry,False,False,0)
        editContactBox.pack_start(numberLabel,False,False,0)
        editContactBox.pack_start(numberEntry,False,False,0)
        editContactBox.pack_start(mailLabel,False,False,0)
        editContactBox.pack_start(mailEntry,False,False,0)
        editContactBox.pack_start(buttonSaveChanges,False,False,0)

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

    def displayNotUsed(self,widget):
        win = MyNotUsedContactsWindow(self.baza_kontaktow.nie_uzywane)
        win.connect("delete-event", gtk.main_quit)
        win.show_all()
        gtk.main()

    def editContact(self,widget,id,name,number,mail):
        win = MyEditWindow(id,name,number,mail)
        win.connect("delete-event", gtk.main_quit)
        win.show_all()
        gtk.main()
        self.baza_kontaktow.update_contacts()

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
            edit_button= gtk.Button("Edytuj kontakt")
            edit_button.connect("clicked",self.editContact,kontakt.id,
                                kontakt.nazwa,kontakt.nr_tel,kontakt.mail)
            remove_button= gtk.Button("Usun kontakt")
            remove_button.connect("clicked", self.removeContact,kontakt.id)
            k_box.pack_start(k_label,False,False,0)
            k_box.pack_start(open_button,False,False,0)
            k_box.pack_start(edit_button,False,False,0)
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

        notUsedBox = gtk.HBox()
        notUsedButton=gtk.Button("Wyswietl nie uzywane od ponad roku kontakty")
        notUsedButton.connect("clicked", self.displayNotUsed)
        notUsedBox.pack_start(notUsedButton,False,False,0)
        box.pack_start(notUsedBox,False,False,0)


if __name__=="__main__":
    win = MyWindow()
    win.connect("delete-event", gtk.main_quit)
    win.show_all()
    gtk.main()
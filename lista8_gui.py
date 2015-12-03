import gtk
from lista8 import BazaKontaktow

class MyWindow(gtk.Window):

    def addContact(self,widget,nameEntry,numberEntry,mailEntry):
        name = nameEntry.get_text()
        number = numberEntry.get_text()
        mail = mailEntry.get_text()
        print name
        print number
        print mail
        self.baza_kontaktow.add_contact(name,number,mail)

    def updateContactList(self):
        

    def __init__(self):
        gtk.Window.__init__(self)
        self.set_default_size(600,250)
        self.baza_kontaktow = BazaKontaktow()

        # VBox z lista kontaktow
        box = gtk.VBox()
        self.add(box)
        self.contact_list = gtk.List()
        box.add(self.contact_list)
        self.contact_list.show()
        self.contact_list.append_items([gtk.ListItem(kontakt.nazwa)
                                   for kontakt in  BazaKontaktow().kontakty])
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
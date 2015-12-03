import gtk
from lista8 import BazaKontaktow

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

    def getSelection(self,widget,list):
        selection = list.get_selection()
        print selection

    def openContact(self,widget,name,number,mail):
        self.baza_kontaktow
        win = MyContactWindow(name,number,mail)
        win.connect("delete-event", gtk.main_quit)
        win.show_all()
        gtk.main()


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
            open_button.connect("clicked",self.openContact,
                                kontakt.nazwa,kontakt.nr_tel,kontakt.mail)
            remove_button= gtk.Button("Usun kontakt")
            k_box.pack_start(k_label,False,False,0)
            k_box.pack_start(open_button,False,False,0)
            k_box.pack_start(remove_button,False,False,0)
            box.pack_start(k_box,False,False,0)
        #self.contact_list = gtk.List()
        #box.add(self.contact_list)
        #self.contact_list.show()
        #self.contact_list.append_items([gtk.ListItem(kontakt.nazwa)
        #                           for kontakt in  BazaKontaktow().kontakty])
        #self.contact_list.connect("selection_changedBazaKontaktow", self.getSelection,self.contact_list)

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
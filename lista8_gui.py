import gtk
from lista8 import BazaKontaktow

class MyWindow(gtk.Window):

    def __init__(self):
        gtk.Window.__init__(self)
        self.set_default_size(600,250)
        self.baza_kontaktow = BazaKontaktow()
        box = gtk.VBox()
        self.add(box)
        contact_list = gtk.List()
        box.add(contact_list)
        contact_list.show()
        contact_list.append_items([gtk.ListItem(kontakt.nazwa) for kontakt in  BazaKontaktow().kontakty])



if __name__=="__main__":
    win = MyWindow()
    win.connect("delete-event", gtk.main_quit)
    win.show_all()
    gtk.main()
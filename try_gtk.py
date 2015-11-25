import pygtk
import gtk, gobject, cairo

class Screen(gtk.DrawingArea):

    __gsignals__ = {"expose-event":"override"}

    def do_expose_event(self, event):
        cr = self.window.cairo_create()
        cr.rectangle(event.area.x, event.area.y,
                     event.area.width, event.area.height)
        cr.clip
        self.draw(cr, *self.window.get_size())

    def draw(self,cr, width, height):
        cr.set_source_rgb(0,0,0.5)
        cr.rectangle(0,0,width,height)
        cr.fill()

def run(Widget):
    window = gtk.Window()
    window.connect("delete-event",gtk.main_quit)
    widget = Widget()
    widget.show()
    window.add(widget)
    window.present()
    gtk.main()

if __name__=="__main__":
    run(Screen)
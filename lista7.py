import pygtk
import gtk, gobject, cairo
from math import radians, tan


class TurtleDrawingArea(gtk.DrawingArea):
    __gsignals__ = {"expose-event":"override"}

    def do_expose_event(self, event):
        cr = self.window.cairo_create()
        cr.rectangle(event.area.x, event.area.y,
                     event.area.width, event.area.height)
        cr.clip
        self.draw(cr, 30,220, *self.window.get_size())

    def draw(self,cr,angle, target_dist, width, height ):
        cr.set_source_rgb(0.5, 0.5, 0.5)
        cr.rectangle(0, 0, width, height)
        cr.fill()

        # draw a rectangle
        cr.set_source_rgb(1.0, 1.0, 1.0)
        cr.rectangle(10, 10, width-20, height - 20)
        cr.fill()

        # draw lines
        cr.set_source_rgb(0.0, 0.0, 0.8)
        cr.move_to(20, height-10)
        cr.rel_line_to(60, -60*tan(radians(angle)))
        cr.move_to(10, height-10)
        cr.rel_line_to(60, -60*tan(radians(angle)))
        cr.stroke()

        #draw target
        cr.set_source_rgb(1.0,0.0,0.0)
        cr.move_to(target_dist,height)
        cr.rel_line_to(0, -20)
        cr.move_to(target_dist-10,height-10)
        cr.rel_line_to(20,0)
        #cr.rel_line_to(0, height / 6.0)
        cr.stroke()



class MyWindow(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)

        self.box = gtk.HBox()
        self.add(self.box)


        self.turtle_area = TurtleDrawingArea()
        self.box.pack_start(self.turtle_area, True,True, 0)
        #self.button_go=gtk.Button("Go")
        #self.box.pack_start(self.button_go,False,False,0)


if __name__=="__main__":
    win = MyWindow()
    win.connect("delete-event", gtk.main_quit)
    win.show_all()
    gtk.main()
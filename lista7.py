import pygtk
import gtk, gobject, cairo
from math import radians, tan
import random



class TurtleDrawingArea(gtk.DrawingArea):

    __gsignals__ = {"expose-event":"override"}

    def do_expose_event(self, event):
        self.cr = self.window.cairo_create()
        self.cr.rectangle(event.area.x, event.area.y,
                     event.area.width, event.area.height)
        self.cr.clip
        if(hasattr(self,'angle') and hasattr(self,'velocity')):
            self.draw(self.cr, self.angle,self.velocity, *self.window.get_size())
        else:
            self.draw(self.cr, 30,0, *self.window.get_size())

    def shoot(self,button,angle,velocity):
        self.angle=angle
        self.velocity=velocity
        self.queue_clear()
        #print "hello"

    def draw(self,cr,angle,velocity, width, height ):
        cr.set_source_rgb(0.5, 0.5, 0.5)
        cr.rectangle(0, 0, width, 200)
        cr.fill()

        # draw a rectangle
        cr.set_source_rgb(1.0, 1.0, 1.0)
        cr.rectangle(10, 10, width-20, 180)
        cr.fill()

        # draw lines
        cr.set_source_rgb(0.0, 0.0, 0.8)
        cr.move_to(20, 190)
        cr.rel_line_to(60, -60*tan(radians(angle)))
        cr.move_to(10, 190)
        cr.rel_line_to(60, -60*tan(radians(angle)))
        cr.stroke()

        #draw target
        target_dist = random.randint(100,300)
        cr.set_source_rgb(1.0,0.0,0.0)
        cr.move_to(target_dist,200)
        cr.rel_line_to(0, -20)
        cr.move_to(target_dist-10,190)
        cr.rel_line_to(20,0)
        cr.stroke()





class MyWindow(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)

        self.box = gtk.VBox()
        self.add(self.box)


        self.turtle_area = TurtleDrawingArea()
        self.box.pack_start(self.turtle_area, True,True, 0)

        self.optBox1= gtk.HBox()
        self.entry_angle= gtk.Entry()
        self.label_angle = gtk.Label("Angle")
        self.label_velocity = gtk.Label("Velocity")
        self.entry_velocity=gtk.Entry()
        self.optBox1.pack_start(self.label_angle,False,False,0)
        self.optBox1.pack_start(self.entry_angle,False,False,0)
        self.optBox1.pack_start(self.label_velocity,False,False,0)
        self.entry_angle.show()
        self.optBox1.pack_start(self.entry_velocity,False,False,0)
        self.entry_velocity.show()

        self.button_target=gtk.Button("Go!")
        self.button_target.connect("clicked", self.turtle_area.shoot,60,60)
        self.optBox1.pack_start(self.button_target,False,False,0)
        self.box.pack_start(self.optBox1,False,False,0)


if __name__=="__main__":
    win = MyWindow()
    win.connect("delete-event", gtk.main_quit)
    win.show_all()
    gtk.main()
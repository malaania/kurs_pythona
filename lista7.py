import pygtk
import gtk, gobject, cairo
from math import radians, tan, sin, cos
import random

def calc_y(x,alpha,v):
    return x*tan(radians(alpha))-10*x*x/(2*v*v*cos(radians(alpha))*cos(radians(alpha)))

class TurtleDrawingArea(gtk.DrawingArea):

    def __init__(self):
        gtk.DrawingArea.__init__(self)
        self.target_dist = random.randint(100,300)
        self.angle = 30.0
        self.velocity = 0

    __gsignals__ = {"expose-event":"override"}

    def do_expose_event(self, event):
        self.cr = self.window.cairo_create()
        self.cr.rectangle(event.area.x, event.area.y,
                     event.area.width, event.area.height)
        self.cr.clip
        if(hasattr(self,'angle') and hasattr(self,'velocity')):
            self.draw(self.cr, self.angle,self.velocity, *self.window.get_size())
        else:
            self.draw(self.cr, self.angle,self.velocity, *self.window.get_size())

    def shoot(self,button):
        self.queue_clear()

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
        cr.set_source_rgb(1.0,0.0,0.0)
        cr.move_to(self.target_dist,200)
        cr.rel_line_to(0, -20)
        cr.move_to(self.target_dist-10,190)
        cr.rel_line_to(20,0)
        cr.stroke()


        if(self.velocity!=0):
            #where the bullet hit
            cr.set_source_rgb(0.0,0.5,0.0)
            shot = 15 + self.velocity*self.velocity*sin(radians(2*self.angle))/10
            cr.move_to(shot,200)
            cr.rel_line_to(0, -20)
            cr.move_to(shot-10,190)
            cr.rel_line_to(20,0)
            cr.stroke()
            #trajectory
            x = shot - 15
            x10 = x/10
            x_sum=x10
            #print x10
            #print shot
            trjct_x = []
            while x_sum<x:
                trjct_x.append(x_sum)
                x_sum += x10
            trjct_y = [calc_y(x,self.angle,self.velocity) for x in trjct_x]
            #print len(trjct_x)
            for i in range(len(trjct_x)):
                #print str(trjct_x[i]) +" "+str(trjct_y[i])
                if trjct_y[i]<0 :
                    print "hello"
                    break
                cr.set_source_rgb(0.0,0.5,0.0)
                cr.move_to(trjct_x[i]+15,190-trjct_y[i])
                cr.rel_line_to(2,2)
                cr.stroke()






class MyWindow(gtk.Window):

    def angle_callback(self,widget,entry):
        angle = entry.get_text()
        self.turtle_area.angle = float(angle)
        print "You set an angle to " + angle +" degrees."

    def velocity_callback(self,widget,entry):
        velocity = entry.get_text()
        self.turtle_area.velocity = float(velocity)
        print "You set an velocity to " + velocity + " m/s."

    def __init__(self):
        gtk.Window.__init__(self)
        self.set_default_size(600,250)
        self.box = gtk.VBox()
        self.add(self.box)

        self.turtle_area = TurtleDrawingArea()
        self.box.pack_start(self.turtle_area, True,True, 0)

        self.optBox1= gtk.HBox()
        self.entry_angle= gtk.Entry()
        self.btn_angle = gtk.Button("Set angle")
        self.btn_velocity = gtk.Button("Set velocity")
        self.entry_velocity=gtk.Entry()
        self.entry_angle.set_text("30")
        self.entry_velocity.set_text("0")
        #self.entry_angle.connect("activate",self.angle_callback, self.entry_angle)
        #self.entry_velocity.connect("activate", self.velocity_callback, self.entry_velocity)

        self.optBox1.pack_start(self.btn_angle,False,False,0)
        self.optBox1.pack_start(self.entry_angle,False,False,0)
        self.optBox1.pack_start(self.btn_velocity, False, False, 0)
        self.entry_angle.show()
        self.optBox1.pack_start(self.entry_velocity,False,False,0)
        self.entry_velocity.show()

        self.button_target=gtk.Button("Go!")
        self.button_target.connect("clicked", self.turtle_area.shoot)
        self.btn_angle.connect("clicked",self.angle_callback,self.entry_angle)
        self.btn_velocity.connect("clicked",self.velocity_callback,self.entry_velocity)
        self.optBox1.pack_start(self.button_target,False,False,0)
        self.box.pack_start(self.optBox1,False,False,0)




if __name__=="__main__":
    win = MyWindow()
    win.connect("delete-event", gtk.main_quit)
    win.show_all()
    gtk.main()
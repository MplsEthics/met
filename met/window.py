"""
window.py
"""

import pygtk
pygtk.require('2.0')
import gtk
from met import version
from met.view import Splash

class Main(gtk.Window):
    def __init__(self):
        gtk.Window.__init__(self)
        self.set_title("Minneapolis Ethics Training v%s" % version)
        self.set_default_size(800, 600)
        self.set_border_width(0)
        self.connect("delete-event", gtk.main_quit)
        Splash(self)
        gtk.main()


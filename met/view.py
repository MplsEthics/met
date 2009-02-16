"""
view.py - contains the various page views
"""

import pygtk
pygtk.require('2.0')
import gtk
import pango
from gtk.gdk import color_parse

blue = color_parse("#b0cfee")

UI = """
<ui>
<menubar name='MenuBar'>
    <menu action='FileMenu'>
        <menuitem action='New'/>
        <menuitem action='Open'/>
        <menuitem action='Save'/>
        <menuitem action='SaveAs'/>
        <separator/>
        <menuitem action='Quit'/>
    </menu>
    <separator/>
    <menu action='HelpMenu'>
        <menuitem action='About'/>
    </menu>
</menubar>
"""

def create_tag_table():
    """
    Create a "tag table", which contains named document style definitions.
    """
    ttt = gtk.TextTagTable()

    tag = gtk.TextTag("center")
    tag.set_property("justification",gtk.JUSTIFY_CENTER)
    ttt.add(tag)

    tag = gtk.TextTag("heading")
    tag.set_property("weight",pango.WEIGHT_BOLD)
    tag.set_property("size",15 * pango.SCALE)
    ttt.add(tag)

    return ttt

tag_table = create_tag_table()

class Splash(object):

    def __init__(self,win):
        buffer = gtk.TextBuffer(table=tag_table)
        view = gtk.TextView(buffer);
        view.modify_bg(gtk.STATE_NORMAL,blue)
        view.modify_base(gtk.STATE_NORMAL,blue)
        #win.modify_bg(gtk.STATE_NORMAL,blue)
        view.set_editable(False)
        view.set_cursor_visible(False)
        self.insert_text(view.get_buffer())

        # create a scrolled window
        sw = gtk.ScrolledWindow()
        sw.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        sw.add(view)

        # create a button too
        button = gtk.Button("exit")

        win.add(sw)
        win.add(button)
        win.show_all()

    def insert_text(self,buffer):
        iter = buffer.get_iter_at_offset(0)

        buffer.insert_with_tags_by_name(iter,
            "\n\n\nMinneapolis Ethics Training\n\n\n", "heading", "center")

        buffer.insert_with_tags_by_name(iter,
            "Ethics training software for the City of Minneapolis",
            "center")


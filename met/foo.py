"""
splash.py - the splash page
"""

import pygtk
pygtk.require('2.0')
import gtk

class SplashPage(gtk.Window):
    def __init__(self, parent=None):
        # Create the toplevel window
        gtk.Window.__init__(self)
        try:
            self.set_screen(parent.get_screen())
        except AttributeError:
            self.connect('destroy', lambda *w: gtk.main_quit())

        self.set_title(self.__class__.__name__)
        self.set_default_size(800, 600)
        self.set_border_width(0)

        # XXX what is this?
        vpaned = gtk.VPaned()
        vpaned.set_border_width(5)
        self.add(vpaned)

        # For convenience, we just use the autocreated buffer from
        # the first text view; you could also create the buffer
        # by itself with gtk.text_buffer_new(), then later create
        # a view widget.

        view1 = gtk.TextView();
        buffer_1 = view1.get_buffer()
        view2 = gtk.TextView(buffer_1)      # XXX huh?

        # create the first scrolled window
        sw = gtk.ScrolledWindow()
        sw.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        vpaned.add1(sw)
        sw.add(view1)

        # create the second scrolled window
        #sw = gtk.ScrolledWindow()
        #sw.set_shadow_type(gtk.SHADOW_ETCHED_IN)
        #sw.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)
        #vpaned.add2(sw)
        #sw.add(view2)

        #self.create_tags(buffer_1)      # XXX wtf
        self.insert_text(buffer_1)

        #self.attach_widgets(view1)
        #self.attach_widgets(view2)
        self.win = None     # XXX wtf
        self.show_all()

    def insert_text(self, text_buffer):
        # use the current directory for the file
        #try:
        #    pixbuf = gtk.gdk.pixbuf_new_from_file(GTKLOGO_IMAGE)
        #except gobject.GError, error:
        #    sys.exit("Failed to load image file gtk-logo-rgb.gif\n")

        #scaled = pixbuf.scale_simple(32, 32, 'bilinear')
        #pixbuf = scaled

        # get start of buffer; each insertion will revalidate the
        # iterator to point to just after the inserted text.
        iter = text_buffer.get_iter_at_offset(0)

        text_buffer.insert(iter, "The text widget can display text with "
            "all kinds of nifty attributes. It also supports multiple views "
            "of the same buffer; this demo is showing the same buffer in "
            "two places.\n\n")

        text_buffer.insert_with_tags_by_name(iter, "Font styles. ", "heading")

        text_buffer.insert(iter, "For example, you can have ")
        text_buffer.insert_with_tags_by_name(iter,
                            "italic", "italic")
        text_buffer.insert(iter, ", ");
        text_buffer.insert_with_tags_by_name(iter,
                            "bold", "bold")
        text_buffer.insert(iter, ", or ", -1)
        text_buffer.insert_with_tags_by_name(iter,
                            "monospace(typewriter)", "monospace")
        text_buffer.insert(iter, ", or ")
        text_buffer.insert_with_tags_by_name(iter,
                            "big", "big")
        text_buffer.insert(iter, " text. ")
        text_buffer.insert(iter, "It's best not to hardcode specific text "
            "sizes; you can use relative sizes as with CSS, such as ")
        text_buffer.insert_with_tags_by_name(iter,
                            "xx-small", "xx-small")
        text_buffer.insert(iter, " or ")
        text_buffer.insert_with_tags_by_name(iter,
                            "x-large", "x-large")
        text_buffer.insert(iter, " to ensure that your program properly "
            "adapts if the user changes the default font size.\n\n")

        text_buffer.insert_with_tags_by_name(iter, "Colors. ", "heading")

        text_buffer.insert(iter, "Colors such as ");
        text_buffer.insert_with_tags_by_name(iter,
                            "a blue foreground", "blue_foreground")
        text_buffer.insert(iter, " or ");
        text_buffer.insert_with_tags_by_name(iter,
                            "a red background",
                            "red_background")
        text_buffer.insert(iter, " or even ", -1);
        text_buffer.insert_with_tags_by_name(iter,
                            "a stippled red background",
                            "red_background",
                            "background_stipple")

        text_buffer.insert(iter, " or ", -1);
        text_buffer.insert_with_tags_by_name(iter,
                            "a stippled blue foreground on solid red background",
                            "blue_foreground",
                            "red_background",
                            "foreground_stipple")
        text_buffer.insert(iter, "(select that to read it) can be used.\n\n", -1);

        text_buffer.insert_with_tags_by_name(iter,
            "Underline, strikethrough, and rise. ", "heading")

        text_buffer.insert_with_tags_by_name(iter,
                            "Strikethrough",
                            "strikethrough")
        text_buffer.insert(iter, ", ", -1)
        text_buffer.insert_with_tags_by_name(iter,
                            "underline",
                            "underline")
        text_buffer.insert(iter, ", ", -1)
        text_buffer.insert_with_tags_by_name(iter,
                            "double underline",
                            "double_underline")
        text_buffer.insert(iter, ", ", -1)
        text_buffer.insert_with_tags_by_name(iter,
                            "superscript",
                            "superscript")
        text_buffer.insert(iter, ", and ", -1)
        text_buffer.insert_with_tags_by_name(iter,
                            "subscript",
                            "subscript")
        text_buffer.insert(iter, " are all supported.\n\n", -1)

        text_buffer.insert_with_tags_by_name(iter, "Images. ",
                            "heading")

        text_buffer.insert_with_tags_by_name(iter, "Spacing. ",
                            "heading")

        text_buffer.insert(iter,
            "You can adjust the amount of space before each line.\n", -1)

        text_buffer.insert_with_tags_by_name(iter,
            "This line has a whole lot of space before it.\n",
            "big_gap_before_line", "wide_margins")
        text_buffer.insert_with_tags_by_name(iter,
            "You can also adjust the amount of space after each line; "
            "this line has a whole lot of space after it.\n",
            "big_gap_after_line", "wide_margins")

        text_buffer.insert_with_tags_by_name(iter,
            "This line has all wrapping turned off, so it makes the "
            "horizontal scrollbar appear.\n\n\n", "no_wrap")

        text_buffer.insert_with_tags_by_name(iter, "Justification. ",
                            "heading");

        text_buffer.insert_with_tags_by_name(iter,
            "\nThis line has center justification.\n", "center")

        text_buffer.insert_with_tags_by_name(iter,
            "This line has right justification.\n", "right_justify")

        text_buffer.insert_with_tags_by_name(iter,
            "Internationalization. ", "heading")

        text_buffer.insert(iter, "You can put widgets in the buffer: "
            "Here's a button: ", -1)

        anchor = text_buffer.create_child_anchor(iter)
        text_buffer.insert(iter, " and a menu: ", -1)
        anchor = text_buffer.create_child_anchor(iter)
        text_buffer.insert(iter, " and a scale: ", -1)
        anchor = text_buffer.create_child_anchor(iter)
        text_buffer.insert(iter, " and an animation: ", -1)
        anchor = text_buffer.create_child_anchor(iter)
        text_buffer.insert(iter, " finally a text entry: ", -1)
        anchor = text_buffer.create_child_anchor(iter)
        text_buffer.insert(iter, ".\n", -1)

        text_buffer.insert(iter, "\n\nThis demo doesn't demonstrate all "
            "the GtkTextBuffer features; it leaves out, for example: "
            "invisible/hidden text(doesn't work in GTK 2, but planned), "
            "tab stops, application-drawn areas on the sides of the "
            "widget for displaying breakpoints and such...", -1)

        # Apply word_wrap tag to whole buffer */
        start, end = text_buffer.get_bounds()
        text_buffer.apply_tag_by_name("word_wrap", start, end)


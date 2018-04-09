import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
lista=[]
class ListBoxRowWithData(Gtk.ListBoxRow):
    def __init__(self, data):
        super(Gtk.ListBoxRow, self).__init__()
        self.data = data
        self.add(Gtk.Label(data))

class ListBoxWindow(Gtk.Window):
    def on_button_clicked(self, widget):
        self.spinner.start()
        ruta=lista[0]
        os.system("./archalien.py %s"%ruta)
        lista.pop(0)
        self.spinner.stop()
    def on_button_selection_changed(self, w):
        ruta=w.get_file().get_path()
        lista.append(ruta)
    def __init__(self):
        Gtk.Window.__init__(self, title="Archalien-Gui")
        self.set_border_width(10)

        self.spinner = Gtk.Spinner()

        box_outer = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(box_outer)
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        box_outer.pack_start(listbox, True, True, 0)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        hbox.pack_start(vbox, True, True, 0)

        label1 = Gtk.Label("Seleccione el archivo", xalign=0)
        vbox.pack_start(label1, True, True, 0)
        label2 = Gtk.Label("a convertir ", xalign=0)
        vbox.pack_start(label2, True, True, 0)

        seleccion_archivo = Gtk.FileChooserButton()
        archivo_filter = Gtk.FileFilter()
        archivo_filter.set_name("Folder")
        archivo_filter.add_pattern("*.deb")
        archivo_filter.add_pattern("*.rpm")
        seleccion_archivo.add_filter(archivo_filter)
        seleccion_archivo.props.valign = Gtk.Align.CENTER
        seleccion_archivo.connect("file-set", self.on_button_selection_changed)
        hbox.pack_start(seleccion_archivo, False, True, 0)
        listbox.add(row)

        row = Gtk.ListBoxRow()
        hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=50)
        row.add(hbox)
        button=Gtk.Button(label="Convertir")
        button.connect("clicked", self.on_button_clicked)
        hbox.pack_start(button, True, False, 0)
        listbox.add(row)

win = ListBoxWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

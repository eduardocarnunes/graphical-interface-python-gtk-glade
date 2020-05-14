import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

builder = Gtk.Builder()
builder.add_from_file('userinterface_Example02_CalcIMC.glade')

class Handler():
    def __init__(self):
        self.peso = builder.get_object('peso')
        self.altura = builder.get_object('altura')
        self.text_buffer = builder.get_object('textbuffer1')
        
    def on_button1_clicked(self, button):
        aux_peso = float(self.peso.get_text())
        aux_altura = float(self.altura.get_text()) ** 2
        imc =  aux_peso/aux_altura
                    
        self.text_buffer.set_text("Seu IMC é: " + str(round(imc, 2)))
        
        
    def on_janela_principal_destroy(self, windows):
        Gtk.main_quit()
        
    

builder.connect_signals(Handler())
window = builder.get_object('janela_principal')
window.show_all()
Gtk.main()

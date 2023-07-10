import gi
import json
import subprocess
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

CONFIG_PATH= '/usr/share/nbfc/configs/HPOMEN15.json'


class NBFCConfigWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="NBFC Config Editor")
        
        # Carica la configurazione
        self.config = self.read_config(CONFIG_PATH)

        # Crea un ScrolledWindow
        self.scrolled_window = Gtk.ScrolledWindow()
        self.add(self.scrolled_window)

        # Crea un'interfaccia utente per modificare la configurazione
       
        self.grid = Gtk.Grid()
        self.scrolled_window.add(self.grid)

      
        # Crea un widget per ogni valore nel file di configurazione
        row = 0
        for key, value in self.config.items():
            if isinstance(value, list):
                for i, item in enumerate(value):
                    for subkey, subvalue in item.items():
                        if isinstance(subvalue, list):
                            for j, subitem in enumerate(subvalue):
                                for subsubkey, subsubvalue in subitem.items():
                                    self.add_label_entry(row, f'{key} {i} {subkey} {j} {subsubkey}', subsubvalue)
                                    row += 1
                        else:
                            self.add_label_entry(row, f'{key} {i} {subkey}', subvalue)
                            row += 1
            else:
                self.add_label_entry(row, key, value)
                row += 1
        # Crea un Button per salvare le modifiche
        self.save_button = Gtk.Button(label="Save")
        self.save_button.connect("clicked", self.on_save_button_clicked)
        self.grid.attach(self.save_button, 0, row, 2, 1)

    def add_label_entry(self, row, label_text, value):
        label = Gtk.Label(label=label_text)
        self.grid.attach(label, 0, row, 1, 1)
        entry = Gtk.Entry()
        entry.set_text(str(value))
        self.grid.attach(entry, 1, row, 1, 1)

    def on_fan_config_combo_changed(self, combo):
        # Aggiorna l'Entry con il nome della configurazione del ventilatore selezionata
        fan_config_index = combo.get_active()
        self.fan_display_name_entry.set_text(self.config['FanConfigurations'][fan_config_index]['FanDisplayName'])

    def on_save_button_clicked(self, button):
        # Salva le modifiche alla configurazione
        # ...
        self.write_config(CONFIG_PATH, self.config)
        
        # Riavvia il servizio NBFC
        subprocess.run(['sudo', 'systemctl', 'restart', 'nbfc_service'])

    def read_config(self, file_path):
        with open(file_path, 'r') as f:
            config = json.load(f)
        return config

    def write_config(self, file_path, config):
        with open(file_path, 'w') as f:
            json.dump(config, f, indent=4)

win = NBFCConfigWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
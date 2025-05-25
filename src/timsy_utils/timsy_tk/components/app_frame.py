import tkinter as tk

from services.config import Config


class AppFrame(tk.Frame):
    def __init__(self, parent, config:Config = None, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.config = config if config else Config()
        self.label = tk.Label(self, text="Hello, World!")
        self.label.pack()

    def set_icon_on_root(self):
        try:
            app_icon = self.config.get('DEFAULT', 'applicationIcon')
        except KeyError as e:
            print(e)
            pass
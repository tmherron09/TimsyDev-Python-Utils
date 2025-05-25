from tkinter import ttk

class CellLeaf(ttk.Frame):
    """
    A single cell for use in PanedTableWidget, displaying a label.
    Methods:
    - set_text(value): Set the label text.
    - get_text(): Get the label text.
    """
    def __init__(self, parent, cell_text: str = "Cell"):
        super().__init__(parent, relief='solid', borderwidth=1)
        self.label = ttk.Label(self, text=cell_text)
        self.label.pack(expand=True, fill='both')
        self.parent = parent

    def set_text(self, value):
        self.label.config(text=value)

    def get_text(self):
        return self.label.cget('text')

from tkinter import ttk

class TreeTable(ttk.Treeview):
    """
    A table layout using ttk.Treeview, supporting headings, columns, and cell click/mouse-over events.
    columns: tuple of column identifiers (default: ('#0', '#1', '#2'))
    headings: list of column headings (default: ['Name', 'Age', 'Department'])
    data: list of row data (each row is a tuple/list)
    Methods:
    - set_data(data): Set the table data.
    - clear(): Clear all rows.
    """
    def __init__(self, parent, columns=None, headings=None, data=None, *args, **kwargs):
        if columns is None:
            columns = ('#0', '#1', '#2')
        if headings is None:
            headings = ['Name', 'Age', 'Department']
        super().__init__(parent, columns=columns, *args, **kwargs)
        self.parent = parent
        for idx, col in enumerate(columns):
            heading = headings[idx] if idx < len(headings) else col
            self.heading(col, text=heading)
            self.column(col, width=100)
        if data:
            self.set_data(data)
        self.bind('<Motion>', self.on_mouse_over)
        self.bind('<Button-1>', self.on_mouse_click)

    def set_data(self, data):
        self.clear()
        for row in data:
            self.insert('', 'end', text=row[0], values=row[1:])

    def clear(self):
        self.delete(*self.get_children())

    def on_mouse_over(self, event):
        row_id = self.identify_row(event.y)
        column_id = self.identify_column(event.x)
        # Optionally, update a status bar or display info

    def on_mouse_click(self, event):
        row_id = self.identify_row(event.y)
        column_id = self.identify_column(event.x)
        item = self.item(row_id)
        tag_name = "highlighted"
        self.tag_configure(tag_name, background="yellow")
        col_index = int(column_id.strip('#')) - 1
        if col_index == -1:
            cell_value = item['text']
        else:
            cell_value = item['values'][col_index]
        print(f"Clicked on row: {row_id}, column: {column_id}, Value: {cell_value}")


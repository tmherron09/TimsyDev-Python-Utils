from tkinter import ttk
import tkinter as tk
from .PanedTableWidget import PanedTableWidget
from .TreeTable import TreeTable

class Table(ttk.Frame):
    """
    A flexible table widget that can use either a paned layout (cells as frames) or a treeview layout (rows/columns with headings).
    Use the 'mode' argument to select the layout: 'paned' or 'tree'.
    Additional configuration options can be passed for row/column counts (paned) or columns/headings (tree).
    """
    def __init__(self, parent, mode='tree', row_count=10, column_count=5, columns=None, headings=None, data=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.mode = mode
        self.table_widget = None
        if mode == 'paned':
            self.table_widget = PanedTableWidget(self, row_count=row_count, column_count=column_count)
        else:
            if columns is None:
                columns = ('#0', '#1', '#2')
            if headings is None:
                headings = ['Name', 'Age', 'Department']
            self.table_widget = TreeTable(self, columns=columns, headings=headings, data=data)
        self.table_widget.pack(expand=True, fill='both')

    def get_widget(self):
        """Return the underlying table widget (PanedTableWidget or TreeTable)."""
        return self.table_widget

    def clear(self):
        """Clear the table contents."""
        if self.mode == 'tree':
            self.table_widget.delete(*self.table_widget.get_children())
        elif self.mode == 'paned':
            for cell in self.table_widget.cells:
                cell.set_text("")

    def set_data(self, data):
        """Set data for the table (tree mode only)."""
        if self.mode == 'tree':
            self.clear()
            for row in data:
                self.table_widget.insert('', 'end', text=row[0], values=row[1:])

    def set_cell(self, row, col, value):
        """Set the value of a cell (paned mode only)."""
        if self.mode == 'paned':
            idx = row * self.table_widget.column_count + col
            if 0 <= idx < len(self.table_widget.cells):
                self.table_widget.cells[idx].set_text(value)

    def get_cell(self, row, col):
        """Get the value of a cell (paned mode only)."""
        if self.mode == 'paned':
            idx = row * self.table_widget.column_count + col
            if 0 <= idx < len(self.table_widget.cells):
                return self.table_widget.cells[idx].get_text()
        return None

# Documentation:
Table.__doc__ += """

Configuration Options:
- mode: 'tree' (default) for TreeTable, 'paned' for PanedTableWidget.
- row_count, column_count: Used for paned mode.
- columns: Tuple of column identifiers for tree mode.
- headings: List of column headings for tree mode.
- data: List of row data for tree mode (each row is a tuple/list).

Methods:
- get_widget(): Returns the underlying table widget.
- clear(): Clears the table contents.
- set_data(data): Sets data for tree mode.
- set_cell(row, col, value): Sets a cell value in paned mode.
- get_cell(row, col): Gets a cell value in paned mode.
"""

# Example usage
if __name__ == '__main__':
    root = tk.Tk()
    root.title("Merged Table Example")
    # Use 'tree' for TreeTable, 'paned' for PanedTableWidget
    table = Table(root, mode='tree')
    table.pack(expand=True, fill='both')
    root.mainloop()


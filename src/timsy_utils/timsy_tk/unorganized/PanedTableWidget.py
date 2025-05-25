from tkinter import ttk

class PanedTableWidget(ttk.PanedWindow):
    """
    A table layout using nested PanedWindows and CellLeaf widgets for a grid-like appearance.
    row_count: number of rows
    column_count: number of columns
    """
    def __init__(self, parent, row_count=10, column_count=5, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.parent = parent
        self.row_count = row_count
        self.column_count = column_count
        self.cells = []
        for row_index in range(self.row_count):
            paned_row = ttk.PanedWindow(self, orient='horizontal')
            for col_index in range(self.column_count):
                from .CellLeaf import CellLeaf
                cell = CellLeaf(paned_row, f'Cell {row_index}-{col_index}')
                paned_row.add(cell)
                self.cells.append(cell)
            self.add(paned_row)

    def set_cell(self, row, col, value):
        idx = row * self.column_count + col
        if 0 <= idx < len(self.cells):
            self.cells[idx].set_text(value)

    def get_cell(self, row, col):
        idx = row * self.column_count + col
        if 0 <= idx < len(self.cells):
            return self.cells[idx].get_text()
        return None

    def clear(self):
        for cell in self.cells:
            cell.set_text("")

PanedTableWidget.__doc__ += """

Methods:
- set_cell(row, col, value): Set the value of a cell.
- get_cell(row, col): Get the value of a cell.
- clear(): Clear all cell values.
"""

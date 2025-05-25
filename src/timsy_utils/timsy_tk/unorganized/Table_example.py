import tkinter as tk
from Table import Table

# Example data for tree mode
tree_data = [
    ("John Doe", 30, "HR"),
    ("Jane Doe", 25, "IT"),
    ("John Smith", 35, "Finance"),
]

def demo_tree_table():
    root = tk.Tk()
    root.title("Table Widget Demo - Tree Mode")
    table = Table(root, mode='tree', columns=("#0", "#1", "#2"), headings=["Name", "Age", "Department"], data=tree_data)
    table.pack(expand=True, fill='both')
    # Dynamically update data after 2 seconds
    def update():
        table.set_data([
            ("Alice", 28, "Marketing"),
            ("Bob", 40, "Sales"),
        ])
    root.after(2000, update)
    root.mainloop()

def demo_paned_table():
    root = tk.Tk()
    root.title("Table Widget Demo - Paned Mode")
    table = Table(root, mode='paned', row_count=4, column_count=3)
    table.pack(expand=True, fill='both')
    # Set some cell values
    table.set_cell(0, 0, "A1")
    table.set_cell(1, 1, "B2")
    table.set_cell(2, 2, "C3")
    # Get a cell value and print it
    print("Cell (1,1):", table.get_cell(1, 1))
    # Clear all cells after 3 seconds
    def clear():
        table.clear()
    root.after(3000, clear)
    root.mainloop()

if __name__ == "__main__":
    print("1: TreeTable demo\n2: PanedTableWidget demo")
    mode = input("Choose demo (1 or 2): ").strip()
    if mode == "2":
        demo_paned_table()
    else:
        demo_tree_table()


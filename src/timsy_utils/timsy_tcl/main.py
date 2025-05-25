import tkinter as tk
from tkinter import ttk
import sys

# --- Helper Functions ---
def load_theme(root, theme_file, apply_proc=None):
    """Load a Tcl theme file and optionally call a theme application proc."""
    try:
        root.tk.call('source', theme_file)
        if apply_proc:
            root.tk.call(apply_proc)
    except tk.TclError as e:
        print(f"Error loading theme: {e}")
        sys.exit(1)


def create_styled_widgets(frame, style_prefix=None):
    """Create and grid a set of styled widgets in the given frame."""
    def style(name):
        return f"{style_prefix}.{name}" if style_prefix else name

    label = ttk.Label(frame, text="Hello, Tkinter!", style=style("TLabel"))
    label.grid(pady=(0, 10))

    entry = ttk.Entry(frame, style=style("TEntry"))
    entry.grid(pady=(0, 10))

    button = ttk.Button(frame, text="Click Me", style=style("TButton"))
    button.grid(pady=(0, 10))

    checkbutton = ttk.Checkbutton(frame, text="Check Me", style=style("TCheckbutton"))
    checkbutton.grid()


def main(theme_file='style_01.tcl'):
    """Run the app with a basic or non-namespaced theme."""
    root = tk.Tk()
    root.title("Stylish Tkinter App")
    load_theme(root, theme_file)
    frame = ttk.Frame(root, padding="20")
    frame.grid()
    create_styled_widgets(frame)
    root.mainloop()


def main_theme(theme_file='theme_01.tcl', apply_proc='Theme01::applyStyles'):
    """Run the app with a namespaced theme and styles."""
    root = tk.Tk()
    root.title("Namespaced Theme in Tkinter")
    load_theme(root, theme_file, apply_proc)
    frame = ttk.Frame(root, padding="20", style="Theme.TFrame")
    frame.grid()
    create_styled_widgets(frame, style_prefix="Theme")
    root.mainloop()


def usage():
    print("Usage: python main.py [basic|theme]")
    print("  basic: Use style_01.tcl (default)")
    print("  theme: Use theme_01.tcl with Theme01::applyStyles")


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'theme':
        main_theme()
    else:
        main()

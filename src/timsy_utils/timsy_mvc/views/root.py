# timsy_mvc/views/root.py

"""
Detailed Usage Guide for Root (and the MVC pattern in timsy_mvc)

How to Use Root in Your Tkinter MVC Application:

1. **Instantiate Root**
   - Create an instance of Root as your main Tkinter window.
   - Pass it as the master to your view frames.

2. **Configure Window**
   - Root sets a default title, size, and background color.
   - You can further configure the window (e.g., add menus, set icons) by extending Root.

3. **Example Usage**
   ```python
   from timsy_mvc.views.root import Root
   from timsy_mvc.views.home import HomeView

   root = Root()
   home_view = HomeView(root)
   home_view.grid(row=0, column=0, sticky='nsew')
   root.mainloop()
   ```

4. **Best Practices**
   - Use Root as the single main window for your application.
   - Place all frames as children of Root for consistent layout and switching.
   - Extend Root if you need to add global UI elements (menus, status bars, etc.).
"""


import tkinter as tk

class Root(tk.Tk):
    """
    Reusable root window for Tkinter MVC applications.
    """
    def __init__(self):
        super().__init__()
        self.title("Timsy MVC Application")
        self.geometry("400x300")
        self.configure(bg="#f0f0f0")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)


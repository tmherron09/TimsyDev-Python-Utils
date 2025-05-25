# timsy_mvc/views/home.py

"""
Detailed Usage Guide for HomeView (and the MVC pattern in timsy_mvc)

How to Use HomeView in Your Tkinter MVC Application:

1. **Instantiate HomeView**
   - Create an instance of HomeView, passing the root window as the master.
   - Place the HomeView in your application's layout (e.g., using grid or pack).

2. **Expose Widgets for Controller Binding**
   - HomeView provides a greeting label and a sign-out button.
   - The controller can access these widgets to bind events (e.g., set the sign-out button's command).

3. **Update the View**
   - The controller or model can update the greeting label by calling `self.greeting.config(text=...)`.
   - Extend HomeView to add more widgets and methods for updating the UI.

4. **Example Usage**
   ```python
   from timsy_mvc.views.root import Root
   from timsy_mvc.views.home import HomeView

   root = Root()
   home_view = HomeView(root)
   home_view.grid(row=0, column=0, sticky='nsew')
   root.mainloop()
   ```

5. **Best Practices**
   - Keep all UI layout and widget creation in the view class.
   - Expose only the widgets or methods needed by the controller for event binding.
   - Do not include business logic in the view.
"""


import tkinter as tk

class HomeView(tk.Frame):
    """
    Example Home view for the MVC pattern.
    Extend this class to add widgets and UI logic for your home screen.
    """
    def __init__(self, master):
        super().__init__(master)
        self.greeting = tk.Label(self, text="Welcome!", font=("Arial", 16))
        self.greeting.pack(pady=20)
        self.signout_btn = tk.Button(self, text="Sign Out")
        self.signout_btn.pack(pady=10)


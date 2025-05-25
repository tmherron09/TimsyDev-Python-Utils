# Template: View Layer

"""
This is a template for a View class in the Tkinter MVC pattern.
Fill in your UI layout, widgets, and expose any needed methods for the controller.
"""

import tkinter as tk

class ViewBase(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        # Build your UI here
        # Example: self.label = tk.Label(self, text="...")
        # self.label.pack()
        pass

    def get_user_input(self):
        """Return user input from widgets (to be called by the controller)."""
        pass

    def set_data(self, data):
        """Update the view with new data from the model."""
        pass

    # Add more methods as needed for your UI


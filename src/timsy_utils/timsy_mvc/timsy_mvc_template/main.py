# Template: Application Entry Point

"""
This is a template for the main entry point of a Tkinter MVC application.
Instantiate your Model, View, and Controller here, then start the main loop.
"""

from template.model import ModelBase
from template.view import ViewBase
from template.controller import ControllerBase


def main():
    # Replace ModelBase, ViewBase, ControllerBase with your concrete classes
    model = ModelBase()
    root = ...  # Create your Tk root window here
    view = ViewBase(root)
    controller = ControllerBase(model, view)
    # Optionally, call controller.start() or similar
    root.mainloop()

if __name__ == "__main__":
    main()


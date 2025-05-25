# timsy_mvc/views/main.py
"""
Detailed Usage Guide for AbstractViewManager (and the MVC pattern in timsy_mvc)

How to Use AbstractViewManager in Your Tkinter MVC Application:

1. **Subclass AbstractViewManager**
   - Create your own view manager class by inheriting from AbstractViewManager.
   - Implement the abstract methods `switch(name)` and `start_mainloop()`.
   - Manage your application's frames or views (e.g., using a dictionary of frames).

2. **Managing Views**
   - Store each view (Tkinter Frame) in a dictionary, e.g., `self.frames['home'] = HomeView(self.root)`.
   - Implement `switch(name)` to raise or display the desired frame.
   - Implement `start_mainloop()` to call `self.root.mainloop()`.

3. **Example Subclass**
   ```python
   import tkinter as tk
   from timsy_mvc.views.main import AbstractViewManager
   from timsy_mvc.views.root import Root
   from timsy_mvc.views.home import HomeView

   class MyViewManager(AbstractViewManager):
       def __init__(self):
           self.root = Root()
           self.frames = {}
           self.frames['home'] = HomeView(self.root)
           self.frames['home'].grid(row=0, column=0, sticky='nsew')

       def switch(self, name):
           self.frames[name].tkraise()

       def start_mainloop(self):
           self.root.mainloop()
   ```

4. **Best Practices**
   - Keep all UI layout and widget creation in the view layer.
   - The view manager should not contain business logic.
   - Expose only the necessary methods for the controller to switch views and start the main loop.
"""

from abc import ABC, abstractmethod
from typing import Any

class AbstractViewManager(ABC):
    """
    Abstract base class for view managers in the MVC pattern.
    Responsible for switching between views and managing the root window.
    """
    @abstractmethod
    def switch(self, name: str) -> None:
        """Switch to the view with the given name."""
        pass

    @abstractmethod
    def start_mainloop(self) -> None:
        """Start the Tkinter main loop."""
        pass


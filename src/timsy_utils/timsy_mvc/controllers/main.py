# timsy_mvc/controllers/main.py

"""
Detailed Usage Guide for AbstractController (and the MVC pattern in timsy_mvc)

How to Use AbstractController in Your Tkinter MVC Application:

1. **Subclass AbstractController**
   - Create your own controller class by inheriting from AbstractController.
   - Implement the abstract method `start()` to initialize your application flow (e.g., set up event bindings, show the initial view).
   - Store references to your model and view in the controller.

2. **Event Handling**
   - Bind view widget events (e.g., button clicks) to controller methods.
   - Register event listeners for model events to update the view as needed.

3. **Coordinating Model and View**
   - In your controller methods, update the model in response to user actions.
   - When the model changes, update the view accordingly (often via event listeners).

4. **Example Subclass**
   ```python
   from timsy_mvc.controllers.main import AbstractController

   class MyController(AbstractController):
       def start(self):
           self.view.switch('home')
           self.view.start_mainloop()
   ```

5. **Best Practices**
   - Keep all coordination logic in the controller.
   - Do not put business logic in the controller; keep it in the model.
   - Do not manipulate widgets directly in the controller except through the view interface.
"""


from abc import ABC, abstractmethod

class AbstractController(ABC):
    """
    Abstract base class for controllers in the MVC pattern.
    Responsible for coordinating between the model and view.
    """
    def __init__(self, model, view):
        self.model = model
        self.view = view

    @abstractmethod
    def start(self):
        """Start the controller and initialize the application flow."""
        pass


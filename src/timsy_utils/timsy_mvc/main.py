# timsy_mvc/main.py
"""
Entry point for a reusable Tkinter MVC application using the timsy_mvc library.
This file demonstrates how to wire together the abstract Model, View, and Controller layers.

Detailed Usage Guide for timsy_mvc/main.py (Entry Point)

How to Use the Entry Point in Your Tkinter MVC Application:

1. **Purpose**
   - This file serves as the main entry point for your Tkinter MVC application.
   - It demonstrates how to wire together the Model, View, and Controller layers using the timsy_mvc library.

2. **Replace Abstract Classes with Concrete Implementations**
   - Import your concrete Model, ViewManager, and Controller classes (e.g., HomeModel, MyViewManager, HomeController).
   - Instantiate them in place of AbstractModel, AbstractViewManager, and AbstractController.

3. **Wiring the Layers**
   - Pass the model and view instances to the controller.
   - Call `controller.start()` to begin the application flow (e.g., show the initial view, start the main loop).

4. **Example Usage**
   ```python
   from timsy_mvc.models.home import HomeModel
   from timsy_mvc.views.my_view_manager import MyViewManager
   from timsy_mvc.controllers.home import HomeController

   def main():
       model = HomeModel()
       view = MyViewManager()
       controller = HomeController(model, view)
       controller.start()

   if __name__ == "__main__":
       main()
   ```

5. **Best Practices**
   - Keep the entry point minimal: only instantiate and wire up the main components.
   - Do not include business logic or UI code here.
   - Use this file as the launching point for your application.
"""

from timsy_mvc.models.main import AbstractModel
from timsy_mvc.views.main import AbstractViewManager
from timsy_mvc.controllers.main import AbstractController


def main():
    # Replace Abstract* with your concrete implementations
    model = AbstractModel()
    view = AbstractViewManager()
    controller = AbstractController(model, view)
    controller.start()

if __name__ == "__main__":
    main()



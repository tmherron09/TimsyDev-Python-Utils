# timsy_mvc/controllers/home.py
"""
Detailed Usage Guide for HomeController (and the MVC pattern in timsy_mvc)

How to Use HomeController in Your Tkinter MVC Application:

1. **Instantiate the Model, ViewManager, and Controller**
   - Create an instance of your model (e.g., HomeModel).
   - Create an instance of your view manager (should have a 'frames' dict with a 'home' frame, e.g., HomeView).
   - Pass both to HomeController.

2. **Event Binding**
   - HomeController automatically binds the signout button to the logout method.
   - It listens for 'username_changed' events from the model and updates the greeting accordingly.

3. **Switching Views**
   - The controller expects the view manager to have a 'frames' dictionary with a 'home' key.
   - To show the home view, call: `view_manager.switch('home')`.

4. **Updating the Model**
   - Call `model.set_username('NewName')` to update the username and trigger the view update.

5. **Extending**
   - Add more widgets to HomeView and bind them in HomeController's `_bind()` method.
   - Add more event listeners for other model events as needed.

6. **Example Integration**
   ```python
   from timsy_mvc.models.home import HomeModel
   from timsy_mvc.views.main import YourViewManager  # Should manage frames including 'home'
   from timsy_mvc.controllers.home import HomeController

   model = HomeModel()
   view_manager = YourViewManager()
   home_controller = HomeController(model, view_manager)
   view_manager.switch('home')
   view_manager.start_mainloop()
   ```

7. **Separation of Concerns**
   - The controller does not directly manipulate widgets except through the view.
   - The model does not know about the view or controller.
   - The view is only responsible for UI layout and exposing widgets for binding.

8. **Best Practices**
   - Use event listeners for all model-to-view updates.
   - Keep business logic in the model, UI logic in the view, and coordination in the controller.
   - Extend the controller for more complex user interactions.
"""

from .timsy_mvc import HomeModel
from .views.home import HomeView

class HomeController:
    """
    Example Home controller for the MVC pattern.
    Connects the HomeModel and HomeView, handles user actions, and updates the view.
    """
    def __init__(self, model: HomeModel, view_manager):
        self.model = model
        self.view_manager = view_manager
        self.frame = self.view_manager.frames["home"] if hasattr(self.view_manager, "frames") else None
        self._bind()
        self.model.add_event_listener('username_changed', self.update_view)

    def _bind(self):
        if self.frame:
            self.frame.signout_btn.config(command=self.logout)

    def logout(self):
        # Example: clear username and update view
        self.model.set_username("")

    def update_view(self, *args, **kwargs):
        username = self.model.get_state().get('username', '')
        if self.frame:
            if username:
                self.frame.greeting.config(text=f"Welcome, {username}!")
            else:
                self.frame.greeting.config(text="Welcome!")


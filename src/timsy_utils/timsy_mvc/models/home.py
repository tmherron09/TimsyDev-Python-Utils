# timsy_mvc/models/home.py
"""
Detailed Usage Guide for HomeModel (and the MVC pattern in timsy_mvc)

How to Use HomeModel in Your Tkinter MVC Application:

1. **Instantiation**
   - Create an instance of HomeModel: `model = HomeModel()`

2. **Setting and Getting State**
   - Use `set_username(username)` to update the username. This will notify any listeners of the change.
   - Use `get_state()` to retrieve the current state as a dictionary, e.g., `{'username': ...}`.

3. **Event System**
   - Register listeners for the 'username_changed' event using `add_event_listener('username_changed', callback)`.
   - The callback will be called with the new username whenever it changes.

4. **Example Usage**
   ```python
   from timsy_mvc.models.home import HomeModel

   def on_username_changed(new_username):
       print(f"Username changed to: {new_username}")

   model = HomeModel()
   model.add_event_listener('username_changed', on_username_changed)
   model.set_username('Alice')  # Triggers the event and prints the message
   print(model.get_state())     # Outputs: {'username': 'Alice'}
   ```

5. **Best Practices**
   - Use the event system to keep the view/controller in sync with the model.
   - Do not include UI or controller logic in the model.
   - Extend HomeModel with additional fields and events as needed for your application.
"""

from . import AbstractModel

class HomeModel(AbstractModel):
    """
    Example concrete model for a Home screen.
    """
    def __init__(self):
        super().__init__()
        self._username = None

    def set_username(self, username: str):
        self._username = username
        self._notify('username_changed', username)

    def get_state(self):
        return {'username': self._username}


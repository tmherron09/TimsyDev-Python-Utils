# timsy_mvc/models/main.py
"""
Detailed Usage Guide for AbstractModel (and the MVC pattern in timsy_mvc)

How to Use AbstractModel in Your Tkinter MVC Application:

1. **Subclass AbstractModel**
   - Create your own model class by inheriting from AbstractModel.
   - Implement the abstract method `get_state()` to return the model's current state (as a dict or any relevant structure).

2. **Event System**
   - Use `add_event_listener(event, callback)` to register listeners for model events.
   - Use `remove_event_listener(event, callback)` to unregister listeners.
   - Use `_notify(event, *args, **kwargs)` to notify all listeners of a specific event (typically called inside your model's business logic methods).

3. **Business Logic**
   - Add your own methods for manipulating the model's data.
   - Call `_notify` whenever the model's state changes and the view/controller should be updated.

4. **Example Subclass**
   ```python
   from timsy_mvc.models.main import AbstractModel

   class MyModel(AbstractModel):
       def __init__(self):
           super().__init__()
           self._value = 0

       def increment(self):
           self._value += 1
           self._notify('value_changed', self._value)

       def get_state(self):
           return {'value': self._value}
   ```

5. **Best Practices**
   - Keep all business/data logic in the model.
   - Never reference view or controller objects directly in the model.
   - Use events to communicate changes to the controller/view.
"""

from abc import ABC, abstractmethod
from typing import Any, Callable

class AbstractModel(ABC):
    """
    Abstract base class for all models in the MVC pattern.
    """
    def __init__(self):
        self._listeners = []

    def add_event_listener(self, event: str, callback: Callable):
        self._listeners.append((event, callback))

    def remove_event_listener(self, event: str, callback: Callable):
        self._listeners = [l for l in self._listeners if l != (event, callback)]

    def _notify(self, event: str, *args, **kwargs):
        for evt, callback in self._listeners:
            if evt == event:
                callback(*args, **kwargs)

    @abstractmethod
    def get_state(self) -> Any:
        """Return the current state of the model."""
        pass


# TkinterMvcExample

A demonstration of the Model-View-Controller (MVC) pattern in a Python Tkinter GUI application. This project provides a modular, scalable structure for building maintainable desktop apps.

---

## Project Structure

```
TkinterMvcExample/
│   main.py                # Entry point
├── models/                # Business logic and data
│     main.py              # Main Model class
│     auth.py, base.py     # Auth and base logic
├── views/                 # UI components (Tkinter Frames)
│     main.py              # ViewStackedFrames/ViewSingleFrame
│     home.py, signin.py, signup.py, root.py
├── controllers/           # Controllers for app logic
│     main.py              # Main Controller
│     home.py, signin.py, signup.py
```

---

## How It Works

- **Model**: Manages data and business logic (e.g., authentication state).
- **View**: Manages the UI, with each screen as a separate frame. `ViewStackedFrames` keeps all frames in memory and raises the active one; `ViewSingleFrame` destroys and recreates frames as needed.
- **Controller**: Handles user actions, updates the model, and switches views. Listens for model events (like authentication changes) and updates the UI accordingly.

---

## Tutorial: Re-using This MVC Pattern

1. **Create Your Model**
   - Add your data logic in `models/` (e.g., `profile.py`).
   - Update `models/main.py` to include your new logic.

2. **Design Your Views**
   - Create new view classes in `views/` (e.g., `profile.py`).
   - Add them to `ViewStackedFrames` or `ViewSingleFrame` in `views/main.py`.

3. **Write Controllers**
   - Add new controller classes in `controllers/` for each view or feature.
   - Update `controllers/main.py` to instantiate and manage your new controllers.

4. **Wire Everything in main.py**
   - Import your new model, view, and controller.
   - Instantiate them and start the controller.

5. **Switch Views**
   - Use `self.view.switch('view_name')` in your controller to change screens.

6. **Listen for Model Events**
   - Use event listeners (as in `auth.add_event_listener`) to react to model changes and update the UI.

---

## Example: Adding a Profile Screen

- **models/profile.py**
  ```python
  class Profile:
      def __init__(self, user_id):
          self.user_id = user_id
          # ... load profile data ...
  ```

- **views/profile.py**
  ```python
  import tkinter as tk
  class ProfileView(tk.Frame):
      def __init__(self, master):
          super().__init__(master)
          # ... build UI ...
  ```

- **controllers/profile.py**
  ```python
  class ProfileController:
      def __init__(self, model, view):
          self.model = model
          self.view = view
          # ... handle events ...
  ```

- **views/main.py**: Add `ProfileView` to `ViewStackedFrames` or `ViewSingleFrame`.
- **controllers/main.py**: Instantiate and manage `ProfileController`.

---

## Summary Table

| Folder        | Purpose                        | Example Files         |
|---------------|-------------------------------|----------------------|
| models/       | Data/business logic            | main.py, auth.py     |
| views/        | UI components (Tkinter Frames) | main.py, home.py     |
| controllers/  | User input & app logic         | main.py, signin.py   |
| main.py       | App entry point                | main.py              |

---

## Best Practices
- Keep logic separated: Models for data, Views for UI, Controllers for flow.
- Use event listeners for model-view communication.
- Add new features by extending each layer (model, view, controller).

---

This project is a great starting point for any Tkinter application that needs to be maintainable and scalable. Adapt and extend as needed for your own apps!


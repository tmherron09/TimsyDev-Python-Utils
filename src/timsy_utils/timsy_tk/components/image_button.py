import tkinter as tk
from typing import Callable, Optional

class ImageButton(tk.Button):
    """
    A Tkinter Button that supports changing its image on press/release.
    Usage:
        btn = ImageButton(parent, default_image_path, pressed_image_path, command=callback)
    """
    def __init__(self, master, default_image_path: str, pressed_image_path: str, command: Optional[Callable] = None, **kwargs):
        self.default_image = tk.PhotoImage(file=default_image_path)
        self.pressed_image = tk.PhotoImage(file=pressed_image_path)
        super().__init__(master, image=self.default_image, command=command, borderwidth=0, **kwargs)
        self.bind("<ButtonPress>", self._on_press)
        self.bind("<ButtonRelease>", self._on_release)
        # Keep references to prevent garbage collection
        self._image_refs = (self.default_image, self.pressed_image)

    def _on_press(self, event=None):
        self.config(image=self.pressed_image)

    def _on_release(self, event=None):
        self.config(image=self.default_image)

if __name__ == '__main__':

    def on_button_click():
        print("Button clicked!")

    def main():
        # Create the main window
        root = tk.Tk()
        root.geometry("400x300")
        root.title("Image Button Demo")

        # Load the images
        try:
            default_image = tk.PhotoImage(file="image_button.png")
            pressed_image = tk.PhotoImage(file="image_button - Copy.png")
        except tk.TclError as e:
            print(f"Error: {e}")
            print("Make sure the image files exist in the same directory.")
            return

        btn = ImageButton(root, "image_button.png", "image_button - Copy.png", command=on_button_click)
        btn.pack()




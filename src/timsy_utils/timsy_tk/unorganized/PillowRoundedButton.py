"""
PillowRoundedButton: A reusable Tkinter button with a dynamically generated rounded-corner image using Pillow.

Features:
- Configurable size, background color, text, font, radius, corners, and text color.
- Supports custom command callbacks.
- Helper methods for generating images and updating button appearance.
- Keeps references to images to prevent garbage collection.
- Supports hover and pressed states with different colors.
- Supports icons with configurable size, side, and padding.
- Supports tooltips on hover.

Usage:
    from PillowRoundedButton import PillowRoundedButton
    btn = PillowRoundedButton(parent, text="Hello", command=callback, icon_path="icon.png", tooltip="Click me!")
    btn.pack()
"""
import tkinter as tk
from PIL import Image, ImageDraw, ImageTk, ImageFont
from typing import Tuple, Callable, Optional

class PillowRoundedButton(tk.Button):
    def __init__(self, parent, size: Tuple[int, int] = (100, 50), bg_color: str = 'lightblue', text: str = 'Click Me',
                 text_color: str = 'black', font: Optional[Tuple[str, int]] = None, radius: int = 10,
                 corners: Tuple[bool, bool, bool, bool] = (True, True, True, True), command: Optional[Callable] = None,
                 hover_color: Optional[str] = None, pressed_color: Optional[str] = None,
                 icon_path: Optional[str] = None, icon_size: Optional[Tuple[int, int]] = None,
                 icon_side: str = 'left', icon_padding: int = 5, tooltip: Optional[str] = None, **kwargs):
        self.size = size
        self.bg_color = bg_color
        self.text = text
        self.text_color = text_color
        self.font = font
        self.radius = radius
        self.corners = corners
        self.command = command
        self.hover_color = hover_color or self._darker_color(bg_color, 0.9)
        self.pressed_color = pressed_color or self._darker_color(bg_color, 0.8)
        self.icon_path = icon_path
        self.icon_size = icon_size
        self.icon_side = icon_side
        self.icon_padding = icon_padding
        self._icon_img = None
        self._current_bg = bg_color
        self._photo = self._generate_photo(self.bg_color)
        super().__init__(parent, image=self._photo, command=self.command, relief="flat", overrelief="flat",
                         borderwidth=0, background=parent.cget('bg'), **kwargs)
        self._image_ref = self._photo  # Prevent garbage collection
        self.bind("<Enter>", self._on_enter)
        self.bind("<Leave>", self._on_leave)
        self.bind("<ButtonPress-1>", self._on_press)
        self.bind("<ButtonRelease-1>", self._on_release)
        if tooltip:
            self.tooltip = Tooltip(self, tooltip)
        else:
            self.tooltip = None

    def _generate_photo(self, bg_color) -> ImageTk.PhotoImage:
        img = self.generate_rounded_img(size=self.size, bg_color=bg_color, text=self.text,
                                        text_color=self.text_color, font=self.font, radius=self.radius, corners=self.corners,
                                        icon_path=self.icon_path, icon_size=self.icon_size, icon_side=self.icon_side, icon_padding=self.icon_padding)
        return ImageTk.PhotoImage(img)

    @staticmethod
    def generate_rounded_img(size=(100, 50), bg_color: str = 'lightblue', text: str = 'Click Me',
                             text_color: str = 'black', font: Optional[Tuple[str, int]] = None, radius: int = 10,
                             corners: Tuple[bool, bool, bool, bool] = (True, True, True, True),
                             icon_path: Optional[str] = None, icon_size: Optional[Tuple[int, int]] = None,
                             icon_side: str = 'left', icon_padding: int = 5) -> Image.Image:
        img = Image.new("RGBA", size)
        draw = ImageDraw.Draw(img)
        draw.rounded_rectangle((0, 0, size[0], size[1]), radius=radius, fill=bg_color, outline=None, width=1, corners=corners)
        # Load and paste icon if provided
        icon_img = None
        if icon_path:
            try:
                icon_img = Image.open(icon_path).convert("RGBA")
                if icon_size:
                    icon_img = icon_img.resize(icon_size, Image.LANCZOS)
                else:
                    # Default icon size: fit height
                    icon_img = icon_img.resize((size[1] - 2 * icon_padding, size[1] - 2 * icon_padding), Image.LANCZOS)
            except Exception:
                icon_img = None
        # Use a default font if none provided
        if font is not None:
            try:
                pil_font = ImageFont.truetype(font[0], font[1])
            except Exception:
                pil_font = ImageFont.load_default()
        else:
            pil_font = ImageFont.load_default()
        text_bbox = draw.textbbox((0, 0), text, font=pil_font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        # Icon and text layout
        if icon_img:
            icon_w, icon_h = icon_img.size
            total_w = icon_w + icon_padding + text_width
            total_h = max(icon_h, text_height)
            if icon_side == 'left':
                icon_x = (size[0] - total_w) // 2
                text_x = icon_x + icon_w + icon_padding
            else:  # right
                text_x = (size[0] - total_w) // 2
                icon_x = text_x + text_width + icon_padding
            icon_y = (size[1] - icon_h) // 2
            text_y = (size[1] - text_height) // 2
            img.paste(icon_img, (icon_x, icon_y), icon_img)
        else:
            text_x = (size[0] - text_width) // 2
            text_y = (size[1] - text_height) // 2
        draw.text((text_x, text_y), text, fill=text_color, font=pil_font)
        return img

    def update_button(self, text: Optional[str] = None, bg_color: Optional[str] = None, text_color: Optional[str] = None,
                      font: Optional[Tuple[str, int]] = None, radius: Optional[int] = None,
                      corners: Optional[Tuple[bool, bool, bool, bool]] = None,
                      hover_color: Optional[str] = None, pressed_color: Optional[str] = None,
                      icon_path: Optional[str] = None, icon_size: Optional[Tuple[int, int]] = None,
                      icon_side: Optional[str] = None, icon_padding: Optional[int] = None, tooltip: Optional[str] = None):
        """Update the button's appearance and regenerate the image."""
        if text is not None:
            self.text = text
        if bg_color is not None:
            self.bg_color = bg_color
        if text_color is not None:
            self.text_color = text_color
        if font is not None:
            self.font = font
        if radius is not None:
            self.radius = radius
        if corners is not None:
            self.corners = corners
        if hover_color is not None:
            self.hover_color = hover_color
        if pressed_color is not None:
            self.pressed_color = pressed_color
        if icon_path is not None:
            self.icon_path = icon_path
        if icon_size is not None:
            self.icon_size = icon_size
        if icon_side is not None:
            self.icon_side = icon_side
        if icon_padding is not None:
            self.icon_padding = icon_padding
        if tooltip is not None:
            if self.tooltip:
                self.tooltip.text = tooltip
            else:
                self.tooltip = Tooltip(self, tooltip)
        self._current_bg = self.bg_color
        self._photo = self._generate_photo(self.bg_color)
        self.config(image=self._photo)
        self._image_ref = self._photo

    def _on_enter(self, event):
        self._set_state_bg(self.hover_color)

    def _on_leave(self, event):
        self._set_state_bg(self.bg_color)

    def _on_press(self, event):
        self._set_state_bg(self.pressed_color)

    def _on_release(self, event):
        self._set_state_bg(self.hover_color)

    def _set_state_bg(self, color):
        self._photo = self._generate_photo(color)
        self.config(image=self._photo)
        self._image_ref = self._photo
        self._current_bg = color

    @staticmethod
    def _darker_color(color, factor=0.9):
        """Return a darker shade of the given color."""
        import colorsys
        if color.startswith('#'):
            color = color.lstrip('#')
            lv = len(color)
            rgb = tuple(int(color[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))
        else:
            # fallback for named colors
            from PIL import ImageColor
            rgb = ImageColor.getrgb(color)
        h, l, s = colorsys.rgb_to_hls(*(v / 255.0 for v in rgb))
        l = max(0, min(1, l * factor))
        r, g, b = [int(x * 255) for x in colorsys.hls_to_rgb(h, l, s)]
        return f'#{r:02x}{g:02x}{b:02x}'

# Example usage/demo
if __name__ == "__main__":
    def on_click():
        print("Button clicked!")

    root = tk.Tk()
    root.title("PillowRoundedButton Demo")
    btn = PillowRoundedButton(root, text="Hello!", bg_color="#aaf0d1", text_color="#222", radius=20, font=("Arial", 16), command=on_click, icon_path="icon.png", icon_size=(24, 24), icon_side="left", icon_padding=10, tooltip="Click me!")
    btn.pack(padx=20, pady=20)
    # Dynamically update button after 2 seconds
    def update():
        btn.update_button(text="Updated!", bg_color="#ffcc00", text_color="#000", radius=30, icon_path="updated_icon.png", icon_size=(32, 32), icon_side="right", icon_padding=5, tooltip="Updated tooltip!")
    root.after(2000, update)
    root.mainloop()


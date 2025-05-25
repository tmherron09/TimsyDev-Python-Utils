import tkinter as tk

class Tooltip:
    """
    Tooltip widget for Tkinter. Displays a tooltip on hover for a given widget.
    Usage:
        Tooltip(widget, text="Tooltip text")
    """
    def __init__(self, widget, text: str, delay: int = 500):
        self.widget = widget
        self.text = text
        self.delay = delay
        self._id = None
        self._tipwindow = None
        self.widget.bind("<Enter>", self._schedule)
        self.widget.bind("<Leave>", self._hide)
        self.widget.bind("<ButtonPress>", self._hide)

    def _schedule(self, event=None):
        self._unschedule()
        self._id = self.widget.after(self.delay, self._show)

    def _unschedule(self):
        if self._id:
            self.widget.after_cancel(self._id)
            self._id = None

    def _show(self, event=None):
        if self._tipwindow or not self.text:
            return
        x, y, _, cy = self.widget.bbox("insert") if self.widget.winfo_ismapped() else (0, 0, 0, 0)
        x = x + self.widget.winfo_rootx() + 20
        y = y + cy + self.widget.winfo_rooty() + 20
        self._tipwindow = tw = tk.Toplevel(self.widget)
        tw.wm_overrideredirect(True)
        tw.wm_geometry(f"+{x}+{y}")
        label = tk.Label(tw, text=self.text, background="#ffffe0", relief="solid", borderwidth=1, font=("tahoma", "8", "normal"))
        label.pack(ipadx=4, ipady=2)

    def _hide(self, event=None):
        self._unschedule()
        if self._tipwindow:
            self._tipwindow.destroy()
            self._tipwindow = None
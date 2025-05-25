# Tcl/Tk TLabel Reference Sheet (for Tkinter and .tcl Files)

This guide focuses on how to style, theme, and configure TLabel widgets in Python's Tkinter/ttk using .tcl files. It covers only what can be used or accessed from Python, such as styles, themes, and widget options.

---

## 1. **Styling TLabel with .tcl Files (ttk::style)**
TLabel appearance is controlled by styles. You can configure the default TLabel style or create custom styles in a .tcl file, then load and use them from Python.

### **Configure the Default TLabel Style**
```tcl
ttk::style configure TLabel \
    -font "Segoe UI 12" \
    -foreground #222 \
    -background #f0f0f0 \
    -anchor center \
    -padding {10 5}
```

### **Create and Use a Custom Style**
```tcl
ttk::style configure MyCustom.TLabel \
    -font "Arial 14 bold" \
    -foreground blue \
    -background #e0eaff \
    -relief raised
```

---

## 2. **Common TLabel Style Options (usable from Python)**
- `-font`         : Font family, size, and style (e.g., "Arial 12 bold")
- `-foreground`   : Text color (e.g., `#333`, `red`)
- `-background`   : Background color (may not always show if not using a custom theme)
- `-anchor`       : Text alignment (`center`, `w`, `e`, `n`, `s`, etc.)
- `-padding`      : Internal padding (e.g., `{10 5}` for x/y)
- `-relief`       : Border style (`flat`, `raised`, `sunken`, `groove`, `ridge`)
- `-wraplength`   : Maximum line width before wrapping (in pixels)
- `-justify`      : Text justification (`left`, `center`, `right`)
- `-width`        : Width in characters
- `-takefocus`    : Whether the label can take focus (`0` or `1`)

---

## 3. **Dynamic/State-Based Styling (map)**
You can change label appearance based on state (e.g., active, disabled):
```tcl
ttk::style map TLabel \
    -foreground {disabled #888 active #0055aa} \
    -background {active #e0eaff}
```

---

## 4. **Using .tcl Styles and Themes from Python**
- **Load a .tcl file:**
  ```python
  root.tk.call('source', 'style_label.tcl')
  ```
- **Use a style in Python:**
  ```python
  import tkinter as tk
  from tkinter import ttk
  label = ttk.Label(root, text="Styled from Tcl", style="MyCustom.TLabel")
  label.pack()
  ```
- **Switch themes (if defined in .tcl):**
  ```python
  root.tk.call('ttk::setTheme', 'mytheme')
  ```

---

## 5. **What .tcl Can and Cannot Expose to Python**
- **Can expose:**
  - Styles and themes (via `ttk::style` and `ttk::setTheme`)
  - Optionally, procedures that configure styles (callable from Python via `root.tk.call('procName')`)
- **Cannot expose:**
  - Tcl widget creation/packing logic (Python must create and pack widgets)
  - Direct event bindings or callbacks (must be done in Python)

---

## 6. **Summary Table: What You Can Use from Python**
| Tcl Feature                | Usable from Python? | How to Use                        |
|---------------------------|:-------------------:|-----------------------------------|
| ttk::style configure      | Yes                 | Set style, then use in ttk.Label  |
| ttk::style map            | Yes                 | Set state-based style             |
| ttk::setTheme             | Yes                 | Switch theme                      |
| proc (for styling only)   | Yes                 | Call with root.tk.call            |
| Widget creation/packing   | No                  | Do in Python                      |
| Event bindings/callbacks  | No                  | Do in Python                      |

---

## 7. **References**
- [Tcl/Tk Manual: ttk::label](https://www.tcl

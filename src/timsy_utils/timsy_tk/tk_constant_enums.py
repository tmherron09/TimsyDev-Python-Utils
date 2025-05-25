"""
Tkinter/ttk Enum Reference Sheet
===============================

This file provides enums for common Tkinter and ttk option values, making code more discoverable and type-safe.

Widget Enum Usage Reference
--------------------------
- TkJustify: Label, Entry, Text, Message, Button, Checkbutton, Radiobutton
- TkCompound: Button, Label, Checkbutton, Radiobutton, Menubutton
- TkCursors: All widgets (option: 'cursor')
- TkReliefs: Button, Label, Frame, Entry, Canvas, etc. (option: 'relief')
- TkAnchors: Label, Button, Canvas, etc. (option: 'anchor')
- TkSticky: grid geometry manager (option: 'sticky')
- TkFill: pack/grid geometry managers (option: 'fill')
- TkSides: pack geometry manager (option: 'side')
- TkOrientation: Scale, Scrollbar, Progressbar, Separator, PanedWindow
- TkWrap: Text, Message, Entry (option: 'wrap')
- TkAlign: Text (option: 'align'), rarely used
- TkBorderMode: Canvas, Frame (option: 'bordermode')
- TkSpecialTags: Text widget (tags, marks, positions)
- TkWidgetStates: All widgets (option: 'state')
- TkCanvasState: Canvas items (option: 'state')
- TkMenuItemTypes: Menu (option: 'type')
- TkSelectionModes: Listbox, Treeview (option: 'selectmode')
- TkActivestyles: Listbox (option: 'activestyle')
- TkCanvasStyles: Canvas (option: 'style' for items)
- ViewArguments: Scrollbar, Listbox, Text (view commands)
- TkFontWeight/TkFontSlant: font configuration (option: 'font')
- TkImageFormats: PhotoImage, BitmapImage (option: 'format')

# ttk-specific enums:
- TtkWidgetStates: All ttk widgets (option: 'state', style map)
- TtkProgressbarMode: Progressbar (option: 'mode')
- TtkNotebookTabPosition: Notebook (option: 'tabposition')
- TtkTreeviewShow: Treeview (option: 'show')
- TtkSizegripSide: Sizegrip (option: 'side')

Helper Functions
----------------
- get_ttk_themes(): Returns a list of available ttk themes.
- print_enum_options(enum_cls): Prints all options for a given enum class.

"""

import tkinter as tk
from enum import Enum


class TkReliefs(Enum):
    """
    Grouped Enum for Tkinter relief styles, providing a set of constants that define the appearance of borders.
    """
    # Flat relief style, producing a flat appearance.
    FLAT = "flat"
    # Raised relief style, creating a 3D raised border.
    RAISED = "raised"
    # Sunken relief style, creating a 3D sunken border.
    SUNKEN = "sunken"
    # Groove relief style, creating a grooved border for a sunken or raised effect.
    GROOVE = "groove"
    # Ridge relief style, creating a ridged border for a 3D effect.
    RIDGE = "ridge"
    # Solid relief style, creating a solid line border.
    SOLID = "solid"


class TkBooleans(Enum):
    """
    Grouped Enum for Tkinter boolean values, encapsulating the various representations of true and false in Tkinter.
    """
    # FALSE = OFF = NO = 0
    FALSE = tk.FALSE
    OFF = tk.OFF
    NO = tk.NO

    # TRUE = ON = YES = 1
    TRUE = tk.TRUE
    ON = tk.ON
    YES = tk.YES


class TkAnchors(Enum):
    """
    Grouped Enum for Tkinter anchor positions, used to specify the alignment of widgets or text.
    """
    N = tk.N
    S = tk.S
    W = tk.W
    E = tk.E
    NW = tk.NW
    SW = tk.SW
    NE = tk.NE
    SE = tk.SE
    NS = tk.NS
    EW = tk.EW
    NSEW = tk.NSEW
    CENTER = tk.CENTER


class TkSticky(Enum):
    """
    Grouped Enum for Tkinter sticky options, used in grid and pack geometry managers to specify how a widget expands
    to fill the available space.
    """
    N = tk.N
    S = tk.S
    W = tk.W
    E = tk.E
    NW = tk.NW
    SW = tk.SW
    NE = tk.NE
    SE = tk.SE
    NS = tk.NS
    EW = tk.EW
    NSEW = tk.NSEW
    CENTER = tk.CENTER

class TkFill(Enum):
    """
    Grouped Enum for Tkinter fill options, used in grid and pack geometry managers to specify how a widget expands
    to fill the available space.
    """
    NONE = "none"
    X = "x"
    Y = "y"
    BOTH = "both"

class TkSides(Enum):
    """
    Grouped Enum for Tkinter side options, used in grid and pack geometry managers to specify the side of the parent
    widget to place the child widget.
    """
    LEFT = "left"
    TOP = "top"
    RIGHT = "right"
    BOTTOM = "bottom"


class TkOrientation(Enum):
    """
    Grouped Enum for Tkinter orientation options, used in widgets like the Scale and Scrollbar to specify the orientation
    of the widget.
    """
    HORIZONTAL = "horizontal"
    VERTICAL = "vertical"

class TkTabs(Enum):
    """
    Grouped Enum for Tkinter tab options, used in widgets like the Notebook to specify the type of tabs to display.
    """
    NUMERIC = "numeric"

class TkWrap(Enum):
    """
    Grouped Enum for Tkinter wrap options, used in widgets like the Text to specify the wrapping behavior.
    """
    CHAR = "char"
    WORD = "word"


class TkAlign(Enum):
    """
    Grouped Enum for Tkinter alignment options, used in widgets like the Text to specify the alignment of text.
    """
    BASELINE = "baseline"

class TkBorderMode(Enum):
    """
    Grouped Enum for Tkinter border mode options, used in widgets like the Text to specify the border mode.
    """
    INSIDE = "inside"
    OUTSIDE = "outside"


class TkSpecialTags(Enum):
    """
    Grouped Enum for Tkinter special tags, marks, and insert positions used in widgets like the Text.
    """
    SEL = "sel"
    SEL_FIRST = "sel.first"
    SEL_LAST = "sel.last"
    END = "end"
    INSERT = "insert"
    CURRENT = "current"
    ANCHOR = "anchor"
    ALL = "all"


class TkWidgetStates(Enum):
    """
    Grouped Enum for Tkinter widget states, used to specify the state of a widget (e.g., normal, disabled, active).
    """
    NORMAL = "normal"
    DISABLED = "disabled"
    ACTIVE = "active"

class TkCanvasState(Enum):
    """
    Grouped Enum for Tkinter canvas states, used to specify the state of a canvas item (e.g., hidden).
    """
    HIDDEN = "hidden"


class TkMenuItemTypes(Enum):
    """
    Grouped Enum for Tkinter menu item types, used to specify the type of menu item (e.g., cascade, checkbutton).
    """
    CASCADE = "cascade"
    CHECKBUTTON = "checkbutton"
    COMMAND = "command"
    RADIOBUTTON = "radiobutton"
    SEPARATOR = "separator"


class TkSelectionModes(Enum):
    """
    Grouped Enum for Tkinter selection modes, used in list boxes to specify the selection mode (e.g., single, browse).
    """
    SINGLE = "single"
    BROWSE = "browse"
    MULTIPLE = "multiple"
    EXTENDED = "extended"

class TkActivestyles(Enum):
    """
    Grouped Enum for Tkinter activestyles, used in list boxes to specify the activestyle (e.g., dotbox, underline).
    """
    DOTBOX = "dotbox"
    UNDERLINE = "underline"


class TkCanvasStyles(Enum):
    """
    Grouped Enum for Tkinter canvas styles, used to specify the style of canvas items (e.g., pieslice, chord).
    """
    PIESLICE = "pieslice"
    CHORD = "chord"
    ARC = "arc"
    FIRST = "first"
    LAST = "last"
    BUTT = "butt"
    PROJECTING = "projecting"
    ROUND = "round"
    BEVEL = "bevel"
    MITER = "miter"


class ViewArguments(Enum):
    """
    Grouped Enum for Tkinter view arguments, used in widgets like the Scrollbar to specify the view arguments.
    """
    MOVETO = "moveto"
    SCROLL = "scroll"
    UNITS = "units"
    PAGES = "pages"


class TkJustify(Enum):
    """
    Enum for text justification in widgets like Label, Entry, Text, etc.
    """
    LEFT = "left"
    CENTER = "center"
    RIGHT = "right"

class TkCompound(Enum):
    """
    Enum for compound options (text+image) in widgets like Button, Label, etc.
    """
    NONE = "none"
    LEFT = "left"
    RIGHT = "right"
    TOP = "top"
    BOTTOM = "bottom"
    CENTER = "center"

class TkCursors(Enum):
    """
    Enum for common cursor names for widgets.
    """
    ARROW = "arrow"
    DOTBOX = "dotbox"
    CROSS = "cross"
    HAND2 = "hand2"
    XTERM = "xterm"
    WATCH = "watch"
    FLEUR = "fleur"
    PLUS = "plus"
    SIZING = "sizing"
    # ...add more as needed

class TkFontWeight(Enum):
    """
    Enum for font weight options in Tkinter font configuration.
    """
    NORMAL = "normal"
    BOLD = "bold"

class TkFontSlant(Enum):
    """
    Enum for font slant options in Tkinter font configuration.
    """
    ROMAN = "roman"
    ITALIC = "italic"

class TkImageFormats(Enum):
    """
    Enum for supported image formats in Tkinter's PhotoImage and BitmapImage.
    """
    GIF = "gif"
    PGM = "pgm"
    PPM = "ppm"
    PNG = "png"
    BMP = "bmp"
    ICO = "ico"
    JPEG = "jpeg"
    # ...add more as supported

# --- ttk-specific enums grouped for clarity ---
class TtkWidgetStates(Enum):
    NORMAL = "normal"
    DISABLED = "disabled"
    ACTIVE = "active"
    READONLY = "readonly"
    PRESSED = "pressed"
    FOCUS = "focus"
    HOVER = "hover"
    ALTERNATE = "alternate"
    SELECTED = "selected"
    BACKGROUND = "background"
    INVALID = "invalid"

class TtkProgressbarMode(Enum):
    DETERMINATE = "determinate"
    INDETERMINATE = "indeterminate"

class TtkNotebookTabPosition(Enum):
    TOP = "top"
    BOTTOM = "bottom"
    LEFT = "left"
    RIGHT = "right"

class TtkTreeviewShow(Enum):
    TREE = "tree"
    HEADINGS = "headings"
    BOTH = "both"

class TtkSizegripSide(Enum):
    BOTTOM = "bottom"
    RIGHT = "right"

# --- Helper to list available ttk themes ---
def get_ttk_themes():
    import tkinter.ttk as ttk
    root = tk.Tk()
    themes = ttk.Style().theme_names()
    root.destroy()
    return themes


def print_enum_options(enum_cls):
    """
    Print all options for a given enum class for quick reference in development.
    Example: print_enum_options(TkJustify)
    """
    print(f"Options for {enum_cls.__name__}:")
    for item in enum_cls:
        print(f"  {item.name}: {item.value}")
    print()


def print_tk_values():
    # Example usage of TkReliefs
    print("TkReliefs:")
    for relief in TkReliefs:
        print(relief, ":", relief.name, ":", relief.value)

    # Example usage of TkBooleans
    print("\nTkBooleans:")
    for boolean in TkBooleans:
        print(boolean, ":", boolean.name, ":", boolean.value)

    # Example usage of TkAnchors
    print("\nTkAnchors:")
    for anchor in TkAnchors:
        print(anchor, ":", anchor.name, ":", anchor.value)

    # Example usage of TkSticky
    print("\nTkSticky:")
    for sticky in TkSticky:
        print(sticky, ":", sticky.name, ":", sticky.value)

    # Example usage of TkFill
    print("\nTkFill:")
    for fill in TkFill:
        print(fill, ":", fill.name, ":", fill.value)

    # Example usage of TkSides
    print("\nTkSides:")
    for side in TkSides:
        print(side, ":", side.name, ":", side.value)

    # Example usage of TkOrientation
    print("\nTkOrientation:")
    for orientation in TkOrientation:
        print(orientation, ":", orientation.name, ":", orientation.value)

    # Example usage of TkTabs
    print("\nTkTabs:")
    for tab in TkTabs:
        print(tab, ":", tab.name, ":", tab.value)

    # Example usage of TkWrap
    print("\nTkWrap:")
    for wrap in TkWrap:
        print(wrap, ":", wrap.name, ":", wrap.value)

    # Example usage of TkAlign
    print("\nTkAlign:")
    for align in TkAlign:
        print(align, ":", align.name, ":", align.value)

    # Example usage of TkBorderMode
    print("\nTkBorderMode:")
    for border_mode in TkBorderMode:
        print(border_mode, ":", border_mode.name, ":", border_mode.value)

    # Example usage of TkSpecialTags
    print("\nTkSpecialTags:")
    for special_tag in TkSpecialTags:
        print(special_tag, ":", special_tag.name, ":", special_tag.value)

    # Example usage of TkWidgetStates
    print("\nTkWidgetStates:")
    for state in TkWidgetStates:
        print(state, ":", state.name, ":", state.value)

    # Example usage of TkCanvasState
    print("\nTkCanvasState:")
    for state in TkCanvasState:
        print(state, ":", state.name, ":", state.value)

    # Example usage of TkMenuItemTypes
    print("\nTkMenuItemTypes:")
    for item_type in TkMenuItemTypes:
        print(item_type, ":", item_type.name, ":", item_type.value)

    # Example usage of TkSelectionModes
    print("\nTkSelectionModes:")
    for mode in TkSelectionModes:
        print(mode, ":", mode.name, ":", mode.value)

    # Example usage of TkActivestyles
    print("\nTkActivestyles:")
    for style in TkActivestyles:
        print(style, ":", style.name, ":", style.value)

    # Example usage of TkCanvasStyles
    print("\nTkCanvasStyles:")
    for style in TkCanvasStyles:
        print(style, ":", style.name, ":", style.value)

    # Example usage of ViewArguments
    print("\nViewArguments:")
    for argument in ViewArguments:
        print(argument, ":", argument.name, ":", argument.value)



# Define a namespace for the theme
namespace eval Theme01 {
    # Procedure to configure styles
    proc applyStyles {} {
        ttk::style theme use clam

        # Configure styles within the namespace
        ttk::style configure Theme.TButton -background #333333 -foreground white -font {Arial 12 bold} -padding 10
        ttk::style map Theme.TButton -background [list active #555555] -foreground [list active white]

        ttk::style configure Theme.TLabel -background #f0f0f0 -foreground #333333 -font {Arial 10} -anchor center

        ttk::style configure Theme.TEntry -fieldbackground #ffffff -foreground #666666 -font {Arial 10 italic}
        ttk::style map Theme.TEntry -fieldbackground [list focus #eeeeee]

        ttk::style configure Theme.TFrame -background #f0f0f0

        ttk::style configure Theme.TCheckbutton -background #f0f0f0 -foreground #333 -font {Arial 10}
    }
}
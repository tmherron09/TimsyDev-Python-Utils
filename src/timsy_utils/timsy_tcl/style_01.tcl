# General style settings
ttk::style theme use "clam"


# Button style
ttk::style configure TButton -background #333333 -foreground white -font {Arial 12 bold} -padding 10
ttk::style map TButton -background [list active #555555] -foreground [list active white]

# Label style
ttk::style configure TLabel -background #f0f0f0 -foreground #333333 -font {Arial 10} -anchor center

# Entry style
ttk::style configure TEntry -fieldbackground #ffffff -foreground #666666 -font {Arial 10 italic}
ttk::style map TEntry -fieldbackground [list focus #eeeeee]

# Frame style
ttk::style configure TFrame -background #f0f0f0

# Checkbutton style
ttk::style configure TCheckbutton -background #f0f0f0 -foreground #333 -font {Arial 10}

from . import layout, bindings
from .constants import *

# Boundaries
width = 480
height = 640
s_width = window.winfo_screenwidth()
s_height = window.winfo_screenheight()
wx = (s_width / 2) - (width / 2)
wy = (s_height / 2) - (height / 2)

# Configuration
window.title("Color Game")
window.geometry("%dx%d+%d+%d" % (width, height, wx, wy))
window.resizable(width=False,height=False)

# Layout
layout.init()
bindings.apply()
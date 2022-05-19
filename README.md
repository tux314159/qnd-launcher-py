# About
An application launcher in Python.
Inspired by <https://github.com/Biont/sway-launcher-desktop/>,
but the code is mine. I personally think Python is a lot easier
to read than a bunch of shell script + sed/awk, so I created this.
It's a quick-and-dirty launcher-- screw you if your arguments or
program paths have spaces and stuff. I might fix this in the
future but I'm too lazy now.

# Features
Very minimal featureset; supports searching an applications directory
for desktop files, parsing them, providing a selection with fzf
and running. IT ASSUMES THAT ALL DESKTOP FILES HAVE A DIFFERENT NAME!

# Dependencies
- Python 3.x
- fzf

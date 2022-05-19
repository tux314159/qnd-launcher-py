# About
An application launcher in Python.
Inspired by <https://github.com/Biont/sway-launcher-desktop/>,
but the code is mine. I personally think Python is a lot easier
to read than a bunch of shell script + sed/awk, so I created this.

# Features
Very minimal featureset; supports searching an applications directory
for desktop files, parsing them, providing a selection with fzf
and running. IT ASSUMES THAT ALL DESKTOP FILES HAVE A DIFFERENT NAME!

# Dependencies
- Python 3.x
- fzf
- a POSIX-compliant shell (if you don't know what that is you probably
  have it)

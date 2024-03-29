#! /usr/bin/python
"""
An application launcher. Works in any environment with fzf
and Python (and a working terminal emulator ;-)).
                       https://xkcd.com/541/^^^^
Inspired by https://github.com/Biont/sway-launcher-desktop
but none of the code was used
"""

import argparse
import glob
import os
import sys
import tempfile
import subprocess

import parsedesktop

# Command-line arguments
parser = argparse.ArgumentParser(description="Application launcher using fzf")
parser.add_argument(
    "-t",
    "--terminal-command",
    default="/usr/bin/kitty -e",  # because I like kitty
    help="some desktop entries need to be executed in the terminal. \
                Use this option to set the terminal command to run those entries. \
                Defaults to /usr/bin/kitty -e",
)
args = parser.parse_args()
term_cmds = args.terminal_command.split(" ")

application_dir = "/usr/share/applications/"
desktop_files = glob.glob(application_dir + "*.desktop")
progs = parsedesktop.parsedesktop(desktop_files)

# Pipe to fzf...
fifo = tempfile.NamedTemporaryFile(mode="w+")
for cprog in progs:
    fifo.write(" " + cprog[0] + "\n")
fifo.seek(0)

progname = subprocess.check_output(
    f"sh -c \"fzf --layout=reverse --preview './get-comment.py {{}}' --preview-window up:3:wrap <{fifo.name}\"",
    shell=True,
).decode("ascii")

# ...and launch that program [ASSUMING NO-ONE HAS THE SAME NAME!!!]
for cprog in progs:
    if progname.strip() != cprog[0].strip():
        continue

    pid = os.fork()
    if pid == 0:
        # double-fork
        pid2 = os.fork()
        if pid2 == 0:
            # reset env
            os.chdir(os.getenv("HOME"))
            os.setsid()
            os.umask(0)
            # Is it supposed to be run in a terminal?
            if cprog[3] == "true":
                os.execvp(
                    term_cmds[0], [term_cmds[0]] + term_cmds[1:] + [cprog[2]]
                )
            else:
                cprogs = cprog[2].split(" ")
                os.execvp(cprogs[0], [cprogs[0]] + cprogs[1:])
        sys.exit(0)
    sys.exit(0)

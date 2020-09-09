#! /usr/bin/python
import argparse
import glob
import sys

import parsedesktop

# Command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument('progname')
args = parser.parse_args()

application_dir = '/usr/share/applications/'
desktop_files = glob.glob(application_dir + '*.desktop')
progs = parsedesktop.parsedesktop(desktop_files)
for cprog in progs:
    if cprog[0].strip() == args.progname.strip():
        print('\033[1m\033[34m' + args.progname.strip() + '\033[0m')
        print(cprog[1].strip())
        sys.exit(0)

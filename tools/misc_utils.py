'''
Copyright (C) 2022 Gagan Malvi

Miscellaneous utilities
'''

import subprocess

def write_profile(profile):
    return subprocess.run(['powerprofilesctl', 'set', profile], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
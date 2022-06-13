'''
Copyright (C) 2022 Gagan Malvi

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

Subject: Miscellaneous utilities
'''

import math
import subprocess
import tools.ioutil as ioutil

# Write power profile
def write_profile(profile):
    return subprocess.run(['powerprofilesctl', 'set', profile], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()

# Convert seconds to HH:MM:SS
def convert_seconds_to_time(seconds):
    seconds = math.ceil(float(seconds))
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "%d:%02d:%02d" % (hour, minutes, seconds)

# Calculate uptime
def calculate_uptime(node):
    return convert_seconds_to_time(ioutil.read_node(node).split(" ")[0])
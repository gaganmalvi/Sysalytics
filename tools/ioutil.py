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

Utilities to read and write to sysfs nodes.
'''

import json

# Write to a node
def write_to_node(node, value):
    with open(node, 'w') as f:
        f.write(str(value))

# Read a node and return the value
def read_node(node):
    with open(node, 'r') as f:
        return f.read().strip()

def write_json(data):
    with open('data.json', 'w') as f:
        f.write(json.dumps(data))
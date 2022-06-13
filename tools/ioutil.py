'''
Copyright (C) 2022 Gagan Malvi

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
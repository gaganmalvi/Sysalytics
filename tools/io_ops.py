'''
Copyright (C) 2022 Gagan Malvi
All rights reserved.

IO operations.
'''

# Write to a node
def write_to_node(node, value):
    with open(node, 'w') as f:
        f.write(str(value))

# Read a node and return the value
def read_node(node):
    with open(node, 'r') as f:
        return f.read()
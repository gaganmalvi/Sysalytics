#!/usr/bin/env python3
'''
Python script for Sysalytics.
This script pulls the following statistics.
- Battery percentage
- Is charging
- Governor
- CPU frequency
- Swappiness
'''
import tools.sysnodes as nodes
import firebase_admin
from firebase_admin import db

# Parse environment variables the easy way
envVars = []
with open('.env', 'r') as f:
    envVars = f.read().splitlines()

# Initialize Realtime Database
databaseURL = envVars[0]
cred = firebase_admin.credentials.Certificate(envVars[1])

default_app = firebase_admin.initialize_app(
    cred,
    {"databaseURL": databaseURL}
)

# Set db reference to root
dbRef = db.reference('/')

# Read all data, write to JSON
data = {
    "battery": {
        "status": nodes.BATTERY_STATUS,
        "capacity": nodes.BATTERY_CAPACITY,
        "model": nodes.BATTERY_MODEL
    },
    "cpu_num_cpus": nodes.num_cpus,
    "cpu_cur_freq": nodes.CPU_CUR_FREQ,
    "cpu_max_freq": nodes.CPU_MAX_FREQ,
    "cpu_min_freq": nodes.CPU_MIN_FREQ,
    "cpu_scal_gov": nodes.CPU_CUR_SGOV,
    "cpu_avl_sgov": nodes.CPU_AVL_SGOV,
    "swappiness": nodes.SWAPPINESS
}

# Write to JSON
dbRef.set(data)
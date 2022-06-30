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

Utility to read and store data from sysfs nodes
'''

import tools.ioutil as ioutil
import subprocess
import os

# Power Profile (read from powerprofilesctl)
POWER_PROFILES_EXECUTABLE = '/usr/bin/powerprofilesctl'
if (os.path.exists(POWER_PROFILES_EXECUTABLE)): POWER_PROFILE = subprocess.run(['powerprofilesctl', 'get'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()

# Swappiness
NODE_SWAPPINESS = "/proc/sys/vm/swappiness"
SWAPPINESS = ioutil.read_node(NODE_SWAPPINESS)

# Uptime
NODE_UPTIME = "/proc/uptime"

# Version
NODE_KERNEL_VERSION = "/proc/sys/kernel/osrelease"

# Battery
BATTERY_PATH = "/sys/class/power_supply/BAT0"
if (os.path.exists(BATTERY_PATH)):
    NODE_BATTERY_STATUS = "/sys/class/power_supply/BAT0/status"
    NODE_BATTERY_CAPACITY = "/sys/class/power_supply/BAT0/capacity"
    NODE_BATTERY_MODEL = "/sys/class/power_supply/BAT0/model_name"
    BATTERY_STATUS = ioutil.read_node(NODE_BATTERY_STATUS)
    BATTERY_CAPACITY = ioutil.read_node(NODE_BATTERY_CAPACITY)
    BATTERY_MODEL = ioutil.read_node(NODE_BATTERY_MODEL)

# No. of CPUs in the system
NODE_NUM_CPUS = "/sys/devices/system/cpu/online"
num_cpus = int(list(ioutil.read_node(NODE_NUM_CPUS))[2]) + 1

# CPU frequencies and governors
NODE_CPU_CUR_FREQ = []
NODE_CPU_MAX_FREQ = []
NODE_CPU_MIN_FREQ = []
NODE_CPU_AVL_SGOV = []
NODE_CPU_CUR_SGOV = []
for i in range(num_cpus):
    NODE_CPU_CUR_FREQ.append("/sys/devices/system/cpu/cpu" + str(i) + "/cpufreq/scaling_cur_freq")
    NODE_CPU_MAX_FREQ.append("/sys/devices/system/cpu/cpu" + str(i) + "/cpufreq/scaling_max_freq")
    NODE_CPU_MIN_FREQ.append("/sys/devices/system/cpu/cpu" + str(i) + "/cpufreq/scaling_min_freq")
    NODE_CPU_AVL_SGOV.append("/sys/devices/system/cpu/cpu" + str(i) + "/cpufreq/scaling_available_governors")
    NODE_CPU_CUR_SGOV.append("/sys/devices/system/cpu/cpu" + str(i) + "/cpufreq/scaling_governor")

CPU_CUR_FREQ = []
CPU_MAX_FREQ = []
CPU_MIN_FREQ = []
CPU_AVL_SGOV = []
CPU_CUR_SGOV = []

for i in range(num_cpus):
    CPU_CUR_FREQ.append(ioutil.read_node(NODE_CPU_CUR_FREQ[i]))
    CPU_MAX_FREQ.append(ioutil.read_node(NODE_CPU_MAX_FREQ[i]))
    CPU_MIN_FREQ.append(ioutil.read_node(NODE_CPU_MIN_FREQ[i]))
    CPU_AVL_SGOV.append(ioutil.read_node(NODE_CPU_AVL_SGOV[i]))
    CPU_CUR_SGOV.append(ioutil.read_node(NODE_CPU_CUR_SGOV[i]))
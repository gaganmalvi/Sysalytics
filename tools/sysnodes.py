'''
Copyright (C) 2022 Gagan Malvi
All rights reserved.

All the /sys nodes that will be used in Sysalytics.
'''

import tools.io_ops as io

# Swappiness
SWAPPINESS = io.read_node("/proc/sys/vm/swappiness")
NODE_SWAPPINESS = "/proc/sys/vm/swappiness"

# Battery
BATTERY_STATUS = io.read_node("/sys/class/power_supply/BAT0/status")
BATTERY_CAPACITY = io.read_node("/sys/class/power_supply/BAT0/capacity")
BATTERY_MODEL = io.read_node("/sys/class/power_supply/BAT0/model_name")

# No. of CPUs in the system
NODE_NUM_CPUS = "/sys/devices/system/cpu/online"
num_cpus = int(list(io.read_node(NODE_NUM_CPUS))[2]) + 1

# CPU frequencies and governors
NODE_CPU_CUR_FREQ = []
NODE_CPU_MAX_FREQ = []
NODE_CPU_MIN_FREQ = []
NODE_CPU_AVL_SGOV = []
for i in range(num_cpus):
    NODE_CPU_CUR_FREQ.append("/sys/devices/system/cpu/cpu" + str(i) + "/cpufreq/scaling_cur_freq")
    NODE_CPU_MAX_FREQ.append("/sys/devices/system/cpu/cpu" + str(i) + "/cpufreq/scaling_max_freq")
    NODE_CPU_MIN_FREQ.append("/sys/devices/system/cpu/cpu" + str(i) + "/cpufreq/scaling_min_freq")
    NODE_CPU_AVL_SGOV.append("/sys/devices/system/cpu/cpu" + str(i) + "/cpufreq/scaling_available_governors")

CPU_CUR_FREQ = []
CPU_MAX_FREQ = []
CPU_MIN_FREQ = []
CPU_CUR_SCALING_GOV = []
CPU_AVL_SGOV = io.read_node("/sys/devices/system/cpu/cpu0/cpufreq/scaling_available_governors") # Only one CPU node is enough to check for available governors

for i in range(num_cpus):
    CPU_CUR_FREQ.append(io.read_node(NODE_CPU_CUR_FREQ[i]))
    CPU_MAX_FREQ.append(io.read_node(NODE_CPU_MAX_FREQ[i]))
    CPU_MIN_FREQ.append(io.read_node(NODE_CPU_MIN_FREQ[i]))
    CPU_CUR_SCALING_GOV.append(io.read_node(NODE_CPU_AVL_SGOV[i]))
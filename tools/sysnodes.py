'''
Copyright (C) 2022 Gagan Malvi
All rights reserved.

All the /sys nodes that will be used in Sysalytics.
'''

# Swappiness
NODE_SWAPPINESS = "/proc/sys/vm/swappiness"

# Battery
NODE_BATTERY_CAPACITY = "/sys/class/power_supply/BAT0/capacity"
NODE_BATTERY_MODEL = "/sys/class/power_supply/BAT0/model_name"
NODE_BATTERY_STATUS = "/sys/class/power_supply/BAT0/status"

# CPU config
NODE_NUM_CPUS = "/sys/devices/system/cpu/online"
NODE_CPU_CUR_FREQ = "/sys/devices/system/cpu/cpu*/cpufreq/scaling_cur_freq"
NODE_CPU_MAX_FREQ = "/sys/devices/system/cpu/cpu*/cpufreq/scaling_max_freq"
NODE_CPU_MIN_FREQ = "/sys/devices/system/cpu/cpu*/cpufreq/scaling_min_freq"
NODE_CPU_SCAL_GOV = "/sys/devices/system/cpu/cpu*/cpufreq/scaling_governor"
NODE_CPU_AVL_SGOV = "/sys/devices/system/cpu/cpu0/cpufreq/scaling_available_governors" # Only one CPU node is enough to check for available governors
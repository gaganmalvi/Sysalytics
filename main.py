'''
Python script for Sysalytics.
This script pulls the following statistics.
- Battery percentage
- Is charging
- Governor
- CPU frequency
- Swappiness
'''
import tools.io_ops as io
import tools.sysnodes as nodes

# Read all data, write to JSON
print("[*] Reading data...")

data = {
    "battery_capacity": nodes.BATTERY_CAPACITY,
    "battery_model": nodes.BATTERY_MODEL,
    "battery_status": nodes.BATTERY_STATUS,
    "cpu_num_cpus": nodes.num_cpus,
    "cpu_cur_freq": nodes.CPU_CUR_FREQ,
    "cpu_max_freq": nodes.CPU_MAX_FREQ,
    "cpu_min_freq": nodes.CPU_MIN_FREQ,
    "cpu_scal_gov": nodes.CPU_CUR_SCALING_GOV,
    "cpu_avl_sgov": nodes.CPU_AVL_SGOV,
    "swappiness": nodes.SWAPPINESS
}

# Write to JSON
print("[*] Writing data to JSON...")
io.write_json(data)
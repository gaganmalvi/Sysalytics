'''
Copyright (C) 2022 Gagan Malvi

Model JSON for the data to be sent to Firebase.
'''

import tools.sysfs_utils as sysfs_utils

def get_system_profile():
    return {
        "battery": {
            "status": sysfs_utils.BATTERY_STATUS,
            "capacity": sysfs_utils.BATTERY_CAPACITY,
            "model": sysfs_utils.BATTERY_MODEL
        },
        "cpu_num_cpus": sysfs_utils.num_cpus,
        "cpu_cur_freq": sysfs_utils.CPU_CUR_FREQ,
        "cpu_max_freq": sysfs_utils.CPU_MAX_FREQ,
        "cpu_min_freq": sysfs_utils.CPU_MIN_FREQ,
        "cpu_scal_gov": sysfs_utils.CPU_CUR_SGOV,
        "cpu_avl_sgov": sysfs_utils.CPU_AVL_SGOV,
        "power_profile": sysfs_utils.POWER_PROFILE,
        "swappiness": sysfs_utils.SWAPPINESS
    }

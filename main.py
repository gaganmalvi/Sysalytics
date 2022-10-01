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

API for application to change system parameters
'''

import psutil
import uvicorn
import os
import tools.ioutil as ioutil
import tools.sysfs_utils as sysfs_utils
import tools.misc_utils as misc_utils
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    """
    Check if server is up.
    """
    return {"status": "OK"}


@app.get("/currentProfile")
async def currentProfile():
    """
    Get current profile.
    """
    if (os.path.exists(sysfs_utils.POWER_PROFILES_EXECUTABLE)):
        return {"profile": sysfs_utils.POWER_PROFILE}
    else:
        return {"profile": "Power profiles are not supported on this system."}


@app.get("/currentSwappiness")
async def currentSwappiness():
    """
    Get current swappiness.
    """
    return {"swappiness": ioutil.read_node(sysfs_utils.NODE_SWAPPINESS)}


@app.get("/currentBatteryStatus")
async def currentBatteryStatus():
    """
    Get current battery status.
    """
    if (os.path.exists(sysfs_utils.BATTERY_PATH)):
        return {"status": ioutil.read_node(sysfs_utils.NODE_BATTERY_STATUS),
                "capacity": ioutil.read_node(sysfs_utils.NODE_BATTERY_CAPACITY),
                "model": ioutil.read_node(sysfs_utils.NODE_BATTERY_MODEL)}
    else:
        return {"status": "Battery is not supported on this system."}


@app.get("/currentGovernor")
async def currentGovernor():
    """
    Get current governor.
    """
    return {"governor": ioutil.read_node(sysfs_utils.NODE_CPU_CUR_SGOV[0])}


@app.get("/getCurrentUptime")
async def getCurrentUptime():
    """
    Get current uptime.
    """
    return {"uptime": misc_utils.calculate_uptime(sysfs_utils.NODE_UPTIME)}


@app.get("/getKernelString")
async def getKernelString():
    """
    Get kernel string.
    """
    return {"kernel": ioutil.read_node(sysfs_utils.NODE_KERNEL_VERSION)}


@app.get("/getKernelStringFull")
async def getKernelString():
    """
    Get full kernel string from /proc/version.
    """
    return {"kernel": ioutil.read_node(sysfs_utils.NODE_FULL_KERNEL_VERSION)}


@app.get("/getCmdline")
async def getCmdline():
    """
    Get full boot command line from /proc/cmdline.
    """
    return {"cmdline": ioutil.read_node(sysfs_utils.NODE_CMDLINE)}


@app.get("/totalCpuUsage")
async def totalCpuUsage():
    """
    Get total CPU usage.
    """
    return {"usage": psutil.cpu_percent()}


@app.get("/RAMusage")
async def RAMusage():
    """
    Get RAM usage.
    """
    return {"usage": psutil.virtual_memory().percent}


@app.post("/setProfile")
async def setProfile(profile: str):
    """
    Set profile
    """
    misc_utils.write_profile(profile)


@app.post("/setSwappiness")
async def setSwappiness(swappiness: int):
    """
    Set swappiness
    """
    ioutil.write_to_node(sysfs_utils.NODE_SWAPPINESS, str(swappiness))

if __name__ == "__main__":
    uvicorn.run(app)

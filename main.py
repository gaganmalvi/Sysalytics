'''
Copyright (C) 2022 Gagan Malvi

API for application to change
- Power Profiles
'''

import uvicorn
import tools.ioutil as ioutil
import tools.sysfs_utils as sysfs_utils
import tools.misc_utils as misc_utils
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
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
    return {"profile": sysfs_utils.POWER_PROFILE}

@app.get("/currentSwappiness")
async def currentSwappiness():
    """
    Get current swappiness.
    """
    return {"swappiness": ioutil.read_node(sysfs_utils.NODE_SWAPPINESS)}

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
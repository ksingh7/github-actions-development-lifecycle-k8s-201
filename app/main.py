from typing import Optional
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"Message": "\o Hello i am an app, that deployed via GitHub Actions on OpenShift. We are LIVE on THE DEV SHOW :)"}

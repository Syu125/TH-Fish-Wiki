from typing import Optional
import uvicorn
import requests

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

app = FastAPI()
app.mount("/home", StaticFiles(directory="static"), name="static")


@app.get("/")
def read_root():
    return RedirectResponse(url="/home/index.html")


@app.get("/hello")
def read_root():
    # Return hello world string
    raise NotImplementedError


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000, log_level="info")

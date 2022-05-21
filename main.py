import uvicorn
import requests
from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from starlette.responses import RedirectResponse

app = FastAPI()
app.mount("/home", StaticFiles(directory="static"), name="static")
fish_watch_api = 'https://www.fishwatch.gov/api/species/'


@app.get("/")
def read_root():
    #change url to "/home/index.html" after part 2
    return RedirectResponse(url="/home/part2.html")


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000, log_level="info")

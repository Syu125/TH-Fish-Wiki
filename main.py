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
    #change url to "/home/index.html" after part 2
    return RedirectResponse(url="/home/part2.html")

@app.get("/hello")
def read_root():
    # Return hardcoded image URLs
    arr = ['https://www.fishwatch.gov/sites/default/files/white%20hake_Calvin%20Alexander_1.jpg', 
        'https://www.fishwatch.gov/sites/default/files/Atlantic%20Chub%20Mackerel_Alessandro%20Duci.jpg', 
        'https://www.fishwatch.gov/sites/default/files/1%20photo-west-coast-region-photo-gallery.jpg',
        'https://www.fishwatch.gov/sites/default/files/atlantic-herring_03.jpg']
    return arr


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5000, log_level="info")

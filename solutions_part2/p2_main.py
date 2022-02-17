@app.get("/hello")
def read_root():
    # Return hello world string
    arr = ['https://www.fishwatch.gov/sites/default/files/white%20hake_Calvin%20Alexander_1.jpg', 
        'https://www.fishwatch.gov/sites/default/files/Atlantic%20Chub%20Mackerel_Alessandro%20Duci.jpg', 
        'https://www.fishwatch.gov/sites/default/files/1%20photo-west-coast-region-photo-gallery.jpg',
        'https://www.fishwatch.gov/sites/default/files/atlantic-herring_03.jpg']
    return arr

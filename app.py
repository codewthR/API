from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()

# Replace 'YOUR_API_KEY' with your actual Google Maps API key
GOOGLE_MAPS_API_KEY = 'API key'
GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/geocode/json'

# Set up templates and static files
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/search")
async def search(query: str):
    if not query:
        return {"error": "No query provided."}

    # Make a request to the Google Maps Geocoding API
    params = {
        'address': query,
        'key': GOOGLE_MAPS_API_KEY
    }
    response = requests.get(GOOGLE_MAPS_API_URL, params=params)
    data = response.json()

    if data['status'] == 'OK':
        results = data['results'][0]
        location_details = {
            'formatted_address': results['formatted_address'],
            'latitude': results['geometry']['location']['lat'],
            'longitude': results['geometry']['location']['lng'],
            'place_id': results['place_id']
        }
        return location_details
    else:
        return {"error": "Location not found."}




# to run enter this --- uvicorn app:app --reload
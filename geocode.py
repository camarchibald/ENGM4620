# geocode.py - Cameron Archibald and Nader Hdeib, 21-02-2025
# Conversion of addresses to coordinates using geocode API

import requests
import json

import os
import re
import time

# Take address string and convert to coordinate tuple
def geocode(address: str) -> tuple[str, str] | tuple[None, None]:
    address = re.sub(r' ', '+', address) # Remove spaces from string
    url = f"https://geocode.maps.co/search?q={address}&api_key={os.environ["GEOCODE_API_KEY"]}"
    time.sleep(1.2) # API calls must be less than 1 per second TODO limit without sleeping
    response = requests.get(url)

    try:
        r = json.loads(response.text)
        if r:
            try:
                result = (r[0]['lat'], r[0]['lon'])
            except:
                result = (None, None)
                print("Bad index on response")
        else:
            result = (None, None)
            print("No coordinates found")
    except:
        result = (None, None)
        print("No response")

    return result
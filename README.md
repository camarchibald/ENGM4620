# Real Estate Cost Analysis Tool
ENGM4602 - Nader Hdeib and Cameron Archibald
## Summary:
This python project is aimed at prospective homeowners in any area looking to view housing prices in recent years and to view predictions of future housing prices, predicted based on previous price trends.
The current phase of the project is a webscraper for realtor.ca which collects current housing listings, and a mapping feature to show the listings.

## Setup:
- Venv

## Features:
The project is interacted with through a command line interface, entering a letter to activate a command. The commands are listed below:

- s: Prompt the user to select a city, scrape data from realtor.ca, and save to that city.
- p: Pickle the data.
- u: Unpickle the data.
- n: Create new city.
- v: Print all listings for a selected city to the command line.
- m: Select a city and generate a map of the listings contained within.

## Scraping:
The code sequence for scraping data is described below:

- Selenium is used to open a Google Chrome window with the realtor.ca page.
- The user must pass the captcha, then enter 'c' in the command line to continue.
- The program then sequentially loads each numbered page of realtor.ca, and the html data is gathered using BeautifulSoup.
- On each page, the prices and street addresses are extracted. The street addresses are passed to the geocode API to return a set of coordinates.
- Each entry is saved in the CityData object.

## Data Structures:
Data for a specific city is stored in a CityData object, which contains a list of dictionaries with keys address, price, latitute, and longitude.
Inside the main program is a list of CityData objects. This can be saved and recalled to memory using 'p' and 'u'.

## Future Improvements:
- Change source of data from realtor.ca to official realtor database for Nova Scotia to allow for more data.
- Use Dr. Hammad's suggested interface for easier gathering of previous trends. Current scraping from realtor.ca is slow and risks blocking.
- Expand on mapping functionality by giving more information by hovering on a datapoint, and improve the price colouring gradient.
- Implement data prediction analysis using ML. Needs lots of past data to work which is a limitation of the current functionality.

# main.py - Cameron Archibald and Nader Hdeib, 21-02-2025
# Webscraping of realtor.ca

import geocode

from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re


# Get URL based on page number TODO allow different cities to be inputted
def get_url(pg) -> str:
    return f"https://www.realtor.ca/map#view=list&CurrentPage={pg}&Sort=6-D&GeoIds=g30_dxgnyskn&GeoName=Halifax%2C%20NS&PropertyTypeGroupID=1&TransactionTypeId=2&PropertySearchTypeId=1&Currency=CAD&HiddenListingIds=&IncludeHiddenListings=false"


# Read max number of pages, removing + if 50+
def find_num_pages(sp: BeautifulSoup) -> int:
    return int((sp.find_all('span', attrs={'class': 'paginationTotalPagesNum'})[2]).text.rstrip("+"))


# Store housing datapoints for a given city
class CityData:
    def __init__(self, name: str):
        self._city_name = name
        self._house_data = []

    # TODO prefer to use dataframe rather than array of dictionaries, no need to store keys 600 times
    # Add a datapoint with address, price, and coordinates
    def add_house(self, address: str, price: str):
        coords = geocode.geocode(address)
        self._house_data.append(
            {'address': address, 'price': int(re.sub(r'[$|,]', '', price)), 'lat': int(coords[0]),
             'lon': int(coords[1])})

    # Search list for entries that match a specific address
    def find_addresses(self, address: str) -> dict | None:
        matches = [house for house in self._house_data if house['address'] == address]
        if matches:
            return matches[0]  # Return first match
        else:
            return None

    # Print all housing data
    def print_data(self):
        for house in self._house_data:
            print(house)

    def get_city_name(self):
        return self._city_name

    def get_house_data(self):
        return self._house_data


# Scraping functionality
def scrape(city: CityData, start_page: int = 1, max_batch_size: int = 600) -> CityData:
    # Open driver
    driver = webdriver.Chrome()
    driver.get(url=get_url(pg=2))

    # Breakpoint here to pass captcha TODO dynamically detect when captcha completed
    char = ''
    while char != 'c':
        char = input("Enter 'c' when captcha complete: ")

    # Read number of pages from html
    num_pages = find_num_pages(sp=BeautifulSoup(driver.page_source, 'html.parser'))

    count = 1  # How many houses have been found
    count_new = 1  # How many new houses have been added to list
    page = start_page  # Page to look at

    # Go through pages
    while page <= num_pages:
        # Because data collection is slow, exit before all 50 pages have been read to minimize data loss
        if count_new > max_batch_size:
            break

        # Open driver
        driver.get(url=get_url(pg=page))
        driver.refresh()
        time.sleep(2)  # Wait for page to load TODO make more intelligent waiting based on the driver itself

        # Get source code
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Find all cards with price element
        entries_on_page = soup.find_all('div', attrs={'class': 'listingCardPrice'})

        # Save price and address (address is two siblings away from price)
        # TODO filter out land
        for price_entry in entries_on_page:
            print(price_entry.text)
            print(price_entry.next_sibling.next_sibling.text)
            print(count)

            if city.find_addresses(address=price_entry.next_sibling.next_sibling.text) is None:
                city.add_house(address=price_entry.next_sibling.next_sibling.text, price=price_entry.text)
                count_new += 1
            else:
                print("Repeated house")

            count += 1

        page += 1

    driver.quit()
    return city

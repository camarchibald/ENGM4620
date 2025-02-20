from bs4 import BeautifulSoup
from selenium import webdriver
import time


# Get URL based on page number TODO allow different cities to be inputted
def get_url(pg):
    return f"https://www.realtor.ca/map#view=list&CurrentPage={pg}&Sort=6-D&GeoIds=g30_dxgnyskn&GeoName=Halifax%2C%20NS&PropertyTypeGroupID=1&TransactionTypeId=2&PropertySearchTypeId=1&Currency=CAD&HiddenListingIds=&IncludeHiddenListings=false"


# Open driver on first page
driver = webdriver.Chrome()
driver.get(url=get_url(pg=1))
pass  # Breakpoint here to pass captcha TODO dynamically detect when captcha completed

count = 1  # How many houses have been found

# Go through pages TODO read the max number of pages at the start and search all of it
for page in range(1, 11):
    driver.get(url=get_url(pg=page))
    driver.refresh()
    time.sleep(2)  # Wait for page to load TODO make more intelligent waiting based on the driver itself

    # Get source code and find all cards with price element
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    table = soup.find_all('div', attrs={'class': 'listingCardPrice'})

    # Print price and address (address is two siblings away from price)
    # TODO store this information
    # TODO filter out land
    for entry in table:
        print(entry.text)
        print(entry.next_sibling.next_sibling.text)
        print(count)
        count += 1

pass

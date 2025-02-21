from bs4 import BeautifulSoup
from selenium import webdriver
import time
import re
import pickle


# Get URL based on page number TODO allow different cities to be inputted
def get_url(pg) -> str:
    return f"https://www.realtor.ca/map#view=list&CurrentPage={pg}&Sort=6-D&GeoIds=g30_dxgnyskn&GeoName=Halifax%2C%20NS&PropertyTypeGroupID=1&TransactionTypeId=2&PropertySearchTypeId=1&Currency=CAD&HiddenListingIds=&IncludeHiddenListings=false"

# Read max number of pages
def find_num_pages(sp: BeautifulSoup) -> int:
    # TODO use rstrip
    return int(re.sub(r'\+', '',(sp.find_all('span', attrs={'class': 'paginationTotalPagesNum'})[2]).text))

class CityData:
    def __init__(self, name: str):
        self.city_name = name
        self.house_data = []

    # TODO prefer to use dataframe rather than array of dictionaries, no need to store keys 600 times
    def add_house(self, address: str, price: str):
        self.house_data.append({'address': address, 'price': int(re.sub(r'[$|,]', '', price))})


def scrape(city_name: str) -> CityData:
    city = CityData(city_name)

    # Open driver on first page
    driver = webdriver.Chrome()
    driver.get(url=get_url(pg=1))

    char = ''
    while char != 'c':
        char = input("Enter 'c' when captcha complete: ")
    pass  # Breakpoint here to pass captcha TODO dynamically detect when captcha completed

    count = 1  # How many houses have been found
    page = 1
    num_pages = 1
    found_num_pages = False

    # Go through pages
    while page <= num_pages:
        driver.get(url=get_url(pg=page))
        driver.refresh()
        time.sleep(2)  # Wait for page to load TODO make more intelligent waiting based on the driver itself

        # Get source code
        soup = BeautifulSoup(driver.page_source, 'html.parser')

        # Read max number of pages and set the loop limit
        if not found_num_pages:
            num_pages = find_num_pages(sp=soup)
            found_num_pages = True


        # Find all cards with price element
        entries_on_page = soup.find_all('div', attrs={'class': 'listingCardPrice'})

        # Print price and address (address is two siblings away from price)
        # TODO store this information
        # TODO filter out land
        for price_entry in entries_on_page:
            city.add_house(address=price_entry.next_sibling.next_sibling.text, price=price_entry.text)

            print(price_entry.text)
            print(price_entry.next_sibling.next_sibling.text)
            print(count)
            count += 1

        page += 1

    driver.quit()
    return city

# TODO make this a function
# TODO allow for different cities to be inputted
command = ''
while command != 'q':
    command = input('Enter command: ')
    match command:
        case 's':
            halifax = scrape(city_name="Halifax")
            pass
        case 'p':
            f = open('halifax', 'wb')
            if halifax:
                pickle.dump(halifax, f)
            f.close()
            pass
        case 'u':
            f = open('halifax', 'rb')
            read_data = pickle.load(f)
            f.close()
            if read_data:
                for house in read_data.house_data:
                    print(house)
            pass

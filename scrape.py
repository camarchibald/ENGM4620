import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Chrome

# Fetch the web page


headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
URL = "https://www.realtor.ca/map#view=list&CurrentPage=1&Sort=6-D&GeoIds=g30_dxgnyskn&GeoName=Halifax%2C%20NS&PropertyTypeGroupID=1&TransactionTypeId=2&PropertySearchTypeId=1&Currency=CAD&HiddenListingIds=&IncludeHiddenListings=false"
#URL = "https://www.google.com"
#URL = "https://www.realtor.ca"
driver = Chrome()
driver.get(url=URL)
pass
pass
soup = BeautifulSoup(driver.page_source, 'html.parser')
table = soup.find_all('div', attrs = {'class':'listingCardPrice'})
table_addr = soup.find_all('div', attrs = {'class':'listingCardAddress'})
print(table)
for entry in table:
    print(entry.text)
    print(entry.next_sibling.next_sibling.text)
pass
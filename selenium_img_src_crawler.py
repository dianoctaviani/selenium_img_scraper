
from typing import ItemsView
from pandas.core.frame import DataFrame
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time


chromedriver = ChromeDriverManager().install()
keywords = pd.read_csv('input/scientific_botanical_names_veggies_fruits.csv', sep=",")

def search_google(search_query):
    search_url = f"https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q={search_query}"

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--disable-web-security')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument('--allow-cross-origin-auth-prompt')

    browser = webdriver.Chrome(chromedriver, options=options)

    # Open browser to begin search
    browser.get(search_url)

    # XPath for the 1st image that appears in Google: //*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img
    img_box = browser.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
    # Click on the thumbnail
    img_box.click()

    # XPath of the image display 
    fir_img = browser.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img')

    # Wait between interaction
    time.sleep(3)
    fir_img.click()

    # Retrieve attribute of src from the element
    img_src = fir_img.get_attribute('src')

    return img_src


# Creating header for file containing image source link 
with open("output/links/img_src_links.csv", "w") as outfile:
    outfile.write("search_terms|src_link\n")

# Loops through the list of search input
for keyword in keywords['scientific_names']:
    try:
        link = search_google(keyword)
        with open("output/links/img_src_links.csv", "a") as outfile:
            outfile.write(f"{keyword}|{link}\n")
    except Exception as e: 
        print(e)

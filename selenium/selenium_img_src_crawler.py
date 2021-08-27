
from typing import ItemsView
from pandas.core.frame import DataFrame
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


keywords = pd.read_csv('scientific_botanical_names_veggies_fruits.csv')
df = pd.DataFrame(columns=['search_terms','src_base64'])

def search_google(search_query):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    search_url = f"https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q={search_query}"
    images_url = []

    # Open browser to begin search
    browser.get(search_url)
    elements = browser.find_elements_by_class_name('rg_i')

    # XPath for the 1st image that appears in Google: //*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img
    img_box = browser.find_element_by_xpath('//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
    # Click on the thumbnail
    img_box.click()

    # XPath of the image display 
    fir_img = browser.find_element_by_xpath('//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div[1]/a/img')
    # Retrieve attribute of src from the element
    img_src = fir_img.get_attribute('src')

    # Quit session and terminate browser
    browser.close()
    browser.quit()

    return(img_src)

# Function to write the DataFrame of the image source links (Base 64)
def write_df(a, b):
    row = [a, b]
    df.loc[len(df)] = row
    df.append(row, ignore_index=True)
    df.to_csv("img_src_links.csv", index=False, mode='w', header=False, sep='|')


for i in keywords['scientific_names']:
    items = search_google(i)
    write_df(i, items)

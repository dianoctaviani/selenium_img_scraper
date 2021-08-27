# Google Image Scraping using Selenium
This repo was created for Tutorial Blog: https://medium.com/@dian.octaviani/method-1-4-automation-of-google-image-scraping-using-selenium-3972ea3aa248

This tutorial explains how to programatically scrape Google Images using Selenium with a combination of Python and Chrome Web Driver. Providing a practical example of how Selenium can be applied. This post also aims to explain the basics of Selenium and how it works.

## Project Background
We currently have a dataset containing 118 searchable keywords of both common and scientific botanical names of edible vegetables and fruits. Using the list of scientific names, we need 1 visual representation of each vegetable or fruit to build an image-based detection model.

I've compiled the dataset into a .csv and made it available for downloads on Kaggle: https://www.kaggle.com/dianoctaviani/scientific-botanical-names-of-fruits-vegetables


## Setup
Install Selenium using PyPi:
```
$ pip3 install selenium
```
Install the WebDriver using PyPi:
```
$ pip3 install webdriver_manager
```

## Structure
There are two python scripts used for this tutorial, it is:
```
1. selenium_img_src_crawler.py 
2. selenium_img_downloader.py 
```
The above scripts required to be run sequentially. 
```
.
└── auto_img_scraper/
    ├── blog/
    │   └── selenium_blog
    ├── input/
    │   └── scientific_botanical_names_veggies_fruits.csv
    ├── output/
    │   ├── images/
    │   │   └── *.png
    │   └── links/
    │       └── img_src_links.csv
    ├── selenium_img_src_crawler.py
    ├── selenium_img_downloader.py
    ├── .gitignore
    ├── README.md
    └── LICENSE
```

## Tutorial
Refer to the blog for the step-by-step tutorial: https://medium.com/@dian.octaviani/method-1-4-automation-of-google-image-scraping-using-selenium-3972ea3aa248
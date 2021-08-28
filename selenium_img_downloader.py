import pandas as pd
import urllib.request
from urllib.request import Request, urlopen
import base64
import logging
import socket

# List of img src for the image downloads
img_src = pd.read_csv('output/links/img_src_links.csv', sep='|')
socket.setdefaulttimeout(15)

# Function to check if result is base64
def check_for_b64(source):
    possible_header = source.split(',')[0]
    if possible_header.startswith('data') and ';base64' in possible_header:
        image_type = possible_header.replace('data:image/', '').replace(';base64', '')
        return image_type
    return False

# Function to perform the image downloads
def download_img():
    logging.basicConfig(filename='logging/logging.log', filemode='w', format='%(name)s | %(levelname)s | %(message)s')
    
    for row in img_src.itertuples(index=True, name='Pandas'):
        # Check if src content is base64 instead of URL link
        is_b64 = check_for_b64(row.src_link)
        # If it is b64, then retrieve the image with the following if statement
        if is_b64:
            image_format = is_b64
            content = base64.b64decode(row.src_link.split(';base64')[1])
            try:
                with open('output/images/'+row.search_terms+'.png'.format(image_format), 'wb') as f:
                    f.write(content)
            except Exception as e:
                logging.error(''+row.search_terms+' | '+row.src_link+' | '+str(e)+'')
        # Else, if it is a direct URL, then perform urlretrieve to download the image
        else:
            try:
                urllib.request.urlretrieve(''+row.src_link+'', 'output/images/'+row.search_terms+'.png')
            except Exception as e: 
                logging.error(''+row.search_terms+' | '+row.src_link+' | '+str(e)+'')

# Calling the image download function
download_img()
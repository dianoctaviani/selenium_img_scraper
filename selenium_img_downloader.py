import pandas as pd
import urllib.request


def download_img():
    img_src = pd.read_csv('m1_selenium/output/links/img_src_links.csv', sep='|')

    url = img_src.iloc[:, 1] 
    keyword = img_src.iloc[:, 0] 

    urllib.request.urlretrieve(url, ''+keyword+'.png')

def check_if_result_b64(source):
    possible_header = source.split(',')[0]
    if possible_header.startswith('data') and ';base64' in possible_header:
        image_type = possible_header.replace('data:image/', '').replace(';base64', '')
        return image_type
    return False


download_img()
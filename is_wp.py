import requests
from bs4 import BeautifulSoup

def is_wordpress_meta(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")
    for meta in soup.findAll("meta"): 
        metaname = meta.get('name', '').lower() 
        #print ('>>>',metaname) 
        if metaname == 'generator': 
            if "WordPress" in meta.get('content'): 
                print (f'{link} seems wp!! ')
                print (meta.get('content')) 
                return True 
            else:
                return False 
    return True


def is_wordpress(link):
    if 'http' in link:
        return is_wordpress_meta(link)
    else:
        print ("not http*")
        return False

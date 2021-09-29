import requests
from bs4 import BeautifulSoup
from urllib.parse import urlsplit
import csv
from is_wp import *
#initiation

SEED_URL = "https://10web.io/blog/10-awesome-websites-made-with-wordpress/"
with open('blacklist.csv') as csvfile:
    blacklist = list(csv.reader(csvfile,delimiter=','))[0] #this returns list of list

print(blacklist)



def get_all_links(soup):
    global blacklist
    links=soup.find_all("a",href=True)
    all_links=[]
    for link in links:
        #print (link)
        add=link["href"]
        if 'http' not in add:
            print ('not an http!')
            continue
        if type(add) == type(None): 
            print (f'EROR===== {add}')
            continue
        
        if not any(blacked in add for blacked in blacklist):
            print(f'link added {add}')
            all_links.append(add)
            blacklist.append(urlsplit(add).hostname) #1 solo hostname

    return all_links
    


def save_wp(wps):
    with open('wordpresses.csv', mode='a') as file_:
        writer = csv.writer(file_)
        writer.writerow(wps)

#main

page = requests.get(SEED_URL)
soup = BeautifulSoup(page.content, "html.parser")
wordpresses=[]
every_link = get_all_links(soup)
for link in every_link:
    if is_wordpress(link):
        # print(urlsplit(link).hostname)
        wordpresses.append(link)
        #save_wp(wordpresses)

save_wp(wordpresses)
#save blacklist
# with open('blacklist.csv', mode='w') as file_:
#     writer = csv.writer(file_)
#     writer.writerow(blacklist)


#check ssl verification errors

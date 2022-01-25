import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# funkcija ki vrne točno določeno vrstico s strani
def nepremicne_web():   
    url = 'https://www.nepremicnine.net/oglasi-oddaja/ljubljana-mesto/stanovanje/'
    response = requests.get(url)
    print(response) #If response==200 -> OK

    soup = BeautifulSoup(response.text, "html.parser")
    one_a_tag = soup.findAll('a')[170] ##returns 170 apartment 
    #all_tag = soup.findAll('a') #For testing ##find all hyperlinks<a>
    link = one_a_tag['href']
    print(link) #Check the path and add it below (download_url...)

    download_url = 'https://www.nepremicnine.net/'+link
    return download_url #Returns link

# debug: nepremicne_web()


# funkcija, ki poišče vse oglase (div->seznam->h2->data-href)
def Neprweb():
    url = 'https://www.nepremicnine.net/oglasi-oddaja/ljubljana-mesto/stanovanje/'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    container = soup.find('div', class_= 'seznam')

    for link in container.findAll('h2'):
        #print(link.get('data-href'))
        addlink = link.get('data-href')
        print('https://www.nepremicnine.net'+addlink)
        #time.sleep(1)
             
# debug: Neprweb()


# funkcija, ki poišče zadnji oglas (div->seznam->h2->data-href)
def Neprweb1():
    url = 'https://www.nepremicnine.net/oglasi-oddaja/ljubljana-mesto/stanovanje/?s=16'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    container = soup.find('div', class_= 'seznam')
    

    for link in container.findAll('h2')[:1]:
        #print(link.get('data-href'))
        addlink = link.get('data-href')
        print('https://www.nepremicnine.net'+addlink)
        download_url = 'https://www.nepremicnine.net/'+addlink
        return download_url         

# debug: Neprweb1()






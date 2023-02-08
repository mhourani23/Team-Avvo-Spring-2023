import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

def scrape(state, county, sector):
  '''
  Given inputs of state, county, sector of law (all lowercase and - instead of spaces)
  Returns a list which contains names of lawyers 
  The pages are the # of pages that exist, currently hardcoded but if the page doesnt exist it wont error out badly
  '''
    pages = ["", '?stq=20', '?stq=40', '?stq=60', '?stq=80', '?stq=100']
    link = f"https://lawyers.findlaw.com/lawyer/firm/{sector}/{county}/{state}"
    lawyers = []
    for add in pages:
        scrape = requests.get(link+add)
        Soup = BeautifulSoup(scrape.text, 'lxml')
        for h2 in Soup.find_all('h2', {"class":"listing-details-header"}): 
            lawyers.append(h2.text)
    return lawyers

# Example run of the function
# scrape('california', 'los-angeles-county','intellectual-property-law')

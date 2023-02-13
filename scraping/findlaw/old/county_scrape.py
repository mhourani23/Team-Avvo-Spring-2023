import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

def county_scrape(state):
    '''
    Takes in state in lowercase (e.g. 'california') and returns all counties covered by findlaw in that state.
    '''
    link = f"https://lawyers.findlaw.com/lawyer/stateallcounties/{state}"
    scrape = requests.get(link)
    Soup = BeautifulSoup(scrape.text, 'lxml')
    lsts = Soup.find_all('div', {'class':"small-12 large-4 columns links"})
    counties = []
    # Need to iterate over len(lsts) because they break counties into multiple div tags
    for i in range(len(lsts)):
        for j in lsts[i].find_all('a'):
            counties.append(j.text)
    return counties
    

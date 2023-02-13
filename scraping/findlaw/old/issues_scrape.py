import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

def issues_scrape():
    link = 'https://lawyers.findlaw.com/lawyer/practice.jsp'
    scrape = requests.get(link)
    Soup = BeautifulSoup(scrapee.text, 'lxml')
    lsts = Soup.find_all('div', {'class':"small-12 large-4 columns links"})

    issues = []

    # This is good, it exempts the headers for each category
    for i in range(len(lsts)):
        for j in lsts[i].find_all('a'):
            issues.append(j.text)
    return issues
  
  # Example Usage
  #legal_issues = issues_scrape()

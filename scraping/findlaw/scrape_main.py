def scrape_findlaw(state):
    df = pd.DataFrame() #(columns = ['State', 'County','Lawyer'])
    counties = county_scrape(state)
    # county_scrape returns counties in the form "Alpine County, CA" but need it in form "alpine-county" so do following transformation
    counties = [county.split(',')[0].lower().replace(' ','-') for county in counties]
    for county in counties:
        for issue in issues:
        #issue = 'intellectual-property-law'
            lawyers = scrape(state, county, issue)
            #df_1 = pd.DataFrame(columns = ['State', 'County','Lawyers','Issue'])
            df_1 = pd.DataFrame()
            df_1['Lawyers'] = lawyers
            df_1['Issue'] = [issue]* len(lawyers)
            df_1['County'] = [county]* len(lawyers)
            df_1['State'] = [state]* len(lawyers)
            df = pd.concat([df,df_1])
    return df

#scrape_findlaw('california')

def issues_scrape():
    link = 'https://lawyers.findlaw.com/lawyer/practice.jsp'
    scrape = requests.get(link)
    Soup = BeautifulSoup(scrape.text, 'lxml')
    lsts = Soup.find_all('div', {'class':"small-12 large-4 columns links"})

    issues = []

    # This is good, it exempts the headers for each category
    for i in range(len(lsts)):
        for j in lsts[i].find_all('a'):
            issues.append(j.text)
    return issues

def county_scrape(state):
    '''
    Takes in state in lowercase (e.g. 'california') and retusn all counties covered by findlaw in that state.
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

def scrape(state, county, sector):
    pages = ["", '?stq=20', '?stq=40', '?stq=60', '?stq=80', '?stq=100']
    link = f"https://lawyers.findlaw.com/lawyer/firm/{sector}/{county}/{state}"
    lawyers = []
    for add in pages:
        scrape = requests.get(link+add)
        Soup = BeautifulSoup(scrape.text, 'lxml')
        for h2 in Soup.find_all('h2', {"class":"listing-details-header"}): 
            lawyers.append(h2.text)
    return lawyers

# **Findlaw Scraping**  

Currently have scraper that returns lawyers on platform given the county, state, and sector.  
Finished scraper that gets all different types of legal issues offered on findlaw.  
Finished county scraper when given state name.

## Website Order: State -> County -> Issue  
### Using county level the link order is 
```
Legal Issue -> County -> State
https://lawyers.findlaw.com/lawyer/firm/banking-finance-law/marin-county/california
```

Working on:  
Is it possible to combine county scraper into the normal scraper so u only need to give state? Just seeing if I will get throttled.  

Return dataframe with lawyers but also state and county columns.

Future:  
Some way to extract states/territories of the USA. Could scrape from website but in weird format.  

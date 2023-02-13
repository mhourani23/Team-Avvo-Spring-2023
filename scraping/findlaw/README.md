# **Findlaw Scraping**  

Current scraper gets all lawyers (given state) and returns a df that has columns legal issue, state, county, lawyer.  
If this is done for a large state (like California) the df is around 1500 rows.  
Not sure what the pandas limit is for rows in a df.

### **All of the supporting python files are in the ```"old"``` folder.**

## Website Order: State -> County -> Issue  
### Using county level the link order is 
```
Legal Issue -> County -> State
https://lawyers.findlaw.com/lawyer/firm/banking-finance-law/marin-county/california
```

Future:  
Some way to extract states/territories of the USA. Could scrape from website but in weird format.  

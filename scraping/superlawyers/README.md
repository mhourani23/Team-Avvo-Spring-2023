# **Super Lawyers Scraper**


**Link Order**
```
Legal Issue -> State -> Locale*
https://attorneys.superlawyers.com/bankruptcy/california/los-angeles/

*Takes city as the input, but LA and Claremont have same results, so might implicitly use county.
```  

## **HTML Issues**  
4 Different div tags for different results:  
1. topspots
1. poap results
1. eoap results
1. basic results  

**This is for the first page only, for some reason every page after is topspots and basic results.

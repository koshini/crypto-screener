# crypto-screener
A web scraper that scrapes various websites for cryptocurrency info and writes to cvs files.
coinmarketcap_gainers.py scrapes the top 7d gainers from https://coinmarketcap.com/gainers-losers/ and writes to gainers.csv.
ICOData.py scrapes all completed ICOs from https://www.icodata.io/ICO/completed and writes to ICOData.csv

# 
We can create a grading system for potentially top ICOs by using these information from previous highly successful ICOs (see https://www.icodata.io/ICO/completed) Select highest to lowest for return
 
1. Rating of 4/5 or 8/10 or A, HIGH and above across at least 2 ICO rating platforms
2. Less than or equal to 20MM being raised (score of 9/10 for less than or equal to10MM and score of 7,8 or 9 for greater than 10MM and less than 20MM)
3. Total coin supply vs circulation (the lower the better)
4. No restrictions to Canadians (important cause otherwise, we can't partake)
5. MVP
6. Partnership and Team (averaged rating out of 10)
7. Take an average of all the parameters and only invest in ones with 7/10 or higher


import requests
import urllib3
from web_scrapte_helper import WebScraperHelper



def main():
    # Instantiate web scraper
    scraper = WebScraperHelper()
    content = scraper.init("https://coinmarketcap.com/gainers-losers/")





if __name__ == "__main__":
    main()

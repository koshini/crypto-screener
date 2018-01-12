import requests
import urllib3

from bs4 import BeautifulSoup

class WebScraperHelper:
    def __init__(self):
        self.soup = None

    def init(self, page_url):
        gainers_page = requests.get(page_url, verify=False)
        if gainers_page.status_code != 200:
            return None
        self.soup = BeautifulSoup(gainers_page.content, 'html.parser')
        return 'ok'
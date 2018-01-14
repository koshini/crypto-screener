import pandas as pd
import requests
from bs4 import BeautifulSoup


def main():
    gainers_page = requests.get("https://coinmarketcap.com/gainers-losers/")
    print(str(gainers_page.status_code))
    soup = BeautifulSoup(gainers_page.content, 'html.parser')

    # Find the 7d gainers table
    table = soup.find(id="gainers-7d")
    table_body = table.find('tbody')
    gainer_list = table_body.find_all('tr')

    # Create a panda dataframe
    headers = ['#', 'Name', 'Symbol', 'Volume(24h)', 'Price(USD)', 'Price(BTC)', '% 7d', 'link']
    df = pd.DataFrame(columns=headers, index=range(0, len(gainer_list)))
    row_marker = 0

    # Parse row by row
    for gainer in gainer_list:
        data = gainer.find_all('td')
        columns = []
        btc_price = 0
        for td in data:
            text = td.text.strip()
            columns.append(text)
        # Find btc price
        btc_price = gainer.find('a',class_='price')['data-btc']
        # Find link to the coin page
        link = gainer.find('a')['href']
        link = 'https://coinmarketcap.com/currencies' + link
        # Insert btc price before '% 7d'
        columns.append(columns[5])
        columns[5] = btc_price
        # Add link
        columns.append(link)

        # Index data to df
        col_marker = 0
        for column in columns:
            df.iat[row_marker,col_marker] = column
            col_marker += 1
        if len(columns) > 0:
            row_marker += 1

    # Write dataframe to a local csv file for now
    df.to_csv('gainers.csv', encoding='utf-8', index=False)


if __name__ == "__main__":
    main()

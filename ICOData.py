import pandas as pd
import requests
from bs4 import BeautifulSoup


def main():
    gainers_page = requests.get("https://www.icodata.io/ICO/completed")
    print(str(gainers_page.status_code))
    soup = BeautifulSoup(gainers_page.content, 'html.parser')

    # Find the 7d gainers table
    table = soup.find(id="table")
    thead = table.find('thead')
    headers = []
    for th in thead.tr.find_all('th'):
        headers.append(th.text)

    table_body = table.find('tbody')
    gainer_list = table_body.find_all('tr')

    # Create a panda dataframe
    df = pd.DataFrame(columns=headers, index=range(0, len(gainer_list)))
    row_marker = 0

    # Parse row by row
    for ICO in gainer_list:
        data = ICO.find_all('td')
        columns = []
        for td in data:
            text = td.text.strip()
            columns.append(text)
        # Find link to the ICO page
        link = data[0].find('a')['href']
        link = 'https://www.icodata.io' + link
        # Add link
        columns[0] = link

        # Index data to df
        col_marker = 0
        for column in columns:
            df.iat[row_marker,col_marker] = column
            col_marker += 1
        if len(columns) > 0:
            row_marker += 1

    # Write dataframe to a local csv file for now
    df.to_csv('ICOData.csv', encoding='utf-8', index=False)


if __name__ == "__main__":
    main()

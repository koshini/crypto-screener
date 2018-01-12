import pygsheets
import pandas as pd


#authorization
gc = pygsheets.authorize(service_file='creds.json')

# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['test col'] = ['btc', 'eth', 'ayyy']

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sh = gc.open('Crypto Screener')

#select the first sheet
wks = sh[1]

#update the first sheet with df, starting at cell B2.
wks.set_dataframe(df,(1,1))
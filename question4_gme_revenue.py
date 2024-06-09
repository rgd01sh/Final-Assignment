import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for GameStop revenue data
url = 'https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract table data
tables = soup.find_all('table')
gme_revenue = pd.read_html(str(tables))[0]

# Display the last five rows
print(gme_revenue.tail())

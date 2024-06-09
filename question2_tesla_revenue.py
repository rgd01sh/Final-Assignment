import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL for Tesla revenue data
url = 'https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Extract table data
tables = soup.find_all('table')
tesla_revenue = pd.read_html(str(tables))[0]

# Display the last five rows
print(tesla_revenue.tail())

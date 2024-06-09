import yfinance as yf
import pandas as pd

# Download GameStop stock data
gme_data = yf.download('GME')

# Reset the index
gme_data.reset_index(inplace=True)

# Display the first five rows
print(gme_data.head())

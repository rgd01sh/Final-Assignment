import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Download GameStop stock data
gme_data = yf.download('GME')

# Reset the index
gme_data.reset_index(inplace=True)

# Define the make_graph function
def make_graph(data, title):
    plt.figure(figsize=(10, 5))
    plt.plot(data['Date'], data['Close'])
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.grid(True)
    plt.show()

# Plot GameStop stock graph
make_graph(gme_data, 'GameStop Stock Price')

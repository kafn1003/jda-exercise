import yfinance as yf               # to download data from Yahoo! finance
import streamlit as st              # to create the webpage
import pandas as pd                 # for data analysis and manipulation
import matplotlib.pyplot as plt     # for plotting

# Loading the BTC-USD Data using yfinance
btc_data = yf.download('BTC-USD')

# Accessing the Closing Prices only
closing_price = btc_data['Close'].round(3).resample('W-FRI', closed='left', label='left').last().to_frame()

# Calculating the percentage change
closing_price['Percentage Change'] = closing_price.pct_change() * 100

# Counting the number of weeks with price movement
five_percent = (closing_price['Percentage Change'].abs() > 5).sum()
ten_percent = (closing_price['Percentage Change'].abs() > 10).sum()

# Main Code
st.title('BTC Price Data in US')
st.markdown("***")
st.subheader("BTC-USD Data via yfinance \n(from September 17, 2014 to present)")
st.write(btc_data)

# Closing Prices
st.subheader('BTC-USD Closing Price (Weekly)')
st.write(closing_price)

# Line Plot for the Closing Prices
plt.figure(figsize=(10, 6))
plt.plot(btc_data.index, btc_data['Close'])
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.title('BTC Closing Price over Time')
st.pyplot(plt)

st.markdown("***")

# Price Movements/Percent Changes
st.subheader('Weeks with Price Movement')
st.write(f"Weeks with more than 5% price movement: {five_percent}")
st.write(f"Weeks with more than 10% price movement: {ten_percent}")

# Bar Plot for the Price Movements/Percent Changes
plt.figure(figsize=(8, 6))
movement_counts = pd.Series([five_percent, ten_percent], index=['> 5%', '> 10%'])
movement_counts.plot(kind='bar')
plt.xlabel('Price Movement')
plt.ylabel('Count')
plt.title('Number of Weeks with Price Movement')
st.pyplot(plt)
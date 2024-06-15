import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the stock **closing price** and ***volume*** of Nvidia!

""")

# User input for the ticker symbol
tickerSymbol = st.text_input("Enter a stock ticker symbol (e.g., NVDA):", "NVDA").upper()

# User input for the start and end dates
start_date = st.date_input("Enter Start Date", pd.to_datetime("2014-05-31"))
end_date = st.date_input("Enter End Date", pd.to_datetime("2024-05-31"))


#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period= '1d', start = start_date, end = end_date)
# Open, High, Low, Close, Volume, Dividends,  Stock Splits


st.write("""
         ## Closing Price
         """)
st.line_chart(tickerDf.Close)
         
st.write("""
         ## Volume
         """)
st.line_chart(tickerDf.Volume)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas_datareader as data
import yfinance as yf

from keras.models import load_model
import streamlit as st

start = '2010-01-01'
end = '2019-12-01'


st.title("Stock Market trend")

user_input = st.text_input('Enter ticker', 'TSLA')
# Use yfinance to fetch stock data
df = yf.download(user_input, start=start, end=end)

#Describe the data

st.subheader('Data from 2010 to 2019')
st.write(df.describe())
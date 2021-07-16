import streamlit as st
import yfinance as yf
import pandas as pd
import cufflinks as cf
import datetime

# App title
st.markdown('''# Stock Market Price''')
st.write('---')

st.sidebar.subheader("Date and Stock Listing")
start_date = st.sidebar.date_input("Start Date", datetime.date(2019, 1, 1))
end_date = st.sidebar.date_input("End date", datetime.date(2021, 6, 29))

ticker_list = pd.read_csv('https://raw.githubusercontent.com/vray797/Financial-Dashboard/main/constituent_symbol.txt')
tickerSymbol = st.sidebar.selectbox('Stock ticker', ticker_list)
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)

logo = '<img src=%s>' % tickerData.info['logo_url']
st.markdown(logo, unsafe_allow_html = True)

name = tickerData.info['longName']
st.header('**%s**' % name)

sector = tickerData.info['sector']
st.subheader(sector)

country = tickerData.info['country']
st.subheader(country)

website = tickerData.info['website']
st.subheader(website)

summary = tickerData.info['longBusinessSummary']
st.info(summary)

# Market Price

regularMarketPrice = tickerData.info['regularMarketPrice']
st.subheader('**Regular Market Price**')
st.write(regularMarketPrice)

# Profit Margins
profitMargins = tickerData.info['profitMargins']
st.subheader('**Profit Margins**')
st.write(profitMargins)

# Ticker Data
st.subheader('**Ticker data**')
st.write(tickerDf)

# Other Recomendation
st.subheader('**Recommendation**')
st.write(tickerData.recommendations)

st.subheader('**Major Holders**')
st.write(tickerData.major_holders)

st.subheader('**Sustainability**')
st.write(tickerData.sustainability)

# Bollinger Bands
st.header('**Bollinger Bands**')
qf=cf.QuantFig(tickerDf,title='First Quant Figure',legend='top',name='GS')
qf.add_bollinger_bands()
fig = qf.iplot(asFigure=True)
st.plotly_chart(fig)







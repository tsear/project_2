import streamlit as st
from PIL import Image

# creates empty containers
header = st.container()
demo = st.container()
explaination = st.container()
resources = st.container()

# title of main page
with header:
	st.title('Project 2: Algorthimic Volatility Trading Bot')
	st.write('This application uses an assortment of volatility technical strategies to trade in & out of positions.')
	# seperation line
	st.markdown("""---""") 

# sidebar
st.sidebar.markdown("# Home")



  
with demo:
	st.multiselect(label = 'Select tickers', options = ['adbe', 'sq', 'twtr', 'aapl', 'amzn', 'msft', 'tsla', 'googl', 'ipi', 'bg', 'tsn', 'cf', 'ntr'])

with demo:
  st.write('* each position will have a balance of $100,000 by default')

with demo:
  st.selectbox(label = 'Select Strategy', options = ['SMA', 'Bolinger Bands', 'Keltner Channel'])


st.button(label = 'Run Portfolio!')

#tickers= {}
#for ticker in ticker_select:
#    tickers[ticker] = pd.DataFrame()
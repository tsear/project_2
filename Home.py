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


with demo:
	st.multiselect(label = 'Select tickers', options = 
		['adbe', "sq", "pltr", "aapl", "amzn", "msft", "tsla", "googl", "ipi", "bg", "tsn", "cf", "ntr"])

# sidebar
st.sidebar.markdown("# Home")

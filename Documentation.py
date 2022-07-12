import streamlit as st
from PIL import Image

st.markdown("# Documentation")
st.sidebar.markdown("# Documentation")

# containers
header = st.container()
documentation = st.container()
closing = st.container()

# Image imports
img1 = Image.open('imports.jpg')
img2 = Image.open('dataframe.jpg')
img3 = Image.open('strategies.jpg')
img4 = Image.open('application.jpg')
img5 = Image.open('dataframeupdate.jpg')
img6 = Image.open('signals.jpg')

# Header
with header:
	st.write('This app uses pandas_ta data that has been fit into a model to identify the success of different trades.')
	st.write('Below you will find a complete documentation, including photos/screenshots, in a readme style format.')
	st.markdown("""---""") 

with documentation:
	st.subheader('Synopsis')
	st.write('- First, we import data for speciffic stocks by adding tickers to a dictionary & calling them with pandas_ta.')
	st.image(img1, caption = 'Imports & ticker dictionary')

with documentation:
	st.write('- Next, we save each ticker in the dictionary to a dataframe.')
	st.write('This will alow us to manipulate the datapoints of each ticker in the future.')
	st.image(img2, caption='saving tickers to dataframe')

with documentation:
	st.write('- After saving the tickers to dataframes we will now implement the custom technical volatility strategies.')
	st.image(img3, caption = 'volatility strategies')

with documentation:
	st.write('- Once the strategies have been defined we then apply them to each individual ticker.')
	st.write('Using this method allows us to append the individual dataframes with new datapoints with pertinent entries.')
	st.image(img4, caption = 'Applying strategies to tickers')
	st.image(img5, caption = 'The new, appended dataframe')

with documentation:
	st.write('- Next, we generate signals for the custom strategies.')
	st.image(img6, caption = 'Strategy signals')

from pydoc import Doc, doc
from holidays import IM
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
img7 = Image.open('rportfolios.jpg')
img8 = Image.open('customr.jpg')
img9 = Image.open('print.jpg')
img10 = Image.open('portfoliostats.jpg')
img11 = Image.open('returnstats.jpg')
img12 = Image.open('plot1.jpg')
img13 = Image.open('plot2.jpg')
img14 = Image.open('chart.jpg')


# Header
with header:
	st.write('This app uses pandas_ta data that has been fit into a model to identify the success of different trades.')
	st.write('Below you will find a complete documentation, including photos/screenshots, in a readme style format.')
	st.markdown("""---""") 


# Documentation
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
	st.write('Using this method allows us to append the individual dataframes with new, custom, datapoints.')
	st.image(img4, caption = 'Applying strategies to tickers')
	st.image(img5, caption = 'The new, appended dataframe')

with documentation:
	st.write('- Next, we generate signals for the custom strategies.')
	st.image(img6, caption = 'Strategy signals')

with documentation:
	st.write('- Now we add risk metrics.')
	st.write('To do so we create three portfolio variables, one for each strategy that sets a position value & accounts for slippage & fees.')
	st.image(img7, caption = 'Risk portfolios')

with documentation:
	st.write('- Here, we are building custom risk metrics & printing all stats for each & every stock & strategy.')
	st.write('We are accounting for Max Drawdown, Drawdown Tolerance, & Value at Risk. These metrics will be output for the user to observe when they run their portfolio.')
	st.write('This is done 3 times, once for each risk portfolio.')
	st.write('It is important to note that we are utilizing vectorbt here for backtesting.')
	st.image(img8, caption = 'Max Drawdown, Drawdown Tolerance, & Value at Risk')
	st.image(img9, caption = 'Printing the return & portfolio stats')

with documentation:
	st.write('- Here is an example - These two photos are the stats for strategy 2 (RSI) for Adobe $adbe')
	st.image(img10, caption = 'Portfolio stats for adbe')
	st.image(img11, caption = 'Return stats for adbe')

with documentation:
	st.write('- The final step is plotting the graph of a stock with buys & sells, included.')
	st.write('To do this we import HTML & make figures for each stock & strategy.')
	st.image(img12, caption = 'Plot part 1')
	st.image(img13, caption = 'Plot part 2')

with documentation:
	st.write('- Here is an example of the chart for strategy 2 (RSI) for adobe $adbe')
	st.image(img14, caption = 'Chart for adbe')
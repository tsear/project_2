import streamlit as st


st.sidebar.markdown("# Next Steps")

st.header('Next Steps')
st.markdown("""---""") 

st.write('- Refine Code')
st.write('Our code is realtively slow due to how we are running it. Since we iterate through each stock & each strategy it does have some buffering issues. We would like to resolve this by finding a way to optimize our code.')

st.write('- Add Relevant Strategies')
st.write('We would like to bolster the ammount of Volatility strategies to our list as well as possibly exapnd to other fields of technical indicators such as Trend (Cross Signals, Choppiness Index, etc...) & Momentum (Awesome Oscillator, KST Oscillator, etc...')

st.write('- Adding Weightings')
st.write('Instead of returning each individual stock the user has selected, we would like to concatonate selections into a portfolio to allow the user to weight it to see more accurate & customizable returns.')


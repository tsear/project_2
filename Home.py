import streamlit as st


# creates empty containers
header = st.container()
demo = st.container()
explaination = st.container()
resources = st.container()

# title of main page
with header:
	st.title('Project 2: t-SNE stock data')

# sidebar
st.sidebar.markdown("# Home")


with demo:
	st.write('This a project Demo')


with explaination:
	st.write('This project aims to take exponential stock returns & tranform that data with PCA & t-SNE')
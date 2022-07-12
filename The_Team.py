import streamlit as st

# creates sidebar title & page 3 title
st.markdown("# The Team")
st.sidebar.markdown("# The Team")

# synopsis
st.subheader('This application was built as the Project 2 for the Columbia BC submission.')

# creates container sepration line
st.markdown("""---""") 


# writes names
st.write('- Donte Thrasher')
st.write('- Grigory Timofeev')
st.write('- Tyler Sear')
import streamlit as st

pages = [
    st.Page("pages/home.py", title = "Home"),
    st.Page("pages/raw_data.py", title = "Raw data"),
    st.Page("pages/dashboard.py", title = "Dashboard"),
]

pg = st.navigation(pages)

pg.run()

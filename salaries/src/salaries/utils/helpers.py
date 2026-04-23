from salaries.utils.constants import DATA_PATH
import pandas as pd
import streamlit as st

def read_textfile(path):
    with open(path) as file:
        return file.read()

@st.cache_data
def get_salaries_df():
    return pd.read_csv(DATA_PATH / "salaries.csv")
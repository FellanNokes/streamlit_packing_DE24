import streamlit as st
from salaries.utils.constants import IMAGE_PATH, MARKDOWN_PATH
from salaries.utils.helpers import read_textfile


def home():
    st.markdown("# HOME")
    st.image(IMAGE_PATH / "salaries_data_engineers.png")
    st.markdown(read_textfile(MARKDOWN_PATH / "intro_salaries.md"))


if __name__ == "__main__":
    home()
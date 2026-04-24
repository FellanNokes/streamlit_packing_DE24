import streamlit as st
from salaries.utils.helpers import get_salaries_df
from salaries.utils.constants import MARKDOWN_PATH, STYLE_PATH
from salaries.components.kpis import avg_salary_usd_kpi
from salaries.components.charts import top_avg_salaries_chart, filtered_table
from salaries.utils.helpers import read_textfile, read_css
from salaries.components.filters import job_title_filter, experience_level_filter


def dashboard_layout():
    st.markdown("# Salaries dashboard")
    st.markdown(read_textfile(MARKDOWN_PATH / "salaries_dashboard_description.md"))
    st.dataframe(get_salaries_df())

    roles = ["Data Analyst", "Data Engineer", "Data Scientist", "AI Engineer", "Machine Learning Engineer"]


    cols = st.columns(len(roles))

    for col, role in zip(cols, roles):
        with col:
            avg_salary_usd_kpi(role, role)

    top_avg_salaries_chart(8)

    cols = st.columns(2)
    with cols[0]:
        job_title = job_title_filter()
    with cols[1]:
        experience_level = experience_level_filter()

    filtered_table(job_title, experience_level)

    st.markdown(job_title)

    read_css(STYLE_PATH / "dashboard.css")
if __name__ == "__main__":
    dashboard_layout()

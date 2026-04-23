import streamlit as st
from salaries.utils.helpers import get_salaries_df
from salaries.utils.constants import MARKDOWN_PATH
from salaries.components.kpis import avg_salary_usd_kpi
from salaries.utils.helpers import read_textfile


def dashboard_layout():
    st.markdown("# Salaries dashboard")
    st.markdown(read_textfile(MARKDOWN_PATH / "salaries_dashboard_description.md"))
    st.dataframe(get_salaries_df())

    roles = [
        ("Data Analyst", "Data Analyst"),
        ("Data Engineer", "Data Engineer"),
        ("Data Scientist", "Data Scientist"),
        ("Machine Learning Engineer", "Machine Learning Engineer"),
    ]
    # KPIs
    cols = st.columns(len(roles))

    for col, (role, label) in zip(cols, roles):
        with col:
            avg_salary_usd_kpi(role=role, label=label)
    #avg_salary_usd_kpi(role = "Data analyst", label = "Data analyst")


if __name__ == "__main__":
    dashboard_layout()

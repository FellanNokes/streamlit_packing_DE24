#%%
from salaries.utils.helpers import get_salaries_df
import duckdb
import streamlit as st


df = get_salaries_df()

def avg_salary_usd_kpi(role, label):
    avg_salary = duckdb.sql(f"""--sql
        SELECT
            ROUND(AVG(salary_in_usd), -3)::INT AS salary_in_usd
        FROM df
        WHERE job_title ILIKE '{role}'
        """).df().iloc[0]

    st.metric(label = label, value = avg_salary["salary_in_usd"])
#%%
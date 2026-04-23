import streamlit as st
from salaries.utils.helpers import get_salaries_df
import duckdb

df = get_salaries_df()

df_top_avg_salaries =duckdb.sql("""--sql
        SELECT
            job_title,
            ROUND(AVG(salary_in_usd), -3)::INT AS avg_salary_in_usd
        FROM df
        GROUP BY job_title
        ORDER BY avg_salary_in_usd DESC
        """).df()

def top_avg_salaries_chart(number_roles = 5):
    with st.container(border=True):
        st.markdown("**Top average yearly salaries USD**")
        st.bar_chart(
            df_top_avg_salaries.head(number_roles),
            x='job_title',
            y='avg_salary_in_usd',
            x_label='JOB TITLE',
            y_label='AVERAGE SALARY USD',
            horizontal=True,
            sort = "-avg_salary_in_usd",
        )

def filtered_table(job_title, experience_level):
    dff = df.query("job_title == @job_title and experience_level == @experience_level")
    st.dataframe(dff)
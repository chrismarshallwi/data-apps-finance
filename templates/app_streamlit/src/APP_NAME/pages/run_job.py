import streamlit as st

from services.databricks import DatabricksJob
from utils.helpers import init_state

init_state("running_jobs", [])
job_id = 940942180575554

col1, _, _ = st.columns(3)


@st.fragment(run_every="10s")
def auto_function(status, running_job: DatabricksJob):
    job_status = running_job.check_status()
    if running_job.has_finished(job_status):
        status.update(label=running_job.format_status_message(job_status), state="complete", expanded=False)
    else:
        status.update(label=running_job.format_status_message(job_status), state="running", expanded=False)


with col1:
    if st.button("Run", key="job_job", type="primary", icon=":material/play_arrow:", help="Run job"):
        st.session_state.running_jobs.append(DatabricksJob(job_id))
        st.rerun()

    for job in st.session_state.running_jobs:
        status = st.status(job.format_status_message(), state="running")
        with status:
            st.badge(f"Run ID: {job.run_id}")
            st.page_link(job.run_page_url, label="View in Databricks", icon=":material/open_in_new:")
        auto_function(status, job)

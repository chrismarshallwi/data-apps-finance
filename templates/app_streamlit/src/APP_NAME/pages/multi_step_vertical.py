import streamlit as st

from data.lakehouse import get_nation
from utils.helpers import has_state, init_state_fn

init_state_fn("nation_data", get_nation)

with st.expander("Step 1", icon=":material/arrow_circle_right:", expanded=has_state("step1_completed")):
    st.subheader("Identify dataset", divider=st.session_state.global_divider)
    st.caption("Short explanation of what this step is about")
    st.dataframe(st.session_state.nation_data, hide_index=True)
    if st.button("Next", key="st1", icon=":material/chevron_right:", type="tertiary"):
        st.session_state.step1_completed = True
        st.rerun()

if "step1_completed" in st.session_state and st.session_state.step1_completed:
    with st.expander("Step 2", icon=":material/arrow_circle_right:", expanded=has_state("step2_completed")):
        st.subheader("Edit data", divider=st.session_state.global_divider)
        st.dataframe(st.session_state.nation_data, hide_index=True)
        if st.button("Next", key="st2", icon=":material/chevron_right:", type="tertiary"):
            st.session_state.step2_completed = True
            st.rerun()

if "step2_completed" in st.session_state and st.session_state.step2_completed:
    with st.expander("Step 3", icon=":material/arrow_circle_right:", expanded=True):
        st.subheader("Review and save", divider=st.session_state.global_divider)
        st.dataframe(st.session_state.nation_data, hide_index=True)
        if st.button("Save", key="st3", icon=":material/save:", type="primary"):
            st.success("Saved successfully", icon=":material/check:")

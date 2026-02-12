import pandas as pd
import streamlit as st

from data.lakehouse import get_nation
from utils.helpers import clear_state, get_state, set_state

df_nation = get_nation()

with st.container(border=True):
    st.text("Filters")
    with st.container(horizontal=True):
        unique_regions = df_nation["n_regionkey"].unique().tolist()
        region_filter = st.pills(
            "Region", options=unique_regions, selection_mode="multi", on_change=lambda: clear_state("filtered_data")
        )


def get_filtered_data() -> pd.DataFrame:
    filtered_df = get_state("filtered_data", df_nation.copy())
    if region_filter:
        filtered_df = filtered_df[filtered_df["n_regionkey"].isin(region_filter)]
    filtered_df["n_comment"] = filtered_df["n_name"] + " is in region " + filtered_df["n_regionkey"].astype(str)
    return filtered_df


# Show editable data
filtered_data = get_filtered_data()
edited_filtered_data = st.data_editor(
    filtered_data,
    num_rows="dynamic",
    hide_index=True,
    column_config={"n_comment": st.column_config.TextColumn(disabled=True)},
)

if not filtered_data.equals(edited_filtered_data):
    set_state("filtered_data", edited_filtered_data)
    st.rerun()

with st.container():
    if st.button(":material/save: Save", type="primary"):
        st.success("Changes saved")

import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

from utils.helpers import clear_state_fn

df = pd.DataFrame(rng(0).standard_normal((50, 20)), columns=["col %d" % i for i in range(20)])

with st.container(horizontal=True):
    with st.popover(":material/filter_alt: Filter"):
        with st.container(horizontal=True, width=400):
            ft_positive = st.toggle("positive numbers", key="editdata_cb1")
            ft_large = st.toggle("large numbers", key="editdata_cb2", help="greater than mod|1.5|")
            ft_bins = st.multiselect("options", ["op1", "op2", "op3"], key="editdata_ms1", accept_new_options=True)
            st.date_input("end date")
    if ft_positive:
        st.badge("positive numbers", icon=":material/filter_alt:")
        df = df[df["col 0"] > 0]
    if ft_large:
        st.badge("large numbers", icon=":material/filter_alt:")
        df = df[abs(df["col 0"]) > 1.5]
    if ft_bins:
        st.badge(f"options {ft_bins}", icon=":material/filter_alt:")
        if "op1" in ft_bins:
            df = df[df["col 0"] > -1]
        if "op2" in ft_bins:
            df = df[df["col 0"] > 0]
        if "op3" in ft_bins:
            df = df[df["col 0"] > 1]


def show_toast(msg):
    st.toast(msg, icon=":material/info:", duration="short")


with st.container(horizontal=True):
    st.button(
        "",
        key="editdata_act1",
        icon=":material/checklist:",
        help="Validate",
        type="tertiary",
        on_click=show_toast,
        args=["Data validated successfully"],
    )
    st.button(
        "",
        key="editdata_act2",
        icon=":material/add_box:",
        help="Insert new row",
        type="tertiary",
        on_click=show_toast,
        args=["New row added successfully"],
    )
    st.button(
        "",
        key="editdata_act3",
        icon=":material/delete:",
        help="Delete selected row",
        type="tertiary",
        on_click=show_toast,
        args=["Row deleted successfully"],
    )

df = df.reset_index(drop=True)
st.data_editor(df, key="editdata_editor", num_rows="dynamic")

with st.container(horizontal=True):
    st.button("Save", icon=":material/save:", type="primary")
    if st.button("Reload", icon=":material/refresh:", type="tertiary"):
        clear_state_fn(lambda k: k.startswith("editdata_"))
        st.rerun()

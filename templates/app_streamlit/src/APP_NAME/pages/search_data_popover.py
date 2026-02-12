import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

# Add a page filter to the sidebar
highlight_data = st.sidebar.slider("Highlight data", -5.0, 5.0, (-0.5, 0.5), step=0.1)
use_lime = st.sidebar.toggle("Use _lime_ color :material/skull:")

df = pd.DataFrame(rng(0).standard_normal((50, 20)), columns=["col %d" % i for i in range(20)])

color = "lime" if use_lime else "#00FF0030"


def highlight(v):
    s = f"background-color: {color};" if v > highlight_data[0] and v < highlight_data[1] else None
    return s


with st.container(horizontal=True):
    with st.popover(":material/filter_alt: Filter"):
        with st.container(horizontal=True, width=400):
            ft_positive = st.toggle("positive numbers")
            ft_large = st.toggle("large numbers", help="greater than mod|1.5|")
            ft_bins = st.multiselect("options", ["op1", "op2", "op3"], accept_new_options=True)
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

st.dataframe(df.style.map(highlight), hide_index=True)

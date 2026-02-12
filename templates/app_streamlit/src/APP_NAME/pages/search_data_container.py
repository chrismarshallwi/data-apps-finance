import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

df = pd.DataFrame(rng(0).standard_normal((50, 20)), columns=["col %d" % i for i in range(20)])


with st.container(border=True):
    st.text("Filters")
    with st.container(horizontal=True):
        with st.container(width=160):
            ft_positive = st.toggle("positive numbers")
            ft_large = st.toggle("large numbers", help="greater than mod|1.5|")
        ft_bins = st.multiselect("options", ["op1", "op2", "op3"], accept_new_options=True)
        st.date_input("end date", width=100)

if ft_positive:
    df = df[df["col 0"] > 0]
if ft_large:
    df = df[abs(df["col 0"]) > 1.5]
if ft_bins:
    if "op1" in ft_bins:
        df = df[df["col 0"] > -1]
    if "op2" in ft_bins:
        df = df[df["col 0"] > 0]
    if "op3" in ft_bins:
        df = df[df["col 0"] > 1]

# Reset index after filtering
df = df.reset_index(drop=True)

event = st.dataframe(df, key="data_container", selection_mode="multi-row", on_select="rerun", hide_index=True)

if event.selection.rows:
    df_selected = df.loc[event.selection.rows]
    # Flatten all selected values into a single Series
    values = df_selected.values.flatten()
    values_series = pd.Series(values)

    if values_series.size:
        # Histogram (density) and normal PDF
        bins = 20
        hist, bin_edges = np.histogram(values_series, bins=bins, density=True)
        bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

        mu, std = values_series.mean(), values_series.std(ddof=0)
        if std == 0:
            pdf = np.zeros_like(bin_centers)
        else:
            pdf = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-((bin_centers - mu) ** 2) / (2 * std**2))

        plot_df = pd.DataFrame({"x": bin_centers, "density": hist, "pdf": pdf})

        # Altair: bars for histogram + line for normal distribution
        bars = (
            alt.Chart(plot_df)
            .mark_bar(opacity=0.6, color="#4CAF50", width=60)
            .encode(x=alt.X("x:Q", title="Value"), y=alt.Y("density:Q", title="Density"))
        )
        line = alt.Chart(plot_df).mark_line(color="black", strokeWidth=2).encode(x="x:Q", y="pdf:Q")

        chart = (bars + line).properties(title="Histogram")
        st.altair_chart(chart, use_container_width=True)

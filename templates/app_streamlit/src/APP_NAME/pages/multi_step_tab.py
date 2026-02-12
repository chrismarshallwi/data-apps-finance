import pandas as pd
import streamlit as st
from numpy.random import default_rng as rng

from data.lakehouse import get_nation
from utils.helpers import init_state_fn

init_state_fn("nation_data", get_nation)

tab1, tab2, tab3 = st.tabs([
    ":material/table: Data table",
    ":material/pie_chart: Chart",
    ":material/analytics: Analysis",
])

with tab1:
    st.dataframe(st.session_state.nation_data, hide_index=True)
    # with st.container(horizontal=True):
    #     if st.button("Next", icon=":material/chevron_right:"):
    #         tab2.

with tab2:
    df = pd.DataFrame(rng(0).standard_normal((20, 10)), columns=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"])
    st.scatter_chart(df)

with tab3:
    df = pd.DataFrame(
        rng(0).standard_normal((20, 10)),
        columns=["col0", "col1", "col2", "col3", "col4", "col5", "col6", "col7", "col8", "col9"],
    )
    df["col4"] = rng(0).choice(["a", "b", "c", "d", "e", "f"], 20)
    st.scatter_chart(
        df,
        x="col1",
        y="col2",
        color="col4",
        size="col3",
    )

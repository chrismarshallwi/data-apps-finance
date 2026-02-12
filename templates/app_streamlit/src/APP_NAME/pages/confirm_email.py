import streamlit as st

if "confirmation_id" in st.query_params:
    confirmation_id = st.query_params["confirmation_id"]
    if st.query_params["confirmed"] == "yes":
        st.success(f"Your email has been confirmed for request :blue-badge[{confirmation_id}]!")

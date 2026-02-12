import streamlit as st

a, b = st.columns(2, border=True, width=400)
c, d = st.columns(2, border=True, width=400)

a.metric("Temperature", "30°F", "-9°F")
a.button("Take action", icon=":material/action_key:", type="tertiary", key="acta")
b.metric("Wind", "4 mph", "2 mph")
b.button("Take action", icon=":material/action_key:", type="tertiary", key="actb")

c.metric("Humidity", "77%", "5%")
c.button("Take action", icon=":material/action_key:", type="tertiary", key="actc")
d.metric("Pressure", "30.34 inHg", "-2 inHg")
d.button("Take action", icon=":material/action_key:", type="tertiary", key="actd")

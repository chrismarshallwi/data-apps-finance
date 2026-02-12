import streamlit as st

from services.auth import UserInfo, get_current_user

user: UserInfo = get_current_user()

col1, _, _ = st.columns(3)

with col1:
    with st.container(border=True):
        st.text("User Information")
        with st.container(horizontal=True):
            st.text("User ID:", width=60)
            st.text(user.id)

        with st.container(horizontal=True):
            st.text("Roles:", width=60)
            for role in user.roles:
                color = "violet" if role == "admin" else "green"
                st.badge(role, icon=":material/badge:", color=color)

        with st.container(horizontal=True):
            st.text("Metadata:", width=60)
            st.write(user.metadata)

    with st.expander(":material/live_help: How to show a button if the user is in a role?", expanded=False):
        test_role = st.text_input("Type a role", placeholder="admin")

        st.divider()
        st.text("Sample code")
        st.code(
            f"""
        from services.auth import get_current_user

        user = get_current_user()
        if '{test_role}' in user.roles:
            st.button("Save")
                """,
            language="python",
        )

        st.divider()
        st.text("Result")
        if test_role in user.roles:
            st.button("Save", key="test_save", type="primary")

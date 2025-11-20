import streamlit as st

pages = [
    st.Page(page="pages/page1.py", title="Home", "🏠"),
    st.Page(page="pages/page2.py", title="Visualisasi Data","📊"),
    st.Page(page="pages/page2.py", title="Settings", "⚙️"),

]

pg = st.navigation(
    pages,
    position="sidebar",
    expanded=True
)

pg.run()
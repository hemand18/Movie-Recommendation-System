import streamlit as st

st.title("Debug Test")

try:
    from recommender import recommend
    st.success("✅ recommender.py imported successfully")
except Exception as e:
    st.error(f"❌ Import Error: {e}")
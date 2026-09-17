import streamlit as st

st.title("SIH - Pothole Detection System")
st.write("AI based pothole detection system for SIH 2025")

uploaded_file = st.file_uploader("Road image upload chey", type=["jpg","png","jpeg"])

if uploaded_file:
    st.image(uploaded_file, caption="Uploaded Road Image")
    st.success("Pothole Detected! (Demo)")

st.write("Team: SIH 2025")

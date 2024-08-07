import streamlit as st

st.title("MVSREC AUTONOMOUS PAPERS")
year = st.selectbox("Select Your Year : ",
["1st Year","2nd Year","3rd Year"])
branch = st.selectbox("Select Your Branch :",
["CSE","DS","AIML","IOT","IT","ECE"])
paper = st.selectbox("Examination : ",
["Mid1","Mid2","Sem"])
if(st.button("Submit")):
    st.text("hiii")
    pdf_url = "https://drive.google.com/file/d/1KQ3O-nq8hCe1kwa16HSRrHhMI4pHMIrH/preview"
    pdf_display = f'<iframe src="{pdf_url}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

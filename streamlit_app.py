import streamlit as st

st.title("MVSREC AUTONOMOUS PAPERS")
year = st.selectbox("Select Your Year and Sem : ",
["1st Year 1st Sem","1st Year 2nd Sem","2nd Year 1st Sem","2nd Year 2nd Sem","3rd Year 1st Sem","3rd Year 2nd Sem"])
if(year=="3rd Year"):
    branch = st.selectbox("Select Your Branch :",
["CSE","IT","ECE"])
else:
    branch = st.selectbox("Select Your Branch :",
["CSE","DS","AIML","IOT","IT","ECE"])
paper = st.selectbox("Examination : ",
["Mid1","Mid2","Sem"])
pdf_url = None
if(st.button("Submit")):
    if(year=="1st Year 1st Sem"):
        if(branch=="DS"):
            if(paper=="Mid1"):
                pdf_url = "https://drive.google.com/file/d/1KQ3O-nq8hCe1kwa16HSRrHhMI4pHMIrH/preview"
            if(paper=="Mid2"):
                pdf_url = "https://drive.google.com/file/d/1JcZWHKk3aLVZjHO6fwTYyhiZtN1RdeTd/preview"
    if(year=="2nd Year 2nd Sem"):
        if(branch=="CSE"):
            if(paper=="Mid1"):
                pdf_url = "https://drive.google.com/file/d/1q27z5x7oK92hC9bb_mB-InUkZDZESkPz/preview"
            elif(paper=="Mid2"):
                pdf_url = "https://drive.google.com/file/d/1jnq_nQwKDOOgpZauapr5xaDAVC6h5n59/preview"
            elif(paper=="Sem"):
                pdf_url = "https://drive.google.com/file/d/1R8fejWceCxq9sR4TP9hcYeEbYH7G9L6Y/preview"
    if(pdf_url=="None"):
        st.text("WILL BE UPDATED SOON")
    else:
        pdf_display = f'<iframe src="{pdf_url}" width="700" height="1000" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)

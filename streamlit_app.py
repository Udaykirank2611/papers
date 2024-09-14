import streamlit as st
st.markdown("""
    <style>
    .top-menu {
        background-color: #f1f1f1;
        padding: 10px;
        text-align: center;
    }
    .top-menu a {
        margin: 0 15px;
        text-decoration: none;
        color: #007bff;
        font-weight: bold;
    }
    .top-menu a:hover {
        text-decoration: underline;
    }
    </style>
    <div class="top-menu">
        <a href="https://bunkchecker.streamlit.app" target="_blank">BunkChecker</a>
        <!-- Add more menu items here if needed -->
    </div>
    """, unsafe_allow_html=True)
st.title("MVSREC AUTONOMOUS PAPERS")
branch = st.selectbox("Select Your Branch :",
["CSE","DS","AIML","IOT","IT","ECE"])
new = ["DS","IOT","AIML"]
if(branch in new):
    year = st.selectbox("Select Your Year and Sem : ",
["1st Year 1st Sem","1st Year 2nd Sem","2nd Year 1st Sem"])
else:
    year = st.selectbox("Select Your Year and Sem : ",
["1st Year 1st Sem","1st Year 2nd Sem","2nd Year 1st Sem","2nd Year 2nd Sem","3rd Year 1st Sem","3rd Year 2nd Sem"])
if branch=="DS" and year == "1st Year 1st Sem":
    paper = st.selectbox("Examination : ",
    ["Mid1 jan 2022-23","Mid2 mar 2022-23","Sem april 2023"])
elif branch=="DS" and year == "1st Year 2nd Sem":
    paper = st.selectbox("Examination : ",
    ["Mid1 july 2023","Mid2 sept 2023","Sem oct 2023"])
else:
    paper = st.selectbox("Examination : ",
    ["Mid1","Mid2","Sem"])
pdf_url = None
if(st.button("Submit")):
    if(year=="1st Year 1st Sem"):
        if(branch=="DS"):
            if(paper=="Mid1 jan 2022-23"):
                pdf_url = "https://drive.google.com/file/d/1KQ3O-nq8hCe1kwa16HSRrHhMI4pHMIrH/preview"
            if(paper=="Mid2 mar 2022-23"):
                pdf_url = "https://drive.google.com/file/d/1JcZWHKk3aLVZjHO6fwTYyhiZtN1RdeTd/preview"
            if(paper=="Sem april 2023"):
                pdf_url = "https://drive.google.com/file/d/1JsKyoQtOxeZKxRKlKN23GLO2A0f9q-HL/preview"
    if(year=="1st Year 2nd Sem"):
        if(branch=="DS"):
            if(paper=="Mid1 july 2023"):
                pdf_url = "https://drive.google.com/file/d/10s6GxKhdYMFIXWBOuxm5xtA1dzYvZwDM/preview"
            if(paper=="Mid2 sept 2023"):
                pdf_url = "https://drive.google.com/file/d/1KETQT4ry1140NSpFtUKhqhbnQYIPIYa5/preview"
            if(paper=="Sem oct 2023"):
                pdf_url = "https://drive.google.com/file/d/1xZrFOvAr7do3TzQJM16fAdF98WBjS6NZ/preview"
    if(year=="2nd Year 1st Sem"):
        if(branch=="DS"):
            if(paper=="Mid1"):
                pdf_url = "https://drive.google.com/file/d/1jQZlGJoTlAs5tLU3KvSiuHxzHbbFIMe7/preview"
            if(paper=="Mid2"):
                pdf_url="https://drive.google.com/file/d/1fnnw3GrDQYl7VKCcLgHcTuvVhsFZTP65/preview"
            if(paper=="Sem"):
                pdf_url = "https://drive.google.com/file/d/1Nxhs7NESzo5bHErQuUuQTGHcKfM2HNZA/preview"
    if(year=="2nd Year 2nd Sem"):
        if(branch=="CSE"):
            if(paper=="Mid1"):
                pdf_url = "https://drive.google.com/file/d/1q27z5x7oK92hC9bb_mB-InUkZDZESkPz/preview"
            elif(paper=="Mid2"):
                pdf_url = "https://drive.google.com/file/d/1jnq_nQwKDOOgpZauapr5xaDAVC6h5n59/preview"
            elif(paper=="Sem"):
                pdf_url = "https://drive.google.com/file/d/1R8fejWceCxq9sR4TP9hcYeEbYH7G9L6Y/preview"
    if(pdf_url==None):
        st.text("WILL BE UPDATED SOON")
    else:
        pdf_display = f'<iframe src="{pdf_url}" width="700" height="1000" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)
footer = """
<style>
.footer {
    position: relative;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: var(--footer-background-color);
    color: var(--footer-text-color);
    text-align: center;
    padding: 10px;
    margin-top: 20px;
}
@media (prefers-color-scheme: dark) {
    :root {
        --footer-background-color: #333;
        --footer-text-color: #f1f1f1;
    }
}
@media (prefers-color-scheme: light) {
    :root {
        --footer-background-color: #f1f1f1;
        --footer-text-color: #333;
    }
}
</style>
<div class="footer">
    <p>Developed by Uday Kiran</p>
    <p>Contact: 245122750006@mvsrec.edu.in</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)

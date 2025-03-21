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
["1st Year 1st Sem","1st Year 2nd Sem","2nd Year 1st Sem","2nd Year 2nd Sem","3rd Year 1st Sem"])
else:
    year = st.selectbox("Select Your Year and Sem : ",
["1st Year 1st Sem","1st Year 2nd Sem","2nd Year 1st Sem","2nd Year 2nd Sem","3rd Year 1st Sem","3rd Year 2nd Sem"])
if branch=="DS" and year == "1st Year 1st Sem":
    paper = st.selectbox("Examination : ",
    ["Mid1 jan 2022-23","Mid2 mar 2022-23","Sem april 2023"])
elif branch=="DS" and year == "1st Year 2nd Sem":
    paper = st.selectbox("Examination : ",
    ["Mid1 july 2023","Mid2 sept 2023","Sem oct 2023"])
elif branch=="DS" and year == "2nd Year 1st Sem":
    paper = st.selectbox("Examination : ",
    ["Mid1 dec 2023-24","Mid2 feb 2024","Sem mar 2024"])
elif branch=="DS" and year == "2nd Year 2nd Sem":
    paper = st.selectbox("Examination : ",
    ["Mid1 july 2024","Mid2 aug 2024","Sem aug 2024"])
elif branch=="DS" and year == "3rd Year 1st Sem":
    paper = st.selectbox("Examination : ",
    ["Mid1 Nov 2024","Mid2 Jan 2025","Sem Feb 2025"])
elif branch=="CSE" and year == "1st Year 1st Sem":
    paper = st.selectbox("Examination : ",
    ["Mid1 feb 2022","Mid2 mar 2022","Sem april 2022"])
elif branch=="CSE" and year == "1st Year 2nd Sem":
    paper = st.selectbox("Examination : ",
    ["Mid1 may 2022","Mid2 july 2022","Sem aug 2022"])
elif branch=="CSE" and year == "2nd Year 1st Sem":
    paper = st.selectbox("Examination : ",
    ["Mid1 nov 2022","Mid2 jan 2023","Sem feb 2023"])
elif branch=="CSE" and year == "2nd Year 2nd Sem":
    paper = st.selectbox("Examination : ",
    ["Mid1 may 2023","Mid2 july 2023","Sem aug 2023"])
elif branch=="CSE" and year == "3rd Year 1st Sem":
    paper = st.selectbox("Examination : ",
    ["Mid1 nov 2023","Mid2 Jan 2024","Sem Jan 2024"])
elif branch=="CSE" and year == "3rd Year 2nd Sem":
    paper = st.selectbox("Examination : ",
    ["Mid1 April 2024","Mid2 July 2024","Sem July 2024"])
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
            if(paper=="Mid1 dec 2023-24"):
                pdf_url = "https://drive.google.com/file/d/1jQZlGJoTlAs5tLU3KvSiuHxzHbbFIMe7/preview"
            if(paper=="Mid2 feb 2024"):
                pdf_url="https://drive.google.com/file/d/1fnnw3GrDQYl7VKCcLgHcTuvVhsFZTP65/preview"
            if(paper=="Sem mar 2024"):
                pdf_url = "https://drive.google.com/file/d/1Nxhs7NESzo5bHErQuUuQTGHcKfM2HNZA/preview"
    if(year=="2nd Year 2nd Sem"):
        if(branch=="DS"):
            if(paper=="Mid1 july 2024"):
                pdf_url = "https://drive.google.com/file/d/12vnyqyPUPgy5eLEzZM6WfPT0IzD7vauU/preview"
            if(paper=="Mid2 aug 2024"):
                pdf_url="https://drive.google.com/file/d/1sedq9ImkXfzSWi1vCSBaVglpkWciMtfK/preview"
            if(paper=="Sem aug 2024"):
                pdf_url = "https://drive.google.com/file/d/1aN3Hkq0D7gTwcyIh4QOOhjC4FTbB0Mo8/preview"
    if(year=="3rd Year 1st Sem"):
        if(branch=="DS"):
            if(paper=="Mid1 Nov 2024"):
                pdf_url = "https://drive.google.com/file/d/1eFJrUEHYPmpWtN8rNDSjY8KvEZXceSLV/preview"
            if(paper=="Mid2 Jan 2025"):
                pdf_url="https://drive.google.com/file/d/1h8iN73g9-I05c8GzxslB1lSjeD7FBiBr/preview"
            if(paper=="Sem Feb 2025"):
                pdf_url="https://drive.google.com/file/d/1gUEMQDcbz6xxz9ZP_ZXXE8wTzv42w4vc/preview"
    if(year=="3rd Year 2nd Sem"):
        if(branch=="DS"):
            if(paper=="Mid1 Nov 2024"):
                pdf_url = "https://drive.google.com/file/d/1eFJrUEHYPmpWtN8rNDSjY8KvEZXceSLV/preview"
    if(year=="1st Year 1st Sem"):
        if(branch=="CSE"):
            if(paper=="Mid1 feb 2022"):
                pdf_url = "https://drive.google.com/file/d/1C7wFXZR2-WZd9sFzhhhDuRWFPBFnRx4_/preview"
            elif(paper=="Mid2 mar 2022"):
                pdf_url = "https://drive.google.com/file/d/1eSOkYKLwiqICvSUiGpNKnKNLCZhz9KpR/preview"
            elif(paper=="Sem april 2022"):
                pdf_url = "https://drive.google.com/file/d/14GWX0riJ4O77MA2Af9wM7PiLoVHorrd7/preview"
    if(year=="1st Year 2nd Sem"):
        if(branch=="CSE"):
            if(paper=="Mid1 may 2022"):
                pdf_url = "https://drive.google.com/file/d/1f85c54BHbfl9JdL-m9QK_dmfTQnApQVn/preview"
            elif(paper=="Mid2 july 2022"):
                pdf_url = "https://drive.google.com/file/d/1t795lQowh9DGLmNPzt4LP9xB_LfYK0Yk/preview"
            elif(paper=="Sem aug 2022"):
                pdf_url = "https://drive.google.com/file/d/1tk8Zj_ORk2f2o9QFZCwGmhQC7UGn7sk0/preview"
    if(year=="2nd Year 1st Sem"):
        if(branch=="CSE"):
            if(paper=="Mid1 nov 2022"):
                pdf_url = "https://drive.google.com/file/d/1Uc5huCAxb5M8xpkOAwjS-5D2JtB75LOM/preview"
            elif(paper=="Mid2 jan 2023"):
                pdf_url = "https://drive.google.com/file/d/1VkvWLxnbv9pW6ypJYIEnkVEHq-KFdcCq/preview"
            elif(paper=="Sem feb 2023"):
                pdf_url = "https://drive.google.com/file/d/1ahuJye6HgrMu8UWMPuMCPxaDoLI14dPt/preview"
    if(year=="2nd Year 2nd Sem"):
        if(branch=="CSE"):
            if(paper=="Mid1 may 2023"):
                pdf_url = "https://drive.google.com/file/d/1q27z5x7oK92hC9bb_mB-InUkZDZESkPz/preview"
            elif(paper=="Mid2 july 2023"):
                pdf_url = "https://drive.google.com/file/d/1jnq_nQwKDOOgpZauapr5xaDAVC6h5n59/preview"
            elif(paper=="Sem aug 2023"):
                pdf_url = "https://drive.google.com/file/d/1R8fejWceCxq9sR4TP9hcYeEbYH7G9L6Y/preview"
    if(year=="3rd Year 1st Sem"):
        if(branch=="CSE"):
            if(paper=="Mid1 nov 2023"):
                pdf_url = "https://drive.google.com/file/d/1scmYK28q_e9kZh5BHgaP6RwUx6CzRXm6/preview"
            elif(paper=="Mid2 Jan 2024"):
                pdf_url = "https://drive.google.com/file/d/1gl1jVXrWkjrIxWmk25QxTY410V6J4qeh/preview"
            elif(paper == "Sem Jan 2024"):
                pdf_url = "https://drive.google.com/file/d/1-VHop0fY-BVMDkF93pMZuU1edw00W3V7/preview"
    if(year=="3rd Year 2nd Sem"):
        if(branch=="CSE"):
            if(paper=="Mid1 April 2024"):
                pdf_url = "https://drive.google.com/file/d/1pV2sDJ-eSi_Crqd0ihFI_C1FpntB4kIi/preview"
            elif(paper=="Mid2 July 2024"):
                pdf_url = "https://drive.google.com/file/d/1_8d8F6eZjDApbiAg0k-qfCls-VSR7xDP/preview"
            elif(paper == "Sem July 2024"):
                pdf_url = "https://drive.google.com/file/d/1-vR7jo5Khy7WnaQ8XSo3ogXC38lN_gfb/preview"
    if(year=="2nd Year 2nd Sem"):
        if(branch=="ECE"):
            if(paper=="Sem"):
                pdf_url = "https://drive.google.com/file/d/1NCsnxC5pOvP9hemib_RQqi4RTBjoGFuI/preview"
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

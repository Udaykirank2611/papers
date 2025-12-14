import streamlit as st

# --- PAGE STYLE ---
st.markdown("""
<style>
/* Gradient Background – light/dark mode support */
body {
    background: linear-gradient(135deg, #6d83f2 0%, #0bc8a9 100%) !important;
    min-height: 100vh;
}
.stApp {
    background: linear-gradient(135deg, #6d83f2 0%, #0bc8a9 100%) !important;
}

/* Fancy Glassmorphism Card for the main area */
.main-card {
    max-width: 670px;
    margin: 32px auto 32px auto;
    background: rgba(255,255,255,0.10);
    box-shadow: 0 8px 32px 0 rgba(21,27,80,.12);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.3);
    padding: 32px 32px 16px 32px;
    font-family: 'Segoe UI', 'Poppins', Arial, sans-serif;
}

h1, h2, h3, h4 {
    color: #fff !important;
    text-shadow: 0 1px 10px rgba(27,51,196,0.16);
}

label, .css-1cpxqw2, .css-1jy7b63 {
    font-size: 1.07rem!important;
    color: #ecebff !important;
    margin-bottom: 6px;
}

/* Custom styled menu bar */
.top-menu {
    background: rgba(0,24,48, 0.75);
    padding: 18px 5px 13px 5px;
    border-radius: 0 0 26px 26px;
    box-shadow: 0 6px 18px rgba(31,74,138,0.08);
    margin-bottom: 28px;
    display: flex;
    justify-content: center;
    align-items: center;
}

.top-menu a {
    margin: 0 15px;
    text-decoration: none;
    color: #fff;
    font-weight: 600;
    letter-spacing: 1px;
    transition: all .22s;
    padding: 7px 18px;
    border-radius: 20px;
}

.top-menu a:hover {
    background: #0bc8a9;
    color: #2b2b2b;
    box-shadow: 0 2px 12px rgba(17,228,215,0.18);
    text-decoration: none;
    transform: translateY(-2px) scale(1.06);
}

/* Glow for selectbox and buttons */
.stSelectbox > div, .stButton > button {
    box-shadow: 0 2px 12px 0 #5786e9cc, 0 1.5px 8px 0 #0bc8a966;
    border-radius: 14px !important;
    font-weight: 600 !important;
    font-family: 'Segoe UI', 'Poppins', Arial, sans-serif !important;
    transition: box-shadow .17s;
}
.stButton > button {
    background: linear-gradient(90deg,#5dd6ff 0,#7b6ffb 100%) !important;
    color: #fff !important;
    border: none;
    font-size: 1.13rem !important;
    padding: 0.2rem 1.4rem;
}
.stButton > button:hover {
    background: linear-gradient(90deg,#0bc8a9 0,#7b6ffb 90%);
    box-shadow: 0 4px 14px 0 #869bff70;
}
/* Responsive PDF display */
.pdf-area iframe {
    border-radius: 16px;
    box-shadow: 0 3px 26px 1px rgba(27, 47, 95, 0.22);
    background: #23273e3b;
    border: none;
    margin: 28px 0 16px;
    min-height: 500px;
}

/* Cool sticky footer */
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100vw;
    background: rgba(25,30,43,0.28);
    color: #fff;
    text-align: center;
    padding: 10px 0;
    font-size: 1.02rem;
    letter-spacing: 2px;
    z-index: 99;
    font-weight: 400;
    user-select: none;
    box-shadow: 0 -2px 8px #1b2c556e;
    backdrop-filter: blur(6px);
}

@media (max-width: 1000px) {
    .main-card { padding: 13px 6px 2px 6px; }
    .pdf-area iframe { width: 94vw !important; min-height: 320px !important;}
    .footer { font-size: .95rem; }
}
</style>
""", unsafe_allow_html=True)

# --- TOP MENU BAR ---
st.markdown("""
<div class="top-menu">
    <a href="https://bunkchecker.streamlit.app" target="_blank">BunkChecker</a>
    <!-- Add more menu items here if needed -->
</div>
""", unsafe_allow_html=True)

# --- MAIN CONTENT CARD ---
st.markdown('<div class="main-card">', unsafe_allow_html=True)

st.title("MVSREC AUTONOMOUS PAPERS")

branch = st.selectbox("Select Your Branch :",
["CSE","DS","AIML","IOT","IT","ECE"])

new = ["DS","IOT","AIML"]
if(branch in new):
    year = st.selectbox("Select Your Year and Sem : ",
    ["1st Year 1st Sem","1st Year 2nd Sem","2nd Year 1st Sem","2nd Year 2nd Sem","3rd Year 1st Sem","3rd Year 2nd Sem"])
else:
    year = st.selectbox("Select Your Year and Sem : ",
    ["1st Year 1st Sem","1st Year 2nd Sem","2nd Year 1st Sem","2nd Year 2nd Sem","3rd Year 1st Sem","3rd Year 2nd Sem","4th Year 1st Sem"])
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
elif branch=="DS" and year == "3rd Year 2nd Sem":
    paper = st.selectbox("Examination : ",
    ["Mid1 April 2025","Mid2 July 2025","Sem August 2025"])
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
elif branch=="IT" and year == "3rd Year 1st Sem":
    paper = st.selectbox("Examination : ",
    ["Mid1 nov 2024"])
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
            if(paper=="Mid1 April 2025"):
                pdf_url = "https://drive.google.com/file/d/1T81A1_TCLiJhRd27CF0vJz6XVBWtAdYN/preview"
            if(paper=="Mid2 July 2025"):
                pdf_url = "https://drive.google.com/file/d/1QOEeYJ7IJCN4RhwZpTFyh4tEtVmMUeJn/preview"
            if(paper == "Sem August 2025"):
                pdf_url = "https://drive.google.com/file/d/1d4UiAvvCpYuKWyksiqGYkmT4u-tE6bw4/preview"
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
    if(year=="3rd Year 1st Sem"):
        if(branch=="IT"):
            if(paper=="Mid1 nov 2024"):
                pdf_url = "https://drive.google.com/file/d/1thIx1Ks0FBonK44Fw-PS0Ngq-ba26INf/preview"
    if(year=="2nd Year 2nd Sem"):
        if(branch=="ECE"):
            if(paper=="Sem"):
                pdf_url = "https://drive.google.com/file/d/1NCsnxC5pOvP9hemib_RQqi4RTBjoGFuI/preview"
    if(pdf_url==None):
        st.markdown("<div style='color:#fff;background:rgba(70,14,109,0.33);border-radius:10px;padding:0.5rem .7rem;display:inline-block;'>WILL BE UPDATED SOON</div>", unsafe_allow_html=True)
    else:
        pdf_display = f'''
        <div class="pdf-area">
            <iframe src="{pdf_url}" width="700" height="500" type="application/pdf"></iframe>
        </div>
        '''
        st.markdown(pdf_display, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
footer = """
<div class="footer">
    <p>Developed by Uday Kiran | Contact: 245122750006@mvsrec.edu.in</p>
</div>
"""
st.markdown(footer, unsafe_allow_html=True)

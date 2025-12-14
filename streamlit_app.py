Here is a complete redesign. I have switched to a **Modern Dark Glassmorphism** theme which is easier on the eyes, professional, and distinct.

I also refactored your Python logic. Instead of 50+ nested `if-else` statements, I used a **Dictionary (Key-Value Pair)** structure. This makes the code cleaner, faster, and much easier for you to update later.

```python
import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title="MVSREC Papers", page_icon="Oc", layout="centered")

# --- DATA STRUCTURE (Refactored for Cleanliness) ---
# Format: Branch -> Year -> Exam -> Link
PAPERS_DB = {
    "DS": {
        "1st Year 1st Sem": {
            "Mid1 Jan 2022-23": "https://drive.google.com/file/d/1KQ3O-nq8hCe1kwa16HSRrHhMI4pHMIrH/preview",
            "Mid2 Mar 2022-23": "https://drive.google.com/file/d/1JcZWHKk3aLVZjHO6fwTYyhiZtN1RdeTd/preview",
            "Sem April 2023": "https://drive.google.com/file/d/1JsKyoQtOxeZKxRKlKN23GLO2A0f9q-HL/preview"
        },
        "1st Year 2nd Sem": {
            "Mid1 July 2023": "https://drive.google.com/file/d/10s6GxKhdYMFIXWBOuxm5xtA1dzYvZwDM/preview",
            "Mid2 Sept 2023": "https://drive.google.com/file/d/1KETQT4ry1140NSpFtUKhqhbnQYIPIYa5/preview",
            "Sem Oct 2023": "https://drive.google.com/file/d/1xZrFOvAr7do3TzQJM16fAdF98WBjS6NZ/preview"
        },
        "2nd Year 1st Sem": {
            "Mid1 Dec 2023-24": "https://drive.google.com/file/d/1jQZlGJoTlAs5tLU3KvSiuHxzHbbFIMe7/preview",
            "Mid2 Feb 2024": "https://drive.google.com/file/d/1fnnw3GrDQYl7VKCcLgHcTuvVhsFZTP65/preview",
            "Sem Mar 2024": "https://drive.google.com/file/d/1Nxhs7NESzo5bHErQuUuQTGHcKfM2HNZA/preview"
        },
        "2nd Year 2nd Sem": {
            "Mid1 July 2024": "https://drive.google.com/file/d/12vnyqyPUPgy5eLEzZM6WfPT0IzD7vauU/preview",
            "Mid2 Aug 2024": "https://drive.google.com/file/d/1sedq9ImkXfzSWi1vCSBaVglpkWciMtfK/preview",
            "Sem Aug 2024": "https://drive.google.com/file/d/1aN3Hkq0D7gTwcyIh4QOOhjC4FTbB0Mo8/preview"
        },
        "3rd Year 1st Sem": {
            "Mid1 Nov 2024": "https://drive.google.com/file/d/1eFJrUEHYPmpWtN8rNDSjY8KvEZXceSLV/preview",
            "Mid2 Jan 2025": "https://drive.google.com/file/d/1h8iN73g9-I05c8GzxslB1lSjeD7FBiBr/preview",
            "Sem Feb 2025": "https://drive.google.com/file/d/1gUEMQDcbz6xxz9ZP_ZXXE8wTzv42w4vc/preview"
        },
        "3rd Year 2nd Sem": {
            "Mid1 April 2025": "https://drive.google.com/file/d/1T81A1_TCLiJhRd27CF0vJz6XVBWtAdYN/preview",
            "Mid2 July 2025": "https://drive.google.com/file/d/1QOEeYJ7IJCN4RhwZpTFyh4tEtVmMUeJn/preview",
            "Sem August 2025": "https://drive.google.com/file/d/1d4UiAvvCpYuKWyksiqGYkmT4u-tE6bw4/preview"
        }
    },
    "CSE": {
        "1st Year 1st Sem": {
            "Mid1 Feb 2022": "https://drive.google.com/file/d/1C7wFXZR2-WZd9sFzhhhDuRWFPBFnRx4_/preview",
            "Mid2 Mar 2022": "https://drive.google.com/file/d/1eSOkYKLwiqICvSUiGpNKnKNLCZhz9KpR/preview",
            "Sem April 2022": "https://drive.google.com/file/d/14GWX0riJ4O77MA2Af9wM7PiLoVHorrd7/preview"
        },
        "1st Year 2nd Sem": {
            "Mid1 May 2022": "https://drive.google.com/file/d/1f85c54BHbfl9JdL-m9QK_dmfTQnApQVn/preview",
            "Mid2 July 2022": "https://drive.google.com/file/d/1t795lQowh9DGLmNPzt4LP9xB_LfYK0Yk/preview",
            "Sem Aug 2022": "https://drive.google.com/file/d/1tk8Zj_ORk2f2o9QFZCwGmhQC7UGn7sk0/preview"
        },
        "2nd Year 1st Sem": {
            "Mid1 Nov 2022": "https://drive.google.com/file/d/1Uc5huCAxb5M8xpkOAwjS-5D2JtB75LOM/preview",
            "Mid2 Jan 2023": "https://drive.google.com/file/d/1VkvWLxnbv9pW6ypJYIEnkVEHq-KFdcCq/preview",
            "Sem Feb 2023": "https://drive.google.com/file/d/1ahuJye6HgrMu8UWMPuMCPxaDoLI14dPt/preview"
        },
        "2nd Year 2nd Sem": {
            "Mid1 May 2023": "https://drive.google.com/file/d/1q27z5x7oK92hC9bb_mB-InUkZDZESkPz/preview",
            "Mid2 July 2023": "https://drive.google.com/file/d/1jnq_nQwKDOOgpZauapr5xaDAVC6h5n59/preview",
            "Sem Aug 2023": "https://drive.google.com/file/d/1R8fejWceCxq9sR4TP9hcYeEbYH7G9L6Y/preview"
        },
        "3rd Year 1st Sem": {
            "Mid1 Nov 2023": "https://drive.google.com/file/d/1scmYK28q_e9kZh5BHgaP6RwUx6CzRXm6/preview",
            "Mid2 Jan 2024": "https://drive.google.com/file/d/1gl1jVXrWkjrIxWmk25QxTY410V6J4qeh/preview",
            "Sem Jan 2024": "https://drive.google.com/file/d/1-VHop0fY-BVMDkF93pMZuU1edw00W3V7/preview"
        },
        "3rd Year 2nd Sem": {
            "Mid1 April 2024": "https://drive.google.com/file/d/1pV2sDJ-eSi_Crqd0ihFI_C1FpntB4kIi/preview",
            "Mid2 July 2024": "https://drive.google.com/file/d/1_8d8F6eZjDApbiAg0k-qfCls-VSR7xDP/preview",
            "Sem July 2024": "https://drive.google.com/file/d/1-vR7jo5Khy7WnaQ8XSo3ogXC38lN_gfb/preview"
        }
    },
    "IT": {
        "3rd Year 1st Sem": {
            "Mid1 Nov 2024": "https://drive.google.com/file/d/1thIx1Ks0FBonK44Fw-PS0Ngq-ba26INf/preview"
        }
    },
    "ECE": {
        "2nd Year 2nd Sem": {
            "Sem": "https://drive.google.com/file/d/1NCsnxC5pOvP9hemib_RQqi4RTBjoGFuI/preview"
        }
    }
}

# --- CUSTOM CSS STYLING ---
st.markdown("""
<style>
    /* Global Reset & Background */
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');
    
    .stApp {
        background: radial-gradient(circle at 10% 20%, rgb(17, 24, 39) 0%, rgb(10, 10, 10) 90%);
        font-family: 'Outfit', sans-serif;
    }

    /* Header Styling */
    .title-text {
        color: #ffffff;
        font-weight: 700;
        font-size: 2.5rem;
        text-align: center;
        background: -webkit-linear-gradient(45deg, #4f46e5, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2rem;
    }

    /* Top Navigation Bar */
    .nav-bar {
        background: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(10px);
        padding: 10px 20px;
        border-radius: 50px;
        display: flex;
        justify-content: center;
        width: fit-content;
        margin: 0 auto 30px auto;
    }
    .nav-bar a {
        color: #e2e8f0;
        text-decoration: none;
        font-weight: 500;
        padding: 8px 16px;
        border-radius: 30px;
        transition: all 0.3s ease;
    }
    .nav-bar a:hover {
        background: rgba(79, 70, 229, 0.2);
        color: #6366f1;
        box-shadow: 0 0 10px rgba(99, 102, 241, 0.3);
    }

    /* Main Glass Card */
    .glass-container {
        background: rgba(30, 41, 59, 0.4);
        border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        padding: 40px;
        margin-bottom: 30px;
        backdrop-filter: blur(12px);
    }

    /* Input Fields */
    .stSelectbox label {
        color: #94a3b8 !important;
        font-size: 0.9rem;
    }
    .stSelectbox > div > div {
        background-color: #0f172a !important;
        border: 1px solid #334155 !important;
        color: white !important;
        border-radius: 12px !important;
    }
    
    /* Submit Button */
    .stButton > button {
        width: 100%;
        background: linear-gradient(135deg, #4f46e5 0%, #06b6d4 100%) !important;
        color: white !important;
        font-weight: 600 !important;
        padding: 0.6rem 1rem !important;
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 4px 14px rgba(6, 182, 212, 0.3);
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(79, 70, 229, 0.5);
    }

    /* Error / Warning Message */
    .not-found {
        background: rgba(220, 38, 38, 0.15);
        color: #fca5a5;
        padding: 15px;
        border-radius: 12px;
        border: 1px solid rgba(220, 38, 38, 0.3);
        text-align: center;
        font-weight: 500;
    }

    /* PDF Viewer */
    iframe {
        border-radius: 16px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 10px 40px rgba(0,0,0,0.5);
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #64748b;
        font-size: 0.85rem;
        margin-top: 40px;
        padding-bottom: 20px;
        border-top: 1px solid rgba(255,255,255,0.05);
        padding-top: 20px;
    }
    .footer span {
        color: #94a3b8;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# --- UI LAYOUT ---

# 1. Navigation
st.markdown("""
<div class="nav-bar">
    <a href="https://bunkchecker.streamlit.app" target="_blank">🔍 BunkChecker</a>
    <a href="#">📚 MVSREC Papers</a>
</div>
""", unsafe_allow_html=True)

# 2. Title
st.markdown('<h1 class="title-text">MVSREC AUTONOMOUS PAPERS</h1>', unsafe_allow_html=True)

# 3. Main Form Area
with st.container():
    st.markdown('<div class="glass-container">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Branch Selection
        branches = ["CSE", "DS", "AIML", "IOT", "IT", "ECE"]
        selected_branch = st.selectbox("Select Branch", branches)

    with col2:
        # Year Selection logic
        # Default years
        all_years = [
            "1st Year 1st Sem", "1st Year 2nd Sem", 
            "2nd Year 1st Sem", "2nd Year 2nd Sem",
            "3rd Year 1st Sem", "3rd Year 2nd Sem",
            "4th Year 1st Sem"
        ]
        
        # Filter years for new branches if necessary
        new_branches = ["DS", "IOT", "AIML"]
        if selected_branch in new_branches:
            available_years = all_years[:-1] # Exclude 4th year
        else:
            available_years = all_years
            
        selected_year = st.selectbox("Select Year & Sem", available_years)

    # Exam Selection logic
    # We check if the branch and year exist in our database to show specific exams
    available_exams = []
    
    if selected_branch in PAPERS_DB and selected_year in PAPERS_DB[selected_branch]:
        # Get keys (Exam Names) from the dictionary
        available_exams = list(PAPERS_DB[selected_branch][selected_year].keys())
    else:
        # Fallback if no specific data is found
        available_exams = ["Mid1", "Mid2", "Sem"]

    selected_exam = st.selectbox("Select Examination", available_exams)
    
    st.markdown("<br>", unsafe_allow_html=True) # Spacer
    submit_btn = st.button("Get Question Paper")
    
    st.markdown('</div>', unsafe_allow_html=True) # End glass container

# --- LOGIC & DISPLAY ---

if submit_btn:
    pdf_url = None
    
    # Try to fetch from DB
    try:
        pdf_url = PAPERS_DB[selected_branch][selected_year][selected_exam]
    except KeyError:
        pdf_url = None

    if pdf_url:
        st.markdown(f'''
            <div style="display:flex; justify-content:center; margin-bottom: 20px;">
                <iframe src="{pdf_url}" width="100%" height="600px"></iframe>
            </div>
        ''', unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="not-found">
            ⚠️ The paper for <b>{selected_branch} - {selected_year} - {selected_exam}</b> is not yet available in the database.<br>
            <span style="font-size:0.8rem; opacity:0.8">It will be updated soon.</span>
        </div>
        """, unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div class="footer">
    Developed by <span>Uday Kiran</span> | Contact: 245122750006@mvsrec.edu.in
</div>
""", unsafe_allow_html=True)
```

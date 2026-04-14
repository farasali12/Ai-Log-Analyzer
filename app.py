import os
import base64
import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

st.set_page_config(page_title="AI Log Analyzer", page_icon="🛡️", layout="wide")

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    st.error("OpenAI API key not found. Add it to your .env file.")
    st.stop()

try:
    client = OpenAI(api_key=api_key)
except Exception as e:
    st.error(f"Error creating OpenAI client: {e}")
    st.stop()


def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode()


background_file = "background.jpg"

background_css = ""

if os.path.exists(background_file):
    bg_base64 = get_base64_image(background_file)
    background_css = f"""
    background-image: linear-gradient(
        rgba(5, 10, 25, 0.82),
        rgba(5, 10, 25, 0.88)
    ), url("data:image/jpg;base64,{bg_base64}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    """
else:
    background_css = """
    background: linear-gradient(135deg, #081120, #0d1b2a, #102a43);
    """

st.markdown(
    f"""
    <style>
    .stApp {{
        {background_css}
        color: white;
    }}

    .block-container {{
        padding-top: 2rem;
        padding-bottom: 2rem;
    }}

    h1, h2, h3, p, label {{
        color: white !important;
    }}

    .main-title {{
        font-size: 58px;
        font-weight: 800;
        margin-bottom: 10px;
        color: #ffffff;
        text-shadow: 2px 2px 8px rgba(0,0,0,0.5);
    }}

    .sub-text {{
        font-size: 23px;
        color: #dbeafe;
        margin-bottom: 30px;
    }}

    .custom-box {{
        background: rgba(255, 255, 255, 0.08);
        padding: 25px;
        border-radius: 18px;
        border: 1px solid rgba(255, 255, 255, 0.15);
        box-shadow: 0 8px 24px rgba(0,0,0,0.25);
        backdrop-filter: blur(6px);
        margin-bottom: 25px;
    }}

    .stButton > button {{
        background: linear-gradient(90deg, #2563eb, #06b6d4);
        color: white;
        font-weight: 700;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.4rem;
        font-size: 16px;
    }}

    .stButton > button:hover {{
        background: linear-gradient(90deg, #1d4ed8, #0891b2);
        color: white;
    }}

    .stDownloadButton > button {{
        background: linear-gradient(90deg, #16a34a, #22c55e);
        color: white;
        font-weight: 700;
        border: none;
        border-radius: 10px;
        padding: 0.6rem 1.4rem;
        font-size: 16px;
    }}

    .stDownloadButton > button:hover {{
        background: linear-gradient(90deg, #15803d, #16a34a);
        color: white;
    }}

    section[data-testid="stFileUploader"] {{
        background: rgba(255, 255, 255, 0.08);
        padding: 18px;
        border-radius: 18px;
        border: 1px solid rgba(255, 255, 255, 0.12);
    }}

    textarea {{
        background-color: rgba(255,255,255,0.06) !important;
        color: white !important;
        border-radius: 12px !important;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">🛡️ AI Log Analyzer</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-text">Upload a log file and let AI analyze suspicious activity in a cleaner, more professional dashboard.</div>',
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader("Upload a log file", type=["txt", "log"])


def analyze_log(log_text):
    prompt = f"""
You are a cybersecurity analyst.

Analyze the logs and respond in this EXACT format:

Summary:
- Write a short summary of what happened

Suspicious Activity:
- List suspicious events or indicators

Severity:
- Low, Medium, or High

Recommended Actions:
- Give practical next steps

Logs:
{log_text}
"""

    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )

        if hasattr(response, "output_text") and response.output_text:
            return response.output_text

        return str(response)

    except Exception as e:
        return f"Error while analyzing logs: {e}"


if uploaded_file is not None:
    log_text = uploaded_file.read().decode("utf-8", errors="ignore")

    st.markdown('<div class="custom-box">', unsafe_allow_html=True)
    st.subheader("Log Preview")
    st.text_area("Uploaded Log Content", log_text, height=250)
    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Analyze Logs"):
        with st.spinner("Analyzing logs..."):
            result = analyze_log(log_text)

        st.markdown('<div class="custom-box">', unsafe_allow_html=True)
        st.subheader("Analysis Result")
        st.write(result)
        st.markdown("</div>", unsafe_allow_html=True)

        if "High" in result:
            st.error("🚨 High Severity Detected")
        elif "Medium" in result:
            st.warning("⚠️ Medium Severity Detected")
        elif "Low" in result:
            st.success("✅ Low Severity Detected")

        st.download_button(
            label="Download Report",
            data=result,
            file_name="analysis_report.txt",
            mime="text/plain"
        )
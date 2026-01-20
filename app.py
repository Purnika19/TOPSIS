import streamlit as st
import pandas as pd
import numpy as np
import re

# =========================
# PAGE CONFIG
# =========================
st.set_page_config(
    page_title="Purnika[s] TOPSIS Web Service",
    layout="centered",
    page_icon="📊",
    initial_sidebar_state="collapsed"
)

# =========================
# HARD RESET CSS (NUCLEAR)
# =========================
st.markdown("""
<style>

/* ---- KILL ALL STREAMLIT TOP BARS ---- */
header, footer {
    display: none !important;
}

[data-testid="stHeader"] {
    display: none !important;
}

[data-testid="stToolbar"] {
    display: none !important;
}

[data-testid="stDecoration"] {
    display: none !important;
}

.block-container {

    padding-bottom: 80px !important;


}

/* ---- PAGE BACKGROUND ---- */
.stApp {
    background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
    color: white;
    animation: fadeIn 0.8s ease-in;
}

/* ---- GLASS CARD ---- */
.card {
    margin-top: 40px;
    background: rgba(255,255,255,0.12);
    backdrop-filter: blur(18px);
    padding: 36px;
    border-radius: 30px;
    box-shadow: 0 30px 60px rgba(0,0,0,0.55);
    animation: slideUp 0.8s ease;
}

/* ---- HEADINGS ---- */
h1 {
    text-align: center;
    font-weight: 900;
    margin-bottom: 12px;
}

.subtitle {
    text-align: center;
    font-size: 1.05em;
    opacity: 0.9;
    margin-bottom: 30px;
}

/* ---- INPUTS ---- */
.stTextInput > div > div > input,
.stFileUploader section {
    background: rgba(255,255,255,0.15) !important;
    border-radius: 16px !important;
    padding: 14px !important;
    border: 1px solid rgba(255,255,255,0.25) !important;
    color: white !important;
    transition: all 0.3s ease;
}

/* Hover */
.stTextInput > div > div > input:hover,
.stFileUploader section:hover {
    border-color: #ff5f9e !important;
    box-shadow: 0 0 22px rgba(255,95,158,0.6);
    transform: translateY(-2px);
}

/* Focus */
.stTextInput > div > div > input:focus {
    box-shadow: 0 0 28px rgba(255,95,158,0.85);
    border-color: #ff5f9e !important;
}
.custom-footer {
    position: fixed;
    bottom: 0;
    left: 0;
    width: 100%;
    text-align: center;
    font-size: 0.9em;
    padding: 10px 0;
    background: linear-gradient(
        to top,
        rgba(15,32,39,0.95),
        rgba(15,32,39,0.6),
        transparent
    );
    color: #ffffff;
    opacity: 0.85;
    z-index: 9999;
    pointer-events: none;
}



/* ---- BUTTON ---- */
.stButton > button {
    background: linear-gradient(135deg, #ff512f, #dd2476);
    color: white;
    border-radius: 18px;
    height: 3.3em;
    font-size: 1.15em;
    width: 100%;
    transition: all 0.25s ease;
}

.stButton > button:hover {
    transform: scale(1.06);
    box-shadow: 0 16px 32px rgba(255,80,120,0.65);
}

.stButton > button:active {
    transform: scale(0.97);
}

/* ---- ANIMATIONS ---- */
@keyframes fadeIn {
    from {opacity: 0;}
    to {opacity: 1;}
}

@keyframes slideUp {
    from {transform: translateY(40px); opacity: 0;}
    to {transform: translateY(0); opacity: 1;}
}

</style>
""", unsafe_allow_html=True)

# =========================
# SINGLE CARD (NO EXTRA CONTAINERS)
# =========================
st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown("""
<h1>📊 TOPSIS Web Service</h1>
<p class="subtitle">
Multi-Criteria Decision Making using TOPSIS<br>
Upload data, apply weights & impacts, download ranked result
</p>
<hr style="opacity:0.25; margin-bottom:28px;">
""", unsafe_allow_html=True)

# =========================
# INPUTS
# =========================
uploaded_file = st.file_uploader("📁 Upload CSV File", type=["csv"])
weights_input = st.text_input(" Weights ", "1,1,1,1")
impacts_input = st.text_input("📈 Impacts ", "+,+,-,+")
email_input = st.text_input("📧 Email ID")

submit = st.button("🚀 Submit")

st.markdown('</div>', unsafe_allow_html=True)

# =========================
# VALIDATION
# =========================
def is_valid_email(email):
    return re.match(r"^[\\w\\.-]+@[\\w\\.-]+\\.\\w+$", email)

# =========================
# TOPSIS LOGIC
# =========================
if submit:

    if not uploaded_file:
        st.error("❌ Please upload a CSV file.")
        st.stop()

    if not is_valid_email(email_input):
        st.error("❌ Invalid email format.")
        st.stop()

    try:
        weights = [float(w.strip()) for w in weights_input.split(",")]
        impacts = [i.strip() for i in impacts_input.split(",")]
    except:
        st.error("❌ Weights must be numeric and comma separated.")
        st.stop()

    if len(weights) != len(impacts):
        st.error("❌ Number of weights and impacts must be equal.")
        st.stop()

    for i in impacts:
        if i not in ["+", "-"]:
            st.error("❌ Impacts must be '+' or '-'.")
            st.stop()

    df = pd.read_csv(uploaded_file)

    if df.shape[1] < 3:
        st.error("❌ CSV must contain at least 3 columns.")
        st.stop()

    data = df.iloc[:, 1:]

    for col in data.columns:
        if not pd.api.types.is_numeric_dtype(data[col]):
            st.error(f"❌ Column '{col}' must be numeric.")
            st.stop()

    if len(weights) != data.shape[1]:
        st.error("❌ Weights count must match criteria columns.")
        st.stop()

    # ---- TOPSIS ----
    matrix = data.values.astype(float)
    norm = matrix / np.sqrt((matrix ** 2).sum(axis=0))
    weighted = norm * np.array(weights)

    ideal_best, ideal_worst = [], []

    for i in range(len(impacts)):
        if impacts[i] == "+":
            ideal_best.append(weighted[:, i].max())
            ideal_worst.append(weighted[:, i].min())
        else:
            ideal_best.append(weighted[:, i].min())
            ideal_worst.append(weighted[:, i].max())

    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    scores = dist_worst / (dist_best + dist_worst)
    df["Topsis Score"] = scores
    df["Rank"] = df["Topsis Score"].rank(ascending=False)

    df.to_csv("topsis_result.csv", index=False)

    st.success("✅ TOPSIS applied successfully!")

    with open("topsis_result.csv", "rb") as f:
        st.download_button(
            "⬇️ Download Result CSV",
            data=f,
            file_name="topsis_result.csv"
        )
st.markdown("""
<div class="custom-footer">
    Made by <b>Purnika Malhotra</b>
</div>
""", unsafe_allow_html=True)





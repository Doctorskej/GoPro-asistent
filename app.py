import streamlit as st

st.set_page_config(page_title="GoPro Asistent", page_icon="🎥", layout="wide", initial_sidebar_state="collapsed")

pozadi_url = "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=2000&auto=format&fit=crop"

st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(6, 10, 20, 0.96), rgba(6, 10, 20, 0.93)), url("{pozadi_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* === HLAVIČKA === */
    .header {{
        text-align: center;
        padding: 2rem 0 1.5rem 0;
    }}
    .header h1 {{
        font-size: 3.2rem;
        color: #00AEEF;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.04em;
    }}
    .header p {{
        font-size: 1.25rem;
        color: #AAAAAA;
        margin-top: 0.4rem;
    }}

    /* === MODERNÍ SEGMENTED BUTTONS (bez červené čáry) === */
    .segment-container {{
        display: flex;
        justify-content: center;
        gap: 12px;
        margin: 1.5rem 0 2.5rem 0;
        flex-wrap: wrap;
    }}
    .segment-btn {{
        background: rgba(255,255,255,0.07);
        color: #CCCCCC;
        border: 1px solid rgba(0,174,239,0.35);
        padding: 16px 32px;
        border-radius: 50px;
        font-weight: 600;
        font-size: 1.1rem;
        cursor: pointer;
        transition: all 0.35s ease;
        display: flex;
        align-items: center;
        gap: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }}
    .segment-btn:hover {{
        background: rgba(0,174,239,0.15);
        border-color: #00AEEF;
        color: white;
        transform: translateY(-3px);
    }}
    .segment-btn.active {{
        background: #00AEEF;
        color: #000000;
        border: 2px solid #00AEEF;
        font-weight: 700;
        box-shadow: 0 0 25px rgba(0,174,239,0.6);
    }}

    /* Glass card */
    .glass {{
        background: rgba(255,255,255,0.085);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(0,174,239,0.3);
        border-radius: 20px;
        padding: 2.2rem;
        box-shadow: 0 15px 50px rgba(0,0,0,0.5);
    }}

    h2 {{ color: #00AEEF !important; font-weight: 700; }}
    p, li {{ color: #F0F0F0; font-size: 1.1rem; line-height: 1.7; }}

    .manual-card {{
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(0,174,239,0.4);
        border-radius: 16px;
        padding: 1.6rem;
        margin-bottom: 14px;
        display: flex;
        align-items: center;
        transition: 0.3s;
    }}
    .manual-card:hover {{
        background: rgba(0,174,239,0.18);
        transform: translateY(-4px);
    }}
</style>
""", unsafe_allow_html=True)

# === HLAVIČKA ===
st.markdown('<div class="header"><h1>📹 GoPro Asistent</h1><p>Praktický průvodce propojením GoPro Hero 13 + DJI Mic 3</p></div>', unsafe_allow_html=True)

# === SEGMENTOVANÉ TLAČÍTKO (bez červené) ===
selected = st.radio(
    "Vyber typ propojení",
    ["🔵 Přímé Bluetooth", "📡 Media Mod + přijímač", "⚡ Rychlý tahák"],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown(f"""
<div class="segment-container">
    <div class="segment-btn {'active' if selected == '🔵 Přímé Bluetooth' else ''}">🔵 Přímé Bluetooth</div>
    <div class="segment-btn {'active' if selected == '📡 Media Mod + přijímač' else ''}">📡 Media Mod + přijímač</div>
    <div class="segment-btn {'active' if selected == '⚡ Rychlý tahák' else ''}">⚡ Rychlý tahák</div>
</div>
""", unsafe_allow_html=True)

# === HLAVNÍ OBSAH ===
st.markdown('<div class="glass">', unsafe_allow_html=True)

if selected == "🔵 Přímé Bluetooth":
    st.header("🔵 Postup pro přímé Bluetooth spojení")
    c1, c2 = st.columns([1.7, 1])
    with c1:
        st.video("https://www.youtube.com/watch?v=LXb3EKWsInQ")
    with c2:
        st.markdown("### Příprava mikrofonu\n1. Vyjmi mikrofon z dokovací stanice...\n...")

elif selected == "📡 Media Mod + přijímač":
    st.header("📡 Propojení kamery s Media Modem a přijímačem RX")
    c1, c2 = st.columns([1.7, 1])
    with c1:
        st.markdown("""
        <iframe src="https://legogroup-my.sharepoint.com/..." width="100%" height="420" frameborder="0" allowfullscreen></iframe>
        """, unsafe_allow_html=True)
    with c2:
        st.markdown("### Instalace Media Modu\n1. Odstraň dvířka...\n...")

else:
    st.header("⚡ Rychlý obrázkový tahák")
    st.image("https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro%20propojen%C3%AD.png", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# === TIPS (pravý sloupec) ===
st.divider()
left, right = st.columns([3, 2])
with right:
    st.subheader("💡 Tipy a triky")
    # ... manuály jako dříve ...

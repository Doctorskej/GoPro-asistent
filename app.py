import streamlit as st

st.set_page_config(
    page_title="GoPro Asistent",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== CSS - VYLEPŠENÝ GLASSMORPHISM + SKRYTÍ TOOLBARU ====================
pozadi_url = "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=2000&auto=format&fit=crop"

st.markdown(f"""
<style>
    /* ... (všechny předchozí styly zůstávají stejné) ... */

    /* === SJEDNOCENÍ VELIKOSTI NADPISŮ v patičce === */
    h1, h2, h3 {{
        color: #00AEEF !important; 
        font-weight: 800; 
        text-shadow: 2px 2px 6px rgba(0,0,0,0.6) !important;
        margin-bottom: 1.2rem;
    }}

    /* Tipy a řešení (header) - mírně větší */
    .stHeader h2 {{
        font-size: 1.85rem !important;
    }}

    /* Manuály (nyní markdown) - stejná velikost jako header */
    .manual-section {{
        font-size: 1.85rem !important;
        font-weight: 800 !important;
        color: #00AEEF !important;
        margin-bottom: 1.2rem;
    }}

    /* Zbytek CSS zůstává stejný jako v předchozí verzi */
    .glass-card {{
        background: rgba(0, 0, 0, 0.68) !important;
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        border-radius: 20px;
        padding: 2.8rem;
        box-shadow: 0 15px 45px rgba(0, 0, 0, 0.65);
    }}

    p, li, [data-testid="stMarkdownContainer"] p, [data-testid="stMarkdownContainer"] li {{
        color: #FFFFFF !important;
        font-weight: 500 !important;
        text-shadow: 1.5px 1.5px 4px rgba(0,0,0,0.85) !important;
        line-height: 1.65;
    }}

    .manual-card {{
        background: rgba(255, 255, 255, 0.075) !important;
        border: 1px solid rgba(0, 174, 239, 0.4) !important;
        border-radius: 18px;
        padding: 1.5rem 2rem;
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        gap: 16px;
        font-size: 1.2rem;
        font-weight: 600;
        color: #FFFFFF !important;
        text-decoration: none !important;
        transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
        backdrop-filter: blur(12px);
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.45);
    }}
    .manual-card:hover {{
        background: rgba(0, 174, 239, 0.18) !important;
        border-color: #00AEEF !important;
        transform: translateY(-5px);
        box-shadow: 0 15px 35px rgba(0, 174, 239, 0.35);
    }}
    .manual-card::before {{
        content: "📘";
        font-size: 1.9rem;
        flex-shrink: 0;
    }}

    /* Silné skrývání horního toolbaru */
    header[data-testid="stHeader"],
    div[data-testid="stToolbar"],
    #GithubIcon,
    button[aria-label*="GitHub"],
    button[aria-label*="Fork"],
    button[aria-label*="Share"],
    [data-testid="stDecoration"],
    footer {{
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
    }}
</style>
""", unsafe_allow_html=True)

# ==================== OBSAH (stejný jako dříve) ====================
st.title("📹 GoPro Asistent")
st.markdown("**Průvodce pro Hero 13 + DJI Mic 3 v průmyslovém provozu**")

tab1, tab2, tab3 = st.tabs(["🔵 Připojení jednoho mikrofonu", "📡 Připojení obou mikrofonů", "⚡ Tahák"])

# ... (tab1, tab2, tab3 zůstávají beze změny - zkopíruj je z předchozí verze) ...

# ==================== PATIČKA – OPRAVENÁ ====================
st.divider()
col_left, col_right = st.columns([3, 2], gap="large")

with col_right:
    st.header("💡 Tipy a řešení")   # ← zůstává header (větší)
    
    # ... expandery zůstávají stejné ...

    # Manuály – teď sjednocené velikostí
    st.markdown('<p class="manual-section">📚 Manuály</p>', unsafe_allow_html=True)
    
    u_g = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro13%20manual.pdf"
    u_d = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/DJI_Mic_3_User_Manual_CS%20(1).pdf"
    
    st.markdown(f'''
        <a href="{u_g}" target="_blank" style="text-decoration:none;">
            <div class="manual-card"><span>Manuál GoPro Hero 13</span></div>
        </a>
    ''', unsafe_allow_html=True)
    
    st.markdown(f'''
        <a href="{u_d}" target="_blank" style="text-decoration:none;">
            <div class="manual-card"><span>Manuál DJI Mic 3</span></div>
        </a>
    ''', unsafe_allow_html=True)

with col_left:
    st.info("**Tip:** Čočka **LINEAR** je nejlepší pro technickou dokumentaci – nedeformuje obraz stroje.")

st.caption("GoPro Asistent • Vylepšená verze • 2026")
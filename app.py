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
    /* 1. CELKOVÉ POZADÍ */
    .stApp {{
        background-image: linear-gradient(rgba(8, 12, 22, 0.82), rgba(8, 12, 22, 0.78)), url("{pozadi_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* 2. ZÁLOŽKY */
    .stTabs [data-baseweb="tab-highlight"] {{ background-color: transparent !important; height: 0 !important; }}
    .stTabs [data-baseweb="tab-border"] {{ display: none !important; }}
    .stTabs [data-baseweb="tab-list"] {{ gap: 16px; padding-bottom: 20px; }}
    .stTabs [data-baseweb="tab"] {{
        background: rgba(255, 255, 255, 0.09);
        border-radius: 16px;
        padding: 16px 28px;
        font-size: 1.12rem;
        font-weight: 600;
        color: #FFFFFF;
        border: 1px solid rgba(0, 174, 239, 0.35);
    }}
    .stTabs [data-baseweb="tab"]:hover {{ background: rgba(255, 255, 255, 0.14); }}
    .stTabs [data-baseweb="tab"][aria-selected="true"] {{
        background: rgba(0, 174, 239, 0.45) !important;
        border: 2px solid #00AEEF !important;
    }}

    /* 3. HLAVNÍ KARTY */
    .glass-card {{
        background: rgba(0, 0, 0, 0.68) !important;
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.18);
        border-radius: 20px;
        padding: 2.8rem;
        box-shadow: 0 15px 45px rgba(0, 0, 0, 0.65);
    }}

    /* 4. TEXT A NADPISY */
    p, li, [data-testid="stMarkdownContainer"] p, [data-testid="stMarkdownContainer"] li {{
        color: #FFFFFF !important;
        font-weight: 500 !important;
        text-shadow: 1.5px 1.5px 4px rgba(0,0,0,0.85) !important;
        line-height: 1.65;
    }}

    h1, h2, h3 {{ 
        color: #00AEEF !important; 
        font-weight: 800; 
        text-shadow: 2px 2px 6px rgba(0,0,0,0.6) !important;
    }}

    /* 5. EXPANDÉRY */
    div[data-testid="stExpander"] {{
        background-color: rgba(255, 255, 255, 0.06) !important;
        border: 1px solid rgba(0, 174, 239, 0.45) !important;
        border-radius: 16px !important;
        margin-bottom: 12px;
    }}
    div[data-testid="stExpander"] summary {{
        padding: 16px 20px;
    }}
    div[data-testid="stExpander"] summary:hover {{
        background-color: rgba(0, 174, 239, 0.18) !important;
    }}

    /* 6. MANUÁLOVÉ KARTY */
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

    /* === SILNÉ SKRYTÍ HORNÍHO BÍLÉHO TOOLBARU (Share, GitHub, atd.) === */
    header[data-testid="stHeader"],
    div[data-testid="stToolbar"],
    #GithubIcon,
    .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_,
    button[aria-label*="GitHub"],
    button[aria-label*="Fork"],
    button[aria-label*="Share"],
    [data-testid="stDecoration"],
    [data-testid="stStatusWidget"],
    #MainMenu,
    footer {{
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
        min-height: 0 !important;
        padding: 0 !important;
        margin: 0 !important;
    }}

    /* Extra ochrana pro novější verze Streamlit */
    .st-emotion-cache-1jc7ptx, 
    .e1ewe7hr3,
    .css-1jc7ptx {{
        display: none !important;
    }}

    /* Responsivita */
    @media (max-width: 768px) {{
        .glass-card {{ padding: 1.8rem; }}
        .manual-card {{ padding: 1.2rem 1.6rem; font-size: 1.1rem; }}
    }}
</style>
""", unsafe_allow_html=True)

# ==================== OBSAH ====================
st.title("📹 GoPro Asistent")
st.markdown("**Průvodce pro Hero 13 + DJI Mic 3**")

tab1, tab2, tab3 = st.tabs(["🔵 Připojení jednoho mikrofonu", "📡 Připojení obou mikrofonů", "⚡ Tahák"])

with tab1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("🔵 Postup pro přímé Bluetooth spojení")
    c1, c2 = st.columns([1.6, 1], gap="large")
    with c1:
        st.markdown("""<iframe src="https://legogroup-my.sharepoint.com/personal/jan_drvota_lego_com/_layouts/15/embed.aspx?UniqueId=ebf4b46d-f64e-485b-be85-5bcba5ba497d&embed=%7B%22ust%22%3Atrue%2C%22hv%22%3A%22CopyEmbedCode%22%7D&referrer=StreamWebApp&referrerScenario=EmbedDialog.Create" style="width: 100%; aspect-ratio: 16 / 9; border: none;" allowfullscreen></iframe>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""
        ### Jak se připojit:
        1. **Vyjmi mikrofon** (musí blikat zeleně).
        2. **Zapni GoPro** (boční tlačítko **MODE**).
        3. **V menu:** Swipe dolů → Swipe doleva.
        4. Stiskni **„Pair device“**.
        5. **Na mikrofonu:** 2x Link (modrá), pak podrž 3s (modro-zelená).
        6. **Na displeji:** Klikni na nalezený **DJI Mic 3 TX**.
        """)
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("📡 Připojení přes Media Mod")
    c1, c2 = st.columns([1.6, 1], gap="large")
    with c1:
        st.markdown("""<iframe src="https://legogroup-my.sharepoint.com/personal/jan_drvota_lego_com/_layouts/15/embed.aspx?UniqueId=061cd250-a744-4be2-8bd8-d404aed6f8d8&embed=%7B%22ust%22%3Atrue%2C%22hv%22%3A%22CopyEmbedCode%22%7D&referrer=StreamWebApp&referrerScenario=EmbedDialog.Create" style="width: 100%; aspect-ratio: 16 / 9; border: none;" allowfullscreen></iframe>""", unsafe_allow_html=True)
    with c2:
        st.markdown("""
        ### Jak se připojit:
        1. **Kamera:** Zasuň ji nadoraz do Media Modu.
        2. **Přijímač:** Vyjmi z pouzdra a potvrď **Confirm**.
        3. **Sáňky:** Nasuň přijímač do sáněk na Modu.
        4. **Kabel:** Propoj **OUT** a **spodní jack** na kameře.
        5. **Kontrola:** Na displeji se musí hýbat sloupce zvuku.
        """)
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro%20propojen%C3%AD.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== PATIČKA ====================
st.divider()
col_left, col_right = st.columns([3, 2], gap="large")

with col_right:
    st.header("💡 Tipy a řešení")
    
    with st.expander("📸 Doporučené profily nastavení kamery "):
        st.markdown("""
        **1. Celkové záběry linky / pracoviště** 
        * **Rozlišení:** 4K
        * **FPS:** 30
        * **Čočka:** Wide
        * **Stabilizace:** AutoBoost
        * **Barvy:** Natural

        **2. Technický detail a údržba**
        * **Rozlišení:** 4K
        * **FPS:** 30
        * **Čočka:** Linear (zásadní!)
        * **Horizon Lock:** Zapnuto
        * **Barvy:** Vibrant

        **3. Natáčení v temných prostorech**
        * **FPS:** 24
        * **ISO Max:** 1600
        * **Ostrost:** Medium
        * **Stabilizace:** Standard
        """)

    with st.expander("🛠️ Řešení problémů"):
        st.markdown("""
        * **Bez zvuku:** Kamera musí sedět nadoraz v Media Modu.
        * **Limit zvuku:** Snižte **Gain** na -6 nebo -12 dB.
        """)

    st.subheader("📚 Manuály")
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
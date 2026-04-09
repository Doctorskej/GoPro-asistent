import streamlit as st

st.set_page_config(
    page_title="GoPro Asistent",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== CSS - FIX PROBLIKÁVÁNÍ DO BÍLÉ ====================
pozadi_url = "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=2000&auto=format&fit=crop"

st.markdown(f"""
<style>
    /* 1. CELKOVÉ POZADÍ - Mírně zesvětlené, aby byla vidět fotka */
    .stApp {{
        background-image: linear-gradient(rgba(8, 12, 22, 0.8), rgba(8, 12, 22, 0.75)), url("{pozadi_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* 2. ZÁLOŽKY (TABS) */
    .stTabs [data-baseweb="tab-highlight"] {{ background-color: transparent !important; height: 0 !important; }}
    .stTabs [data-baseweb="tab-border"] {{ display: none !important; }}
    .stTabs [data-baseweb="tab-list"] {{ gap: 14px; padding-bottom: 15px; }}
    .stTabs [data-baseweb="tab"] {{
        background: rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 15px 26px;
        font-size: 1.1rem;
        font-weight: 600;
        color: #DDDDDD;
        border: 1px solid rgba(0, 174, 239, 0.3);
        transition: all 0.3s ease;
    }}
    .stTabs [data-baseweb="tab"]:hover {{ background: rgba(0, 174, 239, 0.18); border-color: #00AEEF; color: #FFFFFF; }}
    .stTabs [data-baseweb="tab"][aria-selected="true"] {{
        background: rgba(0, 174, 239, 0.32) !important;
        border: 2px solid #00AEEF !important;
        color: #FFFFFF !important;
        box-shadow: 0 0 25px rgba(0, 174, 239, 0.4);
    }}

    /* 3. OPRAVA EXPANDERŮ - KONSTANTNÍ BARVA BEZ BÍLÉ */
    /* Celý kontejner expanderu */
    div[data-testid="stExpander"] {{
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(0, 174, 239, 0.4) !important;
        border-radius: 14px !important;
        margin-bottom: 12px;
    }}

    /* Hlavička expanderu (to, na co klikáš) */
    div[data-testid="stExpander"] summary {{
        background-color: transparent !important;
        color: #FFFFFF !important;
        padding: 10px 15px !important;
    }}

    /* Vynucení barvy při najetí myší (HOVER) - ZABRÁNÍ ZBĚLÁNÍ */
    div[data-testid="stExpander"] summary:hover, 
    div[data-testid="stExpander"] summary:focus,
    div[data-testid="stExpander"]:hover {{
        background-color: rgba(0, 174, 239, 0.1) !important;
        color: #00AEEF !important;
    }}

    /* Vnitřní obsah expanderu */
    div[data-testid="stExpander"] [data-testid="stExpanderDetails"] {{
        background-color: transparent !important;
        padding: 20px !important;
        border-top: 1px solid rgba(0, 174, 239, 0.2);
    }}

    /* Barva textu v expanderu */
    div[data-testid="stExpander"] p, 
    div[data-testid="stExpander"] li,
    div[data-testid="stExpander"] span {{
        color: #FFFFFF !important;
    }}

    /* HLAVNÍ KARTY */
    .glass-card {{
        background: rgba(255, 255, 255, 0.09) !important;
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 18px;
        padding: 2.2rem;
    }}

    h1 {{ color: #00AEEF !important; font-weight: 800; }}
    h2, h3 {{ color: #FFFFFF !important; font-weight: 700; }}
    
    .manual-card {{
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(0, 174, 239, 0.35);
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 16px;
        display: flex;
        align-items: center;
    }}
    img, iframe, video {{ border-radius: 16px; box-shadow: 0 12px 35px rgba(0, 0, 0, 0.5); }}
</style>
""", unsafe_allow_html=True)

# ==================== OBSAH APLIKACE ====================
st.title("📹 GoPro Asistent")
st.markdown("**Návod pro nahrávání údržby a technických instruktáží (Hero 13 + DJI Mic 3)**")

tab1, tab2, tab3 = st.tabs(["🔵 Bluetooth", "📡 Media Mod", "⚡ Rychlý tahák"])

with tab1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("🔵 Přímé připojení Bluetooth")
    col_v, col_t = st.columns([1.65, 1], gap="large")
    with col_v:
        st.markdown("""<iframe src="https://legogroup-my.sharepoint.com/personal/jan_drvota_lego_com/_layouts/15/embed.aspx?UniqueId=ebf4b46d-f64e-485b-be85-5bcba5ba497d&embed=%7B%22ust%22%3Atrue%2C%22hv%22%3A%22CopyEmbedCode%22%7D&referrer=StreamWebApp&referrerScenario=EmbedDialog.Create" style="width: 100%; aspect-ratio: 16 / 9; border: none;" allowfullscreen></iframe>""", unsafe_allow_html=True)
    with col_t:
        st.markdown("""
        1. **Vyjmi mikrofon** (bliká zeleně).
        2. **Zapni kameru** (tlačítko **MODE**).
        3. **Menu:** Přejeď dolů -> doleva.
        4. **Párování:** Zvol **„Pair device“**.
        5. **Link:** 2x stiskni Link na mikrofonu (modrá), pak podrž 3s (modro-zelená).
        6. **Potvrď:** Klikni na nalezený **DJI Mic 3 TX**.
        """)
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("📡 Připojení přes Media Mod")
    col_v, col_t = st.columns([1.65, 1], gap="large")
    with col_v:
        st.markdown("""<iframe src="https://legogroup-my.sharepoint.com/personal/jan_drvota_lego_com/_layouts/15/embed.aspx?UniqueId=061cd250-a744-4be2-8bd8-d404aed6f8d8&embed=%7B%22ust%22%3Atrue%2C%22hv%22%3A%22CopyEmbedCode%22%7D&referrer=StreamWebApp&referrerScenario=EmbedDialog.Create" style="width: 100%; aspect-ratio: 16 / 9; border: none;" allowfullscreen></iframe>""", unsafe_allow_html=True)
    with col_t:
        st.markdown("""
        1. **Vlož kameru** nadoraz do Media Modu.
        2. **Zapni přijímač** a potvrď **Confirm**.
        3. **Nasuň přijímač** do sáněk Modu.
        4. **Propoj kabelem:** OUT -> spodní jack kamery.
        5. **Kontrola:** Na displeji ověř ikonu mikrofonu.
        """)
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro%20propojen%C3%AD.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== PATIČKA S TIPY ====================
st.divider()
c_l, c_r = st.columns([3, 2], gap="large")

with c_l:
    st.info("**Průmyslový tip:** Pro technická videa vždy nastavte čočku **LINEAR**, aby nedocházelo k deformaci strojů.")

with c_r:
    st.header("💡 Tipy a řešení")

    with st.expander("📸 Doporučené průmyslové profily"):
        st.markdown("""
        **1. Celkové záběry linky** Rozlišení: 4K / 30 FPS, Čočka: Wide (Široká).
        
        **2. Technický detail a údržba** Čočka: **LINEAR** (nedeformuje obraz), Horizon Lock: Zapnuto.
        
        **3. Temné prostory** FPS: 24 (více světla), ISO Max: 1600.
        """)

    with st.expander("🛠️ Řešení problémů (Troubleshooting)"):
        st.markdown("""
        * **Kamera nevidí mikrofon:** Vypni Bluetooth v mobilu, mikrofon se k němu možná "přilepil".
        * **Není slyšet zvuk:** Zkontroluj, zda je kamera v Modu doražená až nadoraz na USB-C.
        * **Příliš hlasitý zvuk:** Pokud indikátor na displeji dosahuje červených hodnot, na přijímači snižte **Gain** na -6 nebo -12 dB.
        """)

    st.subheader("📚 Manuály")
    u_g = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro13%20manual.pdf"
    u_d = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/DJI_Mic_3_User_Manual_CS%20(1).pdf"
    st.markdown(f'<a href="{u_g}" target="_blank" style="text-decoration:none;"><div class="manual-card">📘 Manuál GoPro Hero 13</div></a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{u_d}" target="_blank" style="text-decoration:none;"><div class="manual-card">📘 Manuál DJI Mic 3</div></a>', unsafe_allow_html=True)
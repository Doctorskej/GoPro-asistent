import streamlit as st

st.set_page_config(
    page_title="GoPro Asistent",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== CSS ====================
pozadi_url = "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=2000&auto=format&fit=crop"

st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(8, 12, 22, 0.94), rgba(8, 12, 22, 0.91)), url("{pozadi_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

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

    .glass-card {{
        background: rgba(255, 255, 255, 0.09) !important;
        backdrop-filter: blur(16px);
        border: 1px solid rgba(0, 174, 239, 0.3);
        border-radius: 18px;
        padding: 2.2rem;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.45);
    }}

    h1 {{ color: #00AEEF !important; font-weight: 800; letter-spacing: -0.03em; }}
    h2, h3 {{ color: #FFFFFF !important; font-weight: 700; }}
    p, li {{ color: #EEEEEE !important; font-size: 1.08rem; line-height: 1.65; }}

    .stExpander {{
        background: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(0, 174, 239, 0.2) !important;
        border-radius: 14px !important;
        margin-bottom: 10px;
    }}

    .manual-card {{
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(0, 174, 239, 0.35);
        border-radius: 16px;
        padding: 1.5rem 1.8rem;
        margin-bottom: 16px;
        display: flex;
        align-items: center;
        transition: all 0.3s ease;
    }}
    .manual-card:hover {{ background: rgba(0, 174, 239, 0.16); border-color: #00AEEF; transform: translateY(-3px); }}
    .manual-card-icon {{ font-size: 2.3rem; margin-right: 20px; color: #00AEEF; }}
    .manual-card-text {{ font-size: 1.18rem; font-weight: 600; color: #FFFFFF; }}

    img, iframe, video {{ border-radius: 16px; box-shadow: 0 12px 35px rgba(0, 0, 0, 0.5); }}
</style>
""", unsafe_allow_html=True)

# ==================== HLAVIČKA ====================
st.title("📹 GoPro Asistent")
st.markdown("**Průmyslový standard pro nahrávání údržby a instruktážních videí (Hero 13 + DJI Mic 3)**")

# ==================== TABS ====================
tab1, tab2, tab3 = st.tabs([
    "🔵 Přímé Bluetooth – jeden mikrofon",
    "📡 Media Mod + bezdrátový přijímač",
    "⚡ Rychlý obrázkový tahák"
])

with tab1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("🔵 Propojení kamery a jednoho mikrofonu přes Bluetooth")
    col_video, col_text = st.columns([1.65, 1], gap="large")
    with col_video:
        st.subheader("🎥 Videonávod")
        st.markdown("""
        <iframe src="https://legogroup-my.sharepoint.com/personal/jan_drvota_lego_com/_layouts/15/embed.aspx?UniqueId=ebf4b46d-f64e-485b-be85-5bcba5ba497d&embed=%7B%22ust%22%3Atrue%2C%22hv%22%3A%22CopyEmbedCode%22%7D&referrer=StreamWebApp&referrerScenario=EmbedDialog.Create" 
                style="width: 100%; aspect-ratio: 16 / 9; border: none;" allowfullscreen></iframe>
        """, unsafe_allow_html=True)
    with col_text:
        st.markdown("""
        ### Postup připojení
        1. **Vyjmi mikrofon** z dokovací stanice.
        2. **Zkontroluj zapnutí:** (bliká zelené tlačítko).
        3. **Zapni kameru** (tlačítko **MODE**).
        4. **Přejeď prstem** od shora dolů a pak **doleva**.
        5. Stiskni **„Pair device“**.
        6. Stiskni **2x tlačítko připojení** na mikrofonu.
        7. **Podrž tlačítko na 3 vteřiny** (modro-zelené blikání).
        8. Na displeji kamery potvrď **DJI Mic 3 TX**.
        """)
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("📡 Propojení přes Media Mod (Kabelové)")
    col_video, col_text = st.columns([1.65, 1], gap="large")
    with col_video:
        st.subheader("🎥 Videonávod")
        st.markdown("""
        <iframe src="https://legogroup-my.sharepoint.com/personal/jan_drvota_lego_com/_layouts/15/embed.aspx?UniqueId=061cd250-a744-4be2-8bd8-d404aed6f8d8&embed=%7B%22ust%22%3Atrue%2C%22hv%22%3A%22CopyEmbedCode%22%7D&referrer=StreamWebApp&referrerScenario=EmbedDialog.Create" 
                style="width: 100%; aspect-ratio: 16 / 9; border: none;" allowfullscreen></iframe>
        """, unsafe_allow_html=True)
    with col_text:
        st.markdown("""
        ### Postup připojení
        1. **Vlož kameru** nadoraz do Media Modu.
        2. **Vyjmi přijímač** a potvrď **Confirm**.
        3. **Nasuň přijímač** do sáněk Media Modu.
        4. **Zapoj kabel** do přijímače (**Out**) a do kamery (**spodní jack**).
        5. **Zapni kameru**.
        """)
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("⚡ Rychlý obrázkový tahák")
    raw_image_url = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro%20propojen%C3%AD.png"
    st.image(raw_image_url, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== FOOTER SECTION ====================
st.divider()
col_l, col_r = st.columns([3, 2], gap="large")

with col_l:
    st.info("**Průmyslový tip:** Pro technická videa používejte vždy Lineární čočku (Linear), aby nedocházelo k deformaci strojů a linky.")

with col_r:
    st.header("💡 Tipy a triky")

    with st.expander("📸 Doporučené průmyslové profily"):
        st.subheader("1. Celkové záběry linky / pracoviště")
        st.markdown("""
        * **Rozlišení:** 4K / **FPS:** 30.
        * **Čočka (Lens):** **Wide (Široká)** – maximální přehled.
        * **Stabilizace:** AutoBoost.
        * **Barvy:** Natural.
        """)
        
        st.subheader("2. Technický detail a údržba (Makro)")
        st.markdown("""
        * **Rozlišení:** 4K / **FPS:** 30.
        * **Čočka (Lens):** **Linear (Lineární)** – Žádné rybí oko.
        * **Horizon Lock:** Zapnuto.
        * **Barvy:** Vibrant (zvýrazní barevné kabely).
        """)
        
        st.subheader("3. Inspekce v temných prostorech")
        st.markdown("""
        * **FPS:** 24 / **ISO Max:** 1600.
        * **Stabilizace:** Standard.
        """)

    with st.expander("🛠️ Řešení problémů (Troubleshooting)"):
        st.subheader("🔵 Bluetooth")
        st.markdown("""* **Kamera nevidí mikrofon:** Vypni Bluetooth v mobilu, mikrofon se k němu možná "přilepil".""")
        st.subheader("📡 Media Mod")
        st.markdown("""* **Není slyšet zvuk:** Zkontroluj, zda je kamera v Modu doražená až nadoraz na USB-C.""")
        st.markdown("""* **Lupání:** Dotlač jack kabel v přijímači i kameře (musí cvaknout).""")

    st.subheader("📚 Dokumentace")
    url_gopro = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro13%20manual.pdf"
    url_dji = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/DJI_Mic_3_User_Manual_CS%20(1).pdf"
    st.markdown(f'<a href="{url_gopro}" target="_blank" style="text-decoration:none;"><div class="manual-card"><span class="manual-card-icon">📘</span><span class="manual-card-text">Manuál GoPro Hero 13</span></div></a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{url_dji}" target="_blank" style="text-decoration:none;"><div class="manual-card"><span class="manual-card-icon">📘</span><span class="manual-card-text">Manuál DJI Mic 3</span></div></a>', unsafe_allow_html=True)
import streamlit as st

st.set_page_config(
    page_title="GoPro Asistent",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== CSS - BEZ ČERVENÉHO PODTRŽENÍ + LEPŠÍ ČITELNOST ====================
pozadi_url = "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=2000&auto=format&fit=crop"

st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(8, 12, 22, 0.94), rgba(8, 12, 22, 0.91)), url("{pozadi_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* === ODSTRANĚNÍ ČERVENÉHO PODTRŽENÍ === */
    .stTabs [data-baseweb="tab-highlight"] {{
        background-color: transparent !important;
        height: 0 !important;
    }}
    .stTabs [data-baseweb="tab-border"] {{
        display: none !important;
    }}

    /* Moderní tabs styl */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 14px;
        padding-bottom: 15px;
    }}
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
    .stTabs [data-baseweb="tab"]:hover {{
        background: rgba(0, 174, 239, 0.18);
        border-color: #00AEEF;
        color: #FFFFFF;
    }}
    .stTabs [data-baseweb="tab"][aria-selected="true"] {{
        background: rgba(0, 174, 239, 0.32) !important;
        border: 2px solid #00AEEF !important;
        color: #FFFFFF !important;
        box-shadow: 0 0 25px rgba(0, 174, 239, 0.4);
    }}

    /* Glass karty + lepší čitelnost */
    .glass-card {{
        background: rgba(255, 255, 255, 0.09) !important;
        backdrop-filter: blur(16px);
        border: 1px solid rgba(0, 174, 239, 0.3);
        border-radius: 18px;
        padding: 2.2rem;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.45);
    }}

    h1 {{
        color: #00AEEF !important;
        font-weight: 800;
        letter-spacing: -0.03em;
    }}
    h2, h3 {{
        color: #FFFFFF !important;
        font-weight: 700;
    }}

    p, li {{
        color: #EEEEEE !important;
        font-size: 1.08rem;
        line-height: 1.65;
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
    .manual-card:hover {{
        background: rgba(0, 174, 239, 0.16);
        border-color: #00AEEF;
        transform: translateY(-3px);
    }}
    .manual-card-icon {{
        font-size: 2.3rem;
        margin-right: 20px;
        color: #00AEEF;
    }}
    .manual-card-text {{
        font-size: 1.18rem;
        font-weight: 600;
        color: #FFFFFF;
    }}

    img, iframe, video {{
        border-radius: 16px;
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.5);
    }}
</style>
""", unsafe_allow_html=True)

# ==================== HLAVIČKA ====================
st.title("📹 GoPro Asistent")
st.markdown("**Praktický průvodce propojením GoPro Hero 13 + DJI Mic 3**")

# ==================== TABS ====================
tab1, tab2, tab3 = st.tabs([
    "🔵 Přímé Bluetooth – jeden mikrofon",
    "📡 Media Mod + bezdrátový přijímač",
    "⚡ Rychlý obrázkový tahák"
])

with tab1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("🔵 Postup pro přímé Bluetooth spojení")
    col_video, col_text = st.columns([1.65, 1], gap="large")
    with col_video:
        st.subheader("🎥 Videonávod")
        # --- VLOŽENÝ NOVÝ SHAREPOINT ODKAZ ---
        st.markdown("""
        <iframe src="https://legogroup-my.sharepoint.com/personal/jan_drvota_lego_com/_layouts/15/embed.aspx?UniqueId=ebf4b46d-f64e-485b-be85-5bcba5ba497d&embed=%7B%22ust%22%3Atrue%2C%22hv%22%3A%22CopyEmbedCode%22%7D&referrer=StreamWebApp&referrerScenario=EmbedDialog.Create" 
                width="100%" height="400" frameborder="0" scrolling="no" allowfullscreen title="GoPro mikrofon.mp4"></iframe>
        """, unsafe_allow_html=True)
    with col_text:
        st.markdown("""
        ### Příprava mikrofonu
        1. **Vyjmi mikrofon** z dokovací stanice DJI.  
        2. **Zkontroluj napájení:** Zapnutý = bliká zelené tlačítko.
        
        ### Nastavení kamery
        3. **Zapni kameru** (boční tlačítko `MODE`).  
        4. **Přejeď prstem dolů** a pak **doleva**.  
        5. Stiskni **„Pair device“**.
        
        ### Samotné párování
        6. Na mikrofonu **podrž tlačítko Link**.  
        7. Na displeji kamery klikni na **DJI Mic 3 TX**.
        """)
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("📡 Propojení kamery s Media Modem a přijímačem RX")
    col_video, col_text = st.columns([1.65, 1], gap="large")
    with col_video:
        st.subheader("🎥 Videonávod")
        st.markdown("""
        <iframe src="https://legogroup-my.sharepoint.com/personal/jan_drvota_lego_com/_layouts/15/embed.aspx?UniqueId=061cd250-a744-4be2-8bd8-d404aed6f8d8&embed=%7B%22ust%22%3Atrue%2C%22hv%22%3A%22CopyEmbedCode%22%7D&referrer=StreamWebApp&referrerScenario=EmbedDialog.Create" 
                width="100%" height="400" frameborder="0" scrolling="no" allowfullscreen title="GoPro přijímač.mp4"></iframe>
        """, unsafe_allow_html=True)
    with col_text:
        st.markdown("""
        ### Instalace Media Modu
        1. **Odstraň dvířka** kamery.  
        2. **Vlož kameru** do Media Modu.  
        3. **Zavři Media Mod**.
        
        ### Příprava DJI přijímače
        4. **Vyjmi přijímač** z pouzdra.  
        5. **Potvrď informaci** na displeji (Confirm).
        
        ### Fyzické propojení
        6. **Nasuň přijímač** na Media Mod.  
        7. **Zapoj kabel** do přijímače (OUT) a do kamery.
        """)
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("⚡ Rychlý obrázkový tahák")
    st.markdown("*Kliknutím na obrázek si ho můžeš zvětšit.*")
    raw_image_url = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro%20propojen%C3%AD.png"
    st.image(raw_image_url, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== TIPS ====================
st.divider()

col_l, col_r = st.columns([3, 2], gap="large")

with col_r:
    st.header("💡 Tipy a triky")
    st.subheader("🎥 Videonávody")
    st.markdown("- [Uchycení GoPro na rám](https://www.youtube.com/watch?v=LXb3EKWsInQ)\n- [Expozice v temné hale](https://www.youtube.com/watch?v=LXb3EKWsInQ)")
    
    st.subheader("📚 Manuály")
    url_gopro = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro13%20manual.pdf"
    url_dji = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/DJI_Mic_3_User_Manual_CS%20(1).pdf"
    
    st.markdown(f"""
    <a href="{url_gopro}" target="_blank" style="text-decoration:none;">
        <div class="manual-card"><span class="manual-card-icon">📘</span><span class="manual-card-text">Manuál GoPro Hero 13</span></div>
    </a>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <a href="{url_dji}" target="_blank" style="text-decoration:none;">
        <div class="manual-card"><span class="manual-card-icon">📘</span><span class="manual-card-text">Manuál DJI Mic 3</span></div>
    </a>
    """, unsafe_allow_html=True)

with col_l:
    st.info("**Tip pro použití v terénu:** Otevři appku na mobilu v plném režimu. Všechny kroky jsou testovány na GoPro Hero 13 + DJI Mic 3.")
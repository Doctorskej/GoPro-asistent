import streamlit as st

# ==================== NASTAVENÍ ====================
st.set_page_config(
    page_title="GoPro Asistent",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== CSS - BEZ ČERVENÉHO PODTRŽENÍ ====================
pozadi_url = "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=2000&auto=format&fit=crop"

st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(10, 15, 25, 0.93), rgba(10, 15, 25, 0.89)), url("{pozadi_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Moderní tabs bez červené čáry */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 16px;
        padding-bottom: 20px;
    }}
    .stTabs [data-baseweb="tab"] {{
        background: rgba(255, 255, 255, 0.07);
        border-radius: 14px;
        padding: 16px 28px;
        font-size: 1.08rem;
        font-weight: 600;
        color: #CCCCCC;
        border: 1px solid rgba(0, 174, 239, 0.25);
        transition: all 0.3s ease;
    }}
    .stTabs [data-baseweb="tab"]:hover {{
        background: rgba(0, 174, 239, 0.15);
        border-color: #00AEEF;
        color: white;
    }}
    /* Aktivní záložka - modrý glow, žádná červená čára */
    .stTabs [data-baseweb="tab"][aria-selected="true"] {{
        background: rgba(0, 174, 239, 0.28) !important;
        border: 2px solid #00AEEF !important;
        color: #FFFFFF !important;
        box-shadow: 0 0 22px rgba(0, 174, 239, 0.45);
    }}

    .glass-card {{
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(14px);
        border: 1px solid rgba(0, 174, 239, 0.25);
        border-radius: 18px;
        padding: 2rem;
        box-shadow: 0 10px 35px rgba(0, 0, 0, 0.4);
    }}

    h1 {{
        color: #00AEEF !important;
        font-weight: 800;
        letter-spacing: -0.02em;
    }}
    h2, h3 {{
        color: #FFFFFF !important;
    }}

    .manual-card {{
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(0, 174, 239, 0.3);
        border-radius: 16px;
        padding: 1.4rem 1.8rem;
        margin-bottom: 14px;
        display: flex;
        align-items: center;
        transition: all 0.3s ease;
    }}
    .manual-card:hover {{
        background: rgba(0, 174, 239, 0.14);
        border-color: #00AEEF;
        transform: translateY(-2px);
    }}
    .manual-card-icon {{
        font-size: 2.2rem;
        margin-right: 18px;
        color: #00AEEF;
    }}
    .manual-card-text {{
        font-size: 1.15rem;
        font-weight: 600;
        color: #FFFFFF;
    }}

    img, iframe, video {{
        border-radius: 16px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.45);
    }}
</style>
""", unsafe_allow_html=True)

# ==================== HLAVIČKA ====================
st.title("📹 GoPro Asistent")
st.markdown("**Praktický průvodce propojením GoPro Hero 13 + DJI Mic 3**")

# ==================== TABS (bez červeného podtržení) ====================
tab1, tab2, tab3 = st.tabs([
    "🔵 Přímé Bluetooth – jeden mikrofon",
    "📡 Media Mod + bezdrátový přijímač",
    "⚡ Rychlý obrázkový tahák"
])

# --- TAB 1 ---
with tab1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("🔵 Postup pro přímé Bluetooth spojení")
    
    col_video, col_text = st.columns([1.65, 1], gap="large")
    with col_video:
        st.subheader("🎥 Videonávod")
        st.video("https://www.youtube.com/watch?v=LXb3EKWsInQ")
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

# --- TAB 2 ---
with tab2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("📡 Propojení kamery s Media Modem a přijímačem RX")
    
    col_video, col_text = st.columns([1.65, 1], gap="large")
    with col_video:
        st.subheader("🎥 Videonávod")
        st.markdown("""
        <iframe src="https://legogroup-my.sharepoint.com/personal/jan_drvota_lego_com/_layouts/15/embed.aspx?UniqueId=061cd250-a744-4be2-8bd8-d404aed6f8d8&embed=%7B%22ust%22%3Atrue%2C%22hv%22%3A%22CopyEmbedCode%22%7D&referrer=StreamWebApp&referrerScenario=EmbedDialog.Create" 
                width="100%" height="400" frameborder="0" scrolling="no" allowfullscreen></iframe>
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

# --- TAB 3 ---
with tab3:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("⚡ Rychlý obrázkový tahák")
    st.markdown("*Rychlý přehled pro zapojení. Kliknutím na obrázek si ho můžeš zvětšit.*")
    
    raw_image_url = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro%20propojen%C3%AD.png"
    st.image(raw_image_url, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== TIPS SEKCE ====================
st.divider()

col_left, col_right = st.columns([3, 2], gap="large")

with col_right:
    st.header("💡 Tipy a triky")
    
    st.subheader("🎥 Videonávody")
    st.markdown("""
    • [Jak správně uchytit GoPro na rám stroje](https://www.youtube.com/watch?v=LXb3EKWsInQ)  
    • [Jak nastavit expozici v temné hale](https://www.youtube.com/watch?v=LXb3EKWsInQ)
    """)
    
    st.subheader("📚 Manuály")
    url_gopro = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro13%20manual.pdf"
    url_dji = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/DJI_Mic_3_User_Manual_CS%20(1).pdf"
    
    st.markdown(f"""
    <a href="{url_gopro}" target="_blank" style="text-decoration: none;">
        <div class="manual-card">
            <span class="manual-card-icon">📘</span>
            <span class="manual-card-text">Otevřít manuál k GoPro 13</span>
        </div>
    </a>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <a href="{url_dji}" target="_blank" style="text-decoration: none;">
        <div class="manual-card">
            <span class="manual-card-icon">📘</span>
            <span class="manual-card-text">Otevřít manuál k DJI Mic 3</span>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col_left:
    st.info("**Tip:** Appka funguje nejlépe na mobilu v plném režimu. Všechny postupy jsou ověřené na GoPro Hero 13 + DJI Mic 3.")

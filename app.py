import streamlit as st

# ==================== NASTAVENÍ STRÁNKY ====================
st.set_page_config(
    page_title="GoPro Asistent",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== VLASTNÍ MODERNÍ CSS (glassmorphism + GoPro style) ====================
pozadi_url = "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=2000&auto=format&fit=crop"

st.markdown(f"""
<style>
    /* Hlavní pozadí s jemnějším gradientem */
    .stApp {{
        background-image: linear-gradient(rgba(10, 15, 25, 0.92), rgba(10, 15, 25, 0.88)), url("{pozadi_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Glassmorphism kontejnery */
    .glass-card {{
        background: rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(0, 174, 239, 0.25);
        border-radius: 16px;
        padding: 1.8rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }}
    .glass-card:hover {{
        border-color: #00AEEF;
        box-shadow: 0 12px 40px rgba(0, 174, 239, 0.25);
    }}

    /* Nadpisy */
    h1 {{
        color: #00AEEF !important;
        font-weight: 800 !important;
        letter-spacing: -0.02em;
    }}
    h2, h3 {{
        color: #FFFFFF !important;
        font-weight: 700 !important;
    }}

    /* Tabs styling - moderní GoPro look */
    .stTabs [data-baseweb="tab-list"] {{
        gap: 12px;
        padding-bottom: 10px;
    }}
    .stTabs [data-baseweb="tab"] {{
        background: rgba(255, 255, 255, 0.06);
        border-radius: 12px;
        padding: 14px 24px;
        font-weight: 600;
        transition: all 0.2s ease;
    }}
    .stTabs [data-baseweb="tab"]:hover {{
        background: rgba(0, 174, 239, 0.15);
    }}
    .stTabs [aria-selected="true"] {{
        background: rgba(0, 174, 239, 0.25) !important;
        border: 1px solid #00AEEF !important;
        color: #FFFFFF !important;
        box-shadow: 0 0 15px rgba(0, 174, 239, 0.3);
    }}

    /* Text a odrážky */
    p, li, label {{
        color: #E0E0E0 !important;
        font-size: 1.05rem;
        line-height: 1.6;
    }}

    /* Vylepšené manuálové karty */
    .manual-card {{
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(0, 174, 239, 0.3);
        border-radius: 14px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        transition: all 0.3s ease;
    }}
    .manual-card:hover {{
        background: rgba(0, 174, 239, 0.12);
        border-color: #00AEEF;
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(0, 174, 239, 0.2);
    }}
    .manual-card-icon {{
        font-size: 2rem;
        margin-right: 16px;
        color: #00AEEF;
    }}
    .manual-card-text {{
        color: #FFFFFF !important;
        font-size: 1.1rem;
        font-weight: 600;
    }}

    /* Obrázky a videa */
    img, iframe, video {{
        border-radius: 14px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
    }}

    /* Tipy sekce */
    .tips-container {{
        background: rgba(255, 255, 255, 0.06);
        backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: 1.8rem;
        border: 1px solid rgba(255,255,255,0.1);
    }}
</style>
""", unsafe_allow_html=True)

# ==================== HLAVNÍ OBSAH ====================
st.title("📹 GoPro Asistent")
st.markdown("**Praktický průvodce propojením GoPro Hero 13 + DJI Mic 3**")

# Tabs místo radio buttons
tab1, tab2, tab3 = st.tabs([
    "🔵 Přímé Bluetooth – jeden mikrofon",
    "📡 Media Mod + bezdrátový přijímač",
    "⚡ Rychlý obrázkový tahák"
])

# --- TAB 1 ---
with tab1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("🔵 Postup pro přímé Bluetooth spojení")
    
    col_video, col_text = st.columns([1.6, 1], gap="large")
    
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
    
    col_video, col_text = st.columns([1.6, 1], gap="large")
    
    with col_video:
        st.subheader("🎥 Videonávod")
        st.markdown("""
        <iframe src="https://legogroup-my.sharepoint.com/personal/jan_drvota_lego_com/_layouts/15/embed.aspx?UniqueId=061cd250-a744-4be2-8bd8-d404aed6f8d8&embed=%7B%22ust%22%3Atrue%2C%22hv%22%3A%22CopyEmbedCode%22%7D&referrer=StreamWebApp&referrerScenario=EmbedDialog.Create" 
                width="100%" height="380" frameborder="0" scrolling="no" allowfullscreen></iframe>
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
    st.header("⚡ Fast manual propojení")
    st.markdown("*Rychlý přehled pro zapojení bez zbytečných řečí. Kliknutím na obrázek si ho můžeš zvětšit.*")
    
    raw_image_url = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro%20propojen%C3%AD.png"
    st.image(raw_image_url, use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== PRAVÝ SLOUPEC / Tipy ====================
st.divider()

col_left, col_right = st.columns([3, 2], gap="large")

with col_right:
    st.markdown('<div class="tips-container">', unsafe_allow_html=True)
    st.header("💡 Tipy a triky")
    
    st.subheader("🎥 Užitečné videonávody")
    st.markdown("""
    - [Jak správně uchytit GoPro na rám stroje](https://www.youtube.com/watch?v=LXb3EKWsInQ)
    - [Jak nastavit expozici v temné hale](https://www.youtube.com/watch?v=LXb3EKWsInQ)
    """)
    
    st.subheader("📚 Oficiální manuály")
    
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
    st.markdown('</div>', unsafe_allow_html=True)

with col_left:
    st.info("**Tip:** Na mobilu použij plnou obrazovku pro nejlepší zážitek. Všechny kroky jsou testovány na GoPro Hero 13 + DJI Mic 3.")

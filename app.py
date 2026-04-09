import streamlit as st

st.set_page_config(
    page_title="GoPro Asistent",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded"   # <-- důležité pro desktop
)

# ==================== MODERNÍ DESKTOP-FIRST CSS ====================
pozadi_url = "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=2000&auto=format&fit=crop"

st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(5, 8, 18, 0.97), rgba(5, 8, 18, 0.94)), url("{pozadi_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Sidebar - vždy viditelná na desktopu */
    .css-1d391kg {{  /* sidebar container */
        background: rgba(255,255,255,0.06) !important;
        border-right: 1px solid rgba(0,174,239,0.2);
    }}

    /* Header */
    .main-header {{
        text-align: center;
        padding: 2.5rem 0 1.5rem 0;
    }}
    .main-header h1 {{
        font-size: 3.4rem;
        color: #00AEEF;
        font-weight: 800;
        letter-spacing: -0.04em;
        margin: 0;
    }}
    .main-header p {{
        font-size: 1.35rem;
        color: #AAAAAA;
        margin-top: 0.6rem;
    }}

    /* Segmented controls - velké, desktopové */
    .segment-container {{
        display: flex;
        justify-content: center;
        gap: 16px;
        margin: 1.8rem 0 3rem 0;
    }}
    .segment-btn {{
        background: rgba(255,255,255,0.08);
        color: #CCCCCC;
        border: 1px solid rgba(0,174,239,0.35);
        padding: 18px 36px;
        border-radius: 60px;
        font-size: 1.15rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.4s ease;
        min-width: 260px;
        text-align: center;
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }}
    .segment-btn:hover {{
        background: rgba(0,174,239,0.18);
        border-color: #00AEEF;
        color: white;
        transform: translateY(-4px);
    }}
    .segment-btn.active {{
        background: #00AEEF;
        color: #000000;
        font-weight: 700;
        box-shadow: 0 0 30px rgba(0,174,239,0.55);
    }}

    /* Hlavní obsahové karty */
    .content-card {{
        background: rgba(255,255,255,0.085);
        backdrop-filter: blur(22px);
        border: 1px solid rgba(0,174,239,0.3);
        border-radius: 24px;
        padding: 2.8rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.5);
    }}

    h2 {{ color: #00AEEF !important; font-size: 2rem; }}
    p, li {{ color: #F1F1F1; font-size: 1.15rem; line-height: 1.75; }}

    /* Manuálové karty v sidebaru */
    .manual-card {{
        background: rgba(255,255,255,0.07);
        border: 1px solid rgba(0,174,239,0.35);
        border-radius: 16px;
        padding: 1.4rem;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        transition: 0.3s;
    }}
    .manual-card:hover {{
        background: rgba(0,174,239,0.15);
        transform: translateX(6px);
    }}
</style>
""", unsafe_allow_html=True)

# ==================== HLAVIČKA ====================
st.markdown('<div class="main-header"><h1>📹 GoPro Asistent</h1><p>Praktický desktop průvodce propojením GoPro Hero 13 + DJI Mic 3</p></div>', unsafe_allow_html=True)

# ==================== VÝBĚR SCÉNÁŘE (velké desktopové tlačítka) ====================
selected = st.radio(
    label="Vyber typ propojení",
    options=["🔵 Přímé Bluetooth – jeden mikrofon", 
             "📡 Media Mod + bezdrátový přijímač", 
             "⚡ Rychlý obrázkový tahák"],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown(f"""
<div class="segment-container">
    <div class="segment-btn {'active' if 'Bluetooth' in selected else ''}">🔵 Přímé Bluetooth</div>
    <div class="segment-btn {'active' if 'Media Mod' in selected else ''}">📡 Media Mod + přijímač</div>
    <div class="segment-btn {'active' if 'tahák' in selected else ''}">⚡ Rychlý tahák</div>
</div>
""", unsafe_allow_html=True)

# ==================== HLAVNÍ OBSAH ====================
st.markdown('<div class="content-card">', unsafe_allow_html=True)

if "Bluetooth" in selected:
    st.header("🔵 Postup pro přímé Bluetooth spojení")
    col_v, col_t = st.columns([2, 1])
    with col_v:
        st.video("https://www.youtube.com/watch?v=LXb3EKWsInQ")
    with col_t:
        st.markdown("""
        ### Příprava mikrofonu
        1. Vyjmi mikrofon z dokovací stanice DJI.  
        2. Zkontroluj napájení (bliká zeleně).
        
        ### Nastavení kamery
        3. Zapni kameru (tlačítko MODE).  
        4. Přejeď prstem dolů → doleva → **Pair device**.
        
        ### Párování
        5. Podrž **Link** na mikrofonu.  
        6. Vyber **DJI Mic 3 TX** na GoPro.
        """)

elif "Media Mod" in selected:
    st.header("📡 Propojení kamery s Media Modem a přijímačem RX")
    col_v, col_t = st.columns([2, 1])
    with col_v:
        st.markdown("""
        <iframe src="https://legogroup-my.sharepoint.com/personal/jan_drvota_lego_com/_layouts/15/embed.aspx?UniqueId=061cd250-a744-4be2-8bd8-d404aed6f8d8&embed=%7B%22ust%22%3Atrue%2C%22hv%22%3A%22CopyEmbedCode%22%7D&referrer=StreamWebApp&referrerScenario=EmbedDialog.Create" 
                width="100%" height="460" frameborder="0" scrolling="no" allowfullscreen></iframe>
        """, unsafe_allow_html=True)
    with col_t:
        st.markdown("""
        ### Instalace Media Modu
        1. Odstraň dvířka kamery.  
        2. Vlož kameru do Media Modu.  
        3. Zavři kryt.
        
        ### Příprava + propojení
        4. Vyjmi přijímač.  
        5. Nasuň ho na Media Mod.  
        6. Zapoj kabel (OUT → kamera).
        """)

else:
    st.header("⚡ Rychlý obrázkový tahák")
    raw_image_url = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro%20propojen%C3%AD.png"
    st.image(raw_image_url, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# ==================== SIDEBAR (vždy viditelný na desktopu) ====================
with st.sidebar:
    st.header("💡 Tipy & Manuály")
    
    st.subheader("🎥 Doporučená videa")
    st.markdown("- [Uchycení GoPro na rám](https://www.youtube.com/watch?v=LXb3EKWsInQ)\n- [Expozice v hale](https://www.youtube.com/watch?v=LXb3EKWsInQ)")
    
    st.subheader("📚 Oficiální manuály")
    url_gopro = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro13%20manual.pdf"
    url_dji = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/DJI_Mic_3_User_Manual_CS%20(1).pdf"
    
    st.markdown(f"""
    <a href="{url_gopro}" target="_blank" style="text-decoration:none;">
        <div class="manual-card"><span style="font-size:2rem;margin-right:12px;">📘</span><span>GoPro Hero 13</span></div>
    </a>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <a href="{url_dji}" target="_blank" style="text-decoration:none;">
        <div class="manual-card"><span style="font-size:2rem;margin-right:12px;">📘</span><span>DJI Mic 3</span></div>
    </a>
    """, unsafe_allow_html=True)
    
    st.caption("Optimalizováno pro velké obrazovky • Mobilní verze je podpůrná")

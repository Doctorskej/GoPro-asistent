import streamlit as st

st.set_page_config(
    page_title="GoPro Asistent",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==================== CSS - opravené tlačítka + tmavší sidebar ====================
pozadi_url = "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=2000&auto=format&fit=crop"

st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(5, 8, 18, 0.97), rgba(5, 8, 18, 0.94)), url("{pozadi_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Tmavší a elegantnější sidebar */
    section[data-testid="stSidebar"] {{
        background: rgba(10, 12, 22, 0.95) !important;
        border-right: 1px solid rgba(0, 174, 239, 0.15);
    }}
    .stSidebar .stMarkdown h1, .stSidebar .stMarkdown h2, .stSidebar .stMarkdown h3 {{
        color: #00AEEF !important;
    }}

    /* Velká desktopová tlačítka (fungující výběr bez červené) */
    .segment-container {{
        display: flex;
        justify-content: center;
        gap: 18px;
        margin: 2rem 0 3rem 0;
        flex-wrap: wrap;
    }}
    .segment-btn {{
        background: rgba(255,255,255,0.07);
        color: #CCCCCC;
        border: 1px solid rgba(0,174,239,0.4);
        padding: 18px 40px;
        border-radius: 60px;
        font-size: 1.18rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.35s ease;
        min-width: 280px;
        text-align: center;
        box-shadow: 0 8px 25px rgba(0,0,0,0.35);
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
        border: 2px solid #00AEEF;
        font-weight: 700;
        box-shadow: 0 0 35px rgba(0,174,239,0.6);
    }}

    /* Hlavní obsah */
    .content-card {{
        background: rgba(255,255,255,0.085);
        backdrop-filter: blur(20px);
        border: 1px solid rgba(0,174,239,0.3);
        border-radius: 24px;
        padding: 2.8rem;
        box-shadow: 0 20px 60px rgba(0,0,0,0.5);
    }}

    h1, h2 {{ color: #00AEEF !important; }}
    p, li {{ color: #F0F0F0; font-size: 1.15rem; line-height: 1.75; }}
</style>
""", unsafe_allow_html=True)

# ==================== HLAVIČKA ====================
st.markdown("""
    <div style="text-align:center; padding: 2rem 0 1rem 0;">
        <h1 style="font-size:3.5rem; margin:0;">📹 GoPro Asistent</h1>
        <p style="font-size:1.35rem; color:#AAAAAA; margin-top:0.6rem;">
            Praktický desktop průvodce propojením GoPro Hero 13 + DJI Mic 3
        </p>
    </div>
""", unsafe_allow_html=True)

# ==================== VÝBĚR (fungující tlačítka) ====================
option = st.radio(
    "Vyber typ propojení",
    ["🔵 Přímé Bluetooth – jeden mikrofon",
     "📡 Media Mod + bezdrátový přijímač",
     "⚡ Rychlý obrázkový tahák"],
    horizontal=True,
    label_visibility="collapsed"
)

st.markdown(f"""
<div class="segment-container">
    <div class="segment-btn {'active' if 'Bluetooth' in option else ''}">🔵 Přímé Bluetooth</div>
    <div class="segment-btn {'active' if 'Media Mod' in option else ''}">📡 Media Mod + přijímač</div>
    <div class="segment-btn {'active' if 'tahák' in option else ''}">⚡ Rychlý tahák</div>
</div>
""", unsafe_allow_html=True)

# ==================== HLAVNÍ OBSAH ====================
st.markdown('<div class="content-card">', unsafe_allow_html=True)

if "Bluetooth" in option:
    st.header("🔵 Postup pro přímé Bluetooth spojení")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.video("https://www.youtube.com/watch?v=LXb3EKWsInQ")
    with col2:
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

elif "Media Mod" in option:
    st.header("📡 Propojení kamery s Media Modem a přijímačem RX")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        <iframe src="https://legogroup-my.sharepoint.com/personal/jan_drvota_lego_com/_layouts/15/embed.aspx?UniqueId=061cd250-a744-4be2-8bd8-d404aed6f8d8&embed=%7B%22ust%22%3Atrue%2C%22hv%22%3A%22CopyEmbedCode%22%7D&referrer=StreamWebApp&referrerScenario=EmbedDialog.Create" 
                width="100%" height="460" frameborder="0" scrolling="no" allowfullscreen></iframe>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        ### Instalace Media Modu
        1. Odstraň dvířka kamery.  
        2. Vlož kameru do Media Modu.  
        3. Zavři kryt.
        
        ### Příprava a propojení
        4. Vyjmi přijímač z pouzdra.  
        5. Nasuň přijímač na Media Mod.  
        6. Zapoj kabel do přijímače (OUT) a do kamery.
        """)

else:
    st.header("⚡ Rychlý obrázkový tahák")
    raw_image_url = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro%20propojen%C3%AD.png"
    st.image(raw_image_url, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# ==================== SIDEBAR (tmavší a přehledný) ====================
with st.sidebar:
    st.header("💡 Tipy a manuály")
    
    st.subheader("🎥 Užitečné videonávody")
    st.markdown("""
    - [Uchycení GoPro na rám stroje](https://www.youtube.com/watch?v=LXb3EKWsInQ)  
    - [Nastavení expozice v temné hale](https://www.youtube.com/watch?v=LXb3EKWsInQ)
    """)
    
    st.subheader("📚 Oficiální manuály")
    url_gopro = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro13%20manual.pdf"
    url_dji = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/DJI_Mic_3_User_Manual_CS%20(1).pdf"
    
    st.markdown(f"""
    <a href="{url_gopro}" target="_blank" style="text-decoration:none;">
        <div style="background:rgba(255,255,255,0.08); padding:1.2rem; border-radius:14px; margin-bottom:12px; display:flex; align-items:center;">
            <span style="font-size:2.2rem; margin-right:14px;">📘</span>
            <span style="font-size:1.1rem; font-weight:600;">GoPro Hero 13</span>
        </div>
    </a>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <a href="{url_dji}" target="_blank" style="text-decoration:none;">
        <div style="background:rgba(255,255,255,0.08); padding:1.2rem; border-radius:14px; margin-bottom:12px; display:flex; align-items:center;">
            <span style="font-size:2.2rem; margin-right:14px;">📘</span>
            <span style="font-size:1.1rem; font-weight:600;">DJI Mic 3</span>
        </div>
    </a>
    """, unsafe_allow_html=True)
    
    st.caption("Optimalizováno pro velké obrazovky • Desktop-first")

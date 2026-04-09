import streamlit as st

st.set_page_config(
    page_title="GoPro Asistent",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== MODERNÍ CSS (bez červeného podtržení) ====================
pozadi_url = "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=2000&auto=format&fit=crop"

st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(8, 12, 22, 0.94), rgba(8, 12, 22, 0.90)), url("{pozadi_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* Segmented control - moderní tlačítka místo tabs */
    .segment-container {{
        display: flex;
        justify-content: center;
        gap: 12px;
        margin: 2rem 0 2.5rem 0;
        flex-wrap: wrap;
    }}
    .segment-btn {{
        background: rgba(255, 255, 255, 0.08);
        color: #CCCCCC;
        border: 1px solid rgba(0, 174, 239, 0.3);
        padding: 14px 28px;
        border-radius: 50px;
        font-weight: 600;
        font-size: 1.05rem;
        cursor: pointer;
        transition: all 0.3s ease;
        display: flex;
        align-items: center;
        gap: 10px;
        white-space: nowrap;
    }}
    .segment-btn:hover {{
        background: rgba(0, 174, 239, 0.15);
        border-color: #00AEEF;
        color: white;
        transform: translateY(-2px);
    }}
    .segment-btn.active {{
        background: rgba(0, 174, 239, 0.25);
        border: 2px solid #00AEEF;
        color: #FFFFFF;
        box-shadow: 0 0 20px rgba(0, 174, 239, 0.35);
    }}

    .glass-card {{
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(16px);
        border: 1px solid rgba(0, 174, 239, 0.25);
        border-radius: 20px;
        padding: 2rem;
        box-shadow: 0 10px 40px rgba(0, 0, 0, 0.35);
    }}

    h1 {{
        color: #00AEEF !important;
        font-weight: 800;
        letter-spacing: -0.03em;
        margin-bottom: 0.3rem;
    }}
    h2 {{
        color: #FFFFFF !important;
        font-weight: 700;
    }}

    .manual-card {{
        background: rgba(255, 255, 255, 0.07);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(0, 174, 239, 0.3);
        border-radius: 16px;
        padding: 1.4rem 1.6rem;
        margin-bottom: 14px;
        display: flex;
        align-items: center;
        transition: all 0.3s ease;
    }}
    .manual-card:hover {{
        background: rgba(0, 174, 239, 0.15);
        border-color: #00AEEF;
        transform: translateY(-3px);
    }}
    .manual-card-icon {{
        font-size: 2.1rem;
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
        box-shadow: 0 12px 35px rgba(0, 0, 0, 0.5);
    }}
</style>
""", unsafe_allow_html=True)

# ==================== HLAVIČKA ====================
st.markdown("""
    <div style="text-align: center; margin-bottom: 1rem;">
        <h1 style="font-size: 3.2rem; margin-bottom: 0;">📹 GoPro Asistent</h1>
        <p style="font-size: 1.25rem; color: #AAAAAA; margin-top: 0.5rem;">
            Praktický průvodce propojením GoPro Hero 13 + DJI Mic 3
        </p>
    </div>
""", unsafe_allow_html=True)

# ==================== SEGMENTOVANÉ TLAČÍTKO (nahrazuje tabs) ====================
option = st.radio(
    label="Vyber typ propojení",
    options=[
        "🔵 Přímé Bluetooth – jeden mikrofon",
        "📡 Media Mod + bezdrátový přijímač",
        "⚡ Rychlý obrázkový tahák"
    ],
    horizontal=True,
    label_visibility="collapsed"
)

# Převod na aktivní třídu pro CSS
active_class = "active"

st.markdown(f"""
<div class="segment-container">
    <div class="segment-btn {'active' if option == '🔵 Přímé Bluetooth – jeden mikrofon' else ''}">🔵 Přímé Bluetooth</div>
    <div class="segment-btn {'active' if option == '📡 Media Mod + bezdrátový přijímač' else ''}">📡 Media Mod + přijímač</div>
    <div class="segment-btn {'active' if option == '⚡ Rychlý obrázkový tahák' else ''}">⚡ Rychlý tahák</div>
</div>
""", unsafe_allow_html=True)

# ==================== HLAVNÍ OBSAH PODLE VÝBĚRU ====================
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

if option == "🔵 Přímé Bluetooth – jeden mikrofon":
    st.header("🔵 Postup pro přímé Bluetooth spojení")
    col1, col2 = st.columns([1.65, 1])
    with col1:
        st.subheader("🎥 Videonávod")
        st.video("https://www.youtube.com/watch?v=LXb3EKWsInQ")
    with col2:
        st.markdown("""
        ### Příprava mikrofonu
        1. Vyjmi mikrofon z dokovací stanice DJI.
        2. Zkontroluj napájení – zapnutý bliká zeleně.
        
        ### Nastavení kamery
        3. Zapni kameru (tlačítko MODE).
        4. Přejeď prstem dolů → doleva.
        5. Stiskni „Pair device“.
        
        ### Párování
        6. Na mikrofonu podrž tlačítko **Link**.
        7. Na GoPro klikni na **DJI Mic 3 TX**.
        """)

elif option == "📡 Media Mod + bezdrátový přijímač":
    st.header("📡 Propojení kamery s Media Modem a přijímačem RX")
    col1, col2 = st.columns([1.65, 1])
    with col1:
        st.subheader("🎥 Videonávod")
        st.markdown("""
        <iframe src="https://legogroup-my.sharepoint.com/personal/jan_drvota_lego_com/_layouts/15/embed.aspx?UniqueId=061cd250-a744-4be2-8bd8-d404aed6f8d8&embed=%7B%22ust%22%3Atrue%2C%22hv%22%3A%22CopyEmbedCode%22%7D&referrer=StreamWebApp&referrerScenario=EmbedDialog.Create" 
                width="100%" height="400" frameborder="0" scrolling="no" allowfullscreen></iframe>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        ### Instalace Media Modu
        1. Odstraň dvířka kamery.
        2. Vlož kameru do Media Modu.
        3. Zavři Media Mod.
        
        ### Příprava přijímače
        4. Vyjmi přijímač z pouzdra.
        5. Potvrď zprávu na displeji.
        
        ### Propojení
        6. Nasuň přijímač na Media Mod.
        7. Zapoj kabel do přijímače (OUT) a do kamery.
        """)

else:  # Rychlý tahák
    st.header("⚡ Rychlý obrázkový tahák")
    st.markdown("Kliknutím na obrázek si ho můžeš zvětšit.")
    raw_image_url = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro%20propojen%C3%AD.png"
    st.image(raw_image_url, use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

# ==================== TIPS SEKCE ====================
st.divider()

col_a, col_b = st.columns([3, 2])

with col_b:
    st.subheader("💡 Tipy a triky")
    
    st.markdown("**🎥 Užitečné videonávody**")
    st.markdown("""
    • [Uchycení GoPro na rám stroje](https://www.youtube.com/watch?v=LXb3EKWsInQ)  
    • [Nastavení expozice v temné hale](https://www.youtube.com/watch?v=LXb3EKWsInQ)
    """)
    
    st.subheader("📚 Manuály")
    url_gopro = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro13%20manual.pdf"
    url_dji = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/DJI_Mic_3_User_Manual_CS%20(1).pdf"
    
    st.markdown(f"""
    <a href="{url_gopro}" target="_blank" style="text-decoration:none;">
        <div class="manual-card">
            <span class="manual-card-icon">📘</span>
            <span class="manual-card-text">Manuál GoPro Hero 13</span>
        </div>
    </a>
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <a href="{url_dji}" target="_blank" style="text-decoration:none;">
        <div class="manual-card">
            <span class="manual-card-icon">📘</span>
            <span class="manual-card-text">Manuál DJI Mic 3</span>
        </div>
    </a>
    """, unsafe_allow_html=True)

with col_a:
    st.info("**Tip pro terén:** Nejlepší je používat appku na mobilu v režimu na výšku. Všechny postupy jsou ověřené na GoPro Hero 13 + DJI Mic 3 (2026).")

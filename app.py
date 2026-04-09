import streamlit as st

st.set_page_config(
    page_title="GoPro Asistent",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== CSS - KONTRAST A STABILNÍ BARVY ====================
pozadi_url = "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=2000&auto=format&fit=crop"

st.markdown(f"""
<style>
    /* 1. CELKOVÉ POZADÍ */
    .stApp {{
        background-image: linear-gradient(rgba(8, 12, 22, 0.75), rgba(8, 12, 22, 0.7)), url("{pozadi_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    /* 2. ZÁLOŽKY (TABS) */
    .stTabs [data-baseweb="tab-highlight"] {{ background-color: transparent !important; height: 0 !important; }}
    .stTabs [data-baseweb="tab-border"] {{ display: none !important; }}
    .stTabs [data-baseweb="tab-list"] {{ gap: 14px; padding-bottom: 15px; }}
    .stTabs [data-baseweb="tab"] {{
        background: rgba(255, 255, 255, 0.1);
        border-radius: 14px;
        padding: 15px 26px;
        font-size: 1.1rem;
        font-weight: 600;
        color: #FFFFFF;
        border: 1px solid rgba(0, 174, 239, 0.4);
    }}
    .stTabs [data-baseweb="tab"][aria-selected="true"] {{
        background: rgba(0, 174, 239, 0.4) !important;
        border: 2px solid #00AEEF !important;
    }}

    /* 3. HLAVNÍ KARTY */
    .glass-card {{
        background: rgba(0, 0, 0, 0.65) !important;
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 18px;
        padding: 2.5rem;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.6);
    }}

    /* 4. VIDITELNOST TEXTU - Bílá + stín */
    p, li, [data-testid="stMarkdownContainer"] p, [data-testid="stMarkdownContainer"] li {{
        color: #FFFFFF !important;
        font-weight: 500 !important;
        text-shadow: 1px 1px 3px rgba(0,0,0,0.8) !important;
        line-height: 1.6;
    }}

    h1, h2, h3 {{ 
        color: #00AEEF !important; 
        font-weight: 800; 
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5) !important;
    }}

    /* 5. EXPANDÉRY - Fix barev proti problikávání */
    div[data-testid="stExpander"] {{
        background-color: rgba(255, 255, 255, 0.05) !important;
        border: 1px solid rgba(0, 174, 239, 0.5) !important;
        border-radius: 14px !important;
    }}
    div[data-testid="stExpander"] summary {{
        background-color: transparent !important;
        color: #FFFFFF !important;
    }}
    div[data-testid="stExpander"] summary:hover {{
        background-color: rgba(0, 174, 239, 0.15) !important;
        color: #00AEEF !important;
    }}
    div[data-testid="stExpander"] [data-testid="stExpanderDetails"] {{
        background-color: rgba(0, 0, 0, 0.3) !important;
    }}

    /* MANUÁLOVÉ KARTY */
    .manual-card {{
        background: rgba(0, 174, 239, 0.2);
        border: 1px solid #00AEEF;
        border-radius: 16px;
        padding: 1.5rem;
        margin-bottom: 12px;
        display: flex;
        align-items: center;
        transition: 0.3s ease;
    }}
    .manual-card:hover {{ background: rgba(0, 174, 239, 0.35); transform: translateY(-2px); }}
    
    img, iframe, video {{ border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }}
</style>
""", unsafe_allow_html=True)

# ==================== OBSAH ====================
st.title("📹 GoPro Asistent")
st.markdown("**Průvodce pro Hero 13 + DJI Mic 3 v průmyslovém provozu**")

tab1, tab2, tab3 = st.tabs(["🔵 Bluetooth", "📡 Media Mod", "⚡ Tahák"])

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
        3. **V menu:** Swipe dolů -> Swipe doleva.
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
    
    # TVŮJ DETAILNÍ TEXT VLOŽEN SEM:
    with st.expander("📸 Doporučené průmyslové profily (GoPro Hero 13)"):
        st.markdown("""
        **1. Celkové záběry linky / pracoviště** Vhodné pro analýzu toku materiálu, pohybu operátorů nebo prostorové uspořádání.
        * **Rozlišení:** 4K (ideální poměr kvality a velikosti souboru pro firemní síť).
        * **Snímková frekvence (FPS):** 30 (plynulý, přirozený obraz).
        * **Čočka (Lens):** Wide (Široká) – aby bylo vidět celé zařízení i okolní prostor.
        * **Stabilizace (Hypersmooth):** AutoBoost (vynikající pro natáčení za chůze podél linky).
        * **Barvy:** Natural (věrné podání barev pro identifikaci komponent).

        **2. Technický detail a údržba (Makro)** Klíčové pro natáčení servisních úkonů, zapojování konektorů nebo čtení štítků.
        * **Rozlišení:** 4K.
        * **FPS:** 30.
        * **Čočka (Lens):** Linear (Lineární) – **Zcela zásadní!** Odstraní zkreslení "rybího oka". Hrany strojů a nosníky budou rovné, což usnadňuje orientaci v prostoru.
        * **Horizon Lock:** Zapnuto. I když se s kamerou nakloníš do útrob stroje, obraz zůstane vodorovně.
        * **Barvy:** Vibrant (Zvýrazní barevné kódování kabelů, diody a bezpečnostní prvky).

        **3. Inspekce v temných prostorech** Uvnitř strojních skříní, pod dopravníky nebo v revizních šachtách.
        * **FPS:** 24 (nižší frekvence dovolí čipu "nasát" více světla z LED svítilen).
        * **ISO Max:** 1600 (vyšší hodnota zajistí viditelnost v šeru, ale s minimálním zrněním).
        * **Ostrost (Sharpness):** Medium (při slabém světle vypadá obraz přirozeněji).
        * **Stabilizace:** Standard (v šeru vysoká stabilizace způsobuje rozmazání pohybu, tzv. "duchy").
        """)

    with st.expander("🛠️ Řešení problémů"):
        st.markdown("""
        * **Bluetooth:** Vypni Bluetooth v mobilu (mikrofon se často 'přilepí' k němu).
        * **Bez zvuku:** Zkontroluj, jestli kamera v Modu sedí úplně nadoraz.
        * **Limit zvuku:** Pokud indikátor hlasitosti na displeji dosahuje červených hodnot, v menu přijímače snižte zesílení (**Gain**) na -6 nebo -12 dB.
        """)

    st.subheader("📚 Manuály")
    u_g = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro13%20manual.pdf"
    u_d = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/DJI_Mic_3_User_Manual_CS%20(1).pdf"
    st.markdown(f'<a href="{u_g}" target="_blank" style="text-decoration:none;"><div class="manual-card">📘 Manuál GoPro Hero 13</div></a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{u_d}" target="_blank" style="text-decoration:none;"><div class="manual-card">📘 Manuál DJI Mic 3</div></a>', unsafe_allow_html=True)

with col_left:
    st.info("Tip: Čočka **LINEAR** je nejlepší pro technickou dokumentaci – nedeformuje obraz stroje.")
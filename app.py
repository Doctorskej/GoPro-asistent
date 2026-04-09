import streamlit as st

st.set_page_config(
    page_title="GoPro Asistent",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== CSS - OPRAVA KONTRASTU A VIDITELNOSTI ====================
pozadi_url = "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=2000&auto=format&fit=crop"

st.markdown(f"""
<style>
    .stApp {{
        background-image: linear-gradient(rgba(8, 12, 22, 0.9), rgba(8, 12, 22, 0.85)), url("{pozadi_url}");
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

    /* KOMPLETNÍ OPRAVA EXPANDERŮ - Bílý podklad, černý text pro max. čitelnost */
    div[data-testid="stExpander"] {{
        background-color: #FFFFFF !important;
        border-radius: 14px !important;
        border: 2px solid #00AEEF !important;
        margin-bottom: 12px;
    }}
    
    /* Vynucení černé barvy pro text uvnitř expanderu */
    div[data-testid="stExpander"] p, 
    div[data-testid="stExpander"] li,
    div[data-testid="stExpander"] span,
    div[data-testid="stExpander"] label,
    div[data-testid="stExpander"] summary p {{
        color: #000000 !important;
        font-weight: 600 !important;
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
st.markdown("**Návod pro nahrávání údržby a technických instruktáží (Hero 13 + DJI Mic 3)**")

# ==================== TABS ====================
tab1, tab2, tab3 = st.tabs([
    "🔵 Přímé připojení Bluetooth (1 mikrofon)",
    "📡 Připojení přes Media Mod a kabel",
    "⚡ Rychlý obrázkový tahák"
])

with tab1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("🔵 Přímé připojení jednoho mikrofonu")
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
        1. **Vyjmi mikrofon** z pouzdra a ověř, že svítí zeleně.
        2. **Zapni kameru** (tlačítko **MODE**).
        3. **Menu:** Přejeď prstem dolů -> doleva.
        4. **Párování:** Zvol **„Pair device“**.
        5. **Na mikrofonu:** 2x krátce zmáčkni tlačítko (modré blikání).
        6. **Na mikrofonu:** Podrž tlačítko na 3s (modro-zelené blikání).
        7. **Na kameře:** Klikni na nalezený **DJI Mic 3 TX**.
        """)
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("📡 Připojení přes Media Mod a přijímač")
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
        1. **Kamera:** Sundej dvířka a zasuň kameru nadoraz do Media Modu.
        2. **Přijímač:** Vyndej z pouzdra a potvrď **Confirm**.
        3. **Uchycení:** Nasuň přijímač do sáněk na boku Media Modu.
        4. **Propojení:** Zapoj kabel do přijímače (**OUT**) a do kamery (**spodní jack**).
        5. **Kontrola:** Na displeji se musí objevit ikona mikrofonu.
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
    st.info("**Tip pro údržbu:** Pro technická videa vždy nastavte čočku **Linear**, aby linky strojů nebyly prohnuté.")

with col_r:
    st.header("💡 Tipy a řešení problémů")

    # NOVÉ STRUKTUROVANÉ NASTAVENÍ - Bílý podklad, Váš text
    with st.expander("📸 Doporučené průmyslové profily"):
        st.markdown("""
        **1. Celkové záběry linky / pracoviště** *Vhodné pro analýzu toku materiálu, pohybu operátorů nebo prostorové uspořádání.* * **Rozlišení:** 4K (ideální pro firemní síť).  
        * **FPS:** 30 (plynulý obraz).  
        * **Čočka (Lens):** Wide (Široká).  
        * **Stabilizace:** AutoBoost.  
        * **Barvy:** Natural (věrné podání).  

        **2. Technický detail a údržba (Makro)** *Klíčové pro servisní úkony, zapojování konektorů nebo čtení štítků.* * **Rozlišení:** 4K / **FPS:** 30.  
        * **Čočka (Lens):** **Linear (Lineární)** – Zcela zásadní! Odstraní zkreslení. Hrany strojů budou rovné.  
        * **Horizon Lock:** Zapnuto (obraz zůstane vodorovně).  
        * **Barvy:** Vibrant (zvýrazní kabely a diody).  

        **3. Inspekce v temných prostorech** *Uvnitř strojních skříní, pod dopravníky nebo v šachtách.* * **FPS:** 24 (více světla pro čip).  
        * **ISO Max:** 1600 (viditelnost v šeru).  
        * **Ostrost:** Medium.  
        * **Stabilizace:** Standard (v šeru brání duchům v obraze).
        """)

    with st.expander("🛠️ Řešení problémů (Troubleshooting)"):
        st.subheader("🔵 Bluetooth připojení")
        st.markdown("""
        * **Kamera nevidí mikrofon:** Pravděpodobně je mikrofon připojený k tvému mobilu. Vypni Bluetooth v mobilu a zkus to znovu.
        * **Zvuk vypadává:** Mezi kamerou a mikrofonem nesmí být kovová stěna stroje. Bluetooth přes kov neprojde.
        """)
        st.subheader("📡 Připojení přes kabel a Media Mod")
        st.markdown("""
        * **Není slyšet zvuk:** Zkontroluj, jestli je kamera v Media Modu doražená až nadoraz na konektor. Musí tam pevně sedět.
        * **Lupání ve zvuku:** Dotlač propojovací kabel v přijímači i v kameře. Musí to slyšitelně cvaknout.
        * **Příliš hlasitý zvuk:** Pokud indikátor hlasitosti dosahuje červených hodnot, upravte v menu přijímače úroveň zisku (Gain) na -6 dB nebo -12 dB.
        """)

    st.subheader("📚 Manuály")
    url_gopro = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro13%20manual.pdf"
    url_dji = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/DJI_Mic_3_User_Manual_CS%20(1).pdf"
    st.markdown(f'<a href="{url_gopro}" target="_blank" style="text-decoration:none;"><div class="manual-card"><span class="manual-card-icon">📘</span><span class="manual-card-text">Manuál GoPro Hero 13</span></div></a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{url_dji}" target="_blank" style="text-decoration:none;"><div class="manual-card"><span class="manual-card-icon">📘</span><span class="manual-card-text">Manuál DJI Mic 3</span></div></a>', unsafe_allow_html=True)
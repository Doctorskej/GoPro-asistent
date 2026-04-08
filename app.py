import streamlit as st

# 1. NASTAVENÍ STRÁNKY (Unified material icon)
st.set_page_config(page_title="GoPro Asistent", page_icon=":material/videocam:", layout="wide")

# 2. VLASTNÍ MODERNÍ DESIGN (Keeping background image, simplifying CSS)
pozadi_url = "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=2000&auto=format&fit=crop"

st.markdown(f"""
<style>
/* Gradient přes fotku pro 100% čitelnost */
.stApp {{
    background-image: linear-gradient(rgba(15, 15, 15, 0.85), rgba(15, 15, 15, 0.85)), url("{pozadi_url}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

.block-container {{
    padding: 3rem;
}}

/* Vizuální hierarchie nadpisů */
h1, h2 {{
    color: #00AEEF !important;
    font-weight: 800 !important;
}}

/* Podnadpisy */
h3 {{
    color: #FFFFFF !important;
    font-weight: 700 !important;
    font-size: 1.3rem !important;
    margin-top: 1.5rem !important;
    padding-bottom: 0.3rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.15);
}}

/* Obecný text */
p, label {{
    color: #FFFFFF !important;
    font-size: 1.1rem;
    font-weight: 500;
}}

/* Provzdušnění odrážek */
li {{
    color: #FFFFFF !important;
    font-size: 1.1rem;
    font-weight: 500;
    margin-bottom: 0.8rem;
    line-height: 1.5;
}}

/* Odkazy (Zůstává beze změny z verze 1.0) */
a {{
    color: #FFFFFF !important;
    text-decoration: none !important;
    border-bottom: 2px solid #00AEEF;
    font-weight: 600;
    transition: all 0.3s ease;
}}
a:hover {{
    color: #00AEEF !important;
    border-bottom: 2px solid #FFFFFF;
}}

/* Videa, iFramy, img */
div[data-testid="stVideo"], iframe, img {{
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
    width: 100% !important;
}}

/* Vytvoření čitelných tlačítek-karet pro manuály */
.manual-card {{
    background-color: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(0, 174, 239, 0.3);
    padding: 1rem;
    border-radius: 10px;
    margin-bottom: 0.8rem;
    display: flex;
    align-items: center;
    cursor: pointer;
    transition: all 0.3s ease;
    width: 100%;
    text-align: left;
    outline: none;
}}
.manual-card:hover {{
    background-color: rgba(0, 174, 239, 0.1) !important;
    border: 1px solid #FFFFFF !important;
}}
.manual-card-icon {{
    font-size: 1.5rem;
    margin-right: 10px;
    color: #FFFFFF;
}}
.manual-card-text {{
    color: #FFFFFF !important;
    font-size: 1.1rem;
    font-weight: 500;
}}
</style>
""", unsafe_allow_html=True)

# --- HLAVNÍ OBSAH ---

st.title(":material/videocam: GoPro Asistent")
st.write("Vyber si typ připojení:")

levy_sloupec, pravy_sloupec = st.columns([3, 2], gap="large")

with levy_sloupec:
    # NOVÉ: Záložky místo radio buttonů, video nahoře, text dole
    scenar_tab1, scenar_tab2, scenar_tab3 = st.tabs([
        "1. Připojení JEDNOHO mikrofonu (Napřímo přes Bluetooth)",
        "2. Připojení BEZDRÁTOVÉHO PŘIJÍMAČE (Celý DJI set s kabelem)",
        "3. Fast manual propojení (Rychlý obrázkový tahák)"
    ])

    with scenar_tab1:
        st.header("🔵 Postup pro přímé Bluetooth spojení")
        
        # Stack video full-width then text
        st.write("**Videonávod:**")
        st.video("https://www.youtube.com/watch?v=LXb3EKWsInQ")
        st.markdown("*Ideální pro maximální minimalismus.*")

        st.markdown("""
        ### Příprava mikrofonu
        1. **Vyjmi mikrofon** z dokovací stanice DJI.
        2. **Zkontroluj napájení:** Zapnutý = bliká zelené tlačítko.
           * *Tip: Pokud nesvítí, zapni ho podržením červeného tlačítka.*

        ### Nastavení kamery
        3. **Zapni kameru** (tlačítko `MODE`).
        4. **Přejeď prstem dolů** a pak **doleva**.
        5. Stiskni **„Pair device“**.

        ### Samotné párování
        6. Na mikrofonu **podrž tlačítko Link** (bliká modro-zeleně).
        7. Na displeji kamery klikni na **DJI Mic 3 TX**.
        """)

    with scenar_tab2:
        st.header("📡 Propojení kamery s Media Modem a přijímačem RX")
        
        # Stack video full-width then text
        st.write("**Videonávod:**")
        st.markdown("""
        <iframe src="https://legogroup-my.sharepoint.com/personal/jan_drvota_lego_com/_layouts/15/embed.aspx?UniqueId=061cd250-a744-4be2-8bd8-d404aed6f8d8&embed=%7B%22ust%22%3Atrue%2C%22hv%22%3A%22CopyEmbedCode%22%7D&referrer=StreamWebApp&referrerScenario=EmbedDialog.Create" width="100%" height="360" frameborder="0" scrolling="no" allowfullscreen title="GoPro přijímač.mp4"></iframe>
        """, unsafe_allow_html=True)

        st.markdown("""
        ### Instalace Media Modu
        1. **Odstraň dvířka** kamery.
        2. **Otevři Media Mod**.
        3. **Vlož kameru** do Media Modu.
        4. **Zavři Media Mod**.

        ### Příprava DJI přijímače
        5. **Vyjmi přijímač** z pouzdra.
        6. **Potvrď informaci** na displeji (Confirm).
        
        ### Fyzické propojení
        7. **Nasuň přijímač** na Media Mod.
        8. **Zapoj kabel** do přijímače (OUT) a do kamery.
        """)
        
    with scenar_tab3:
        st.header("⚡ Fast manual propojení")
        st.markdown("*Rychlý přehled pro zapojení bez zbytečných řečí. Kliknutím na obrázek si ho můžeš zvětšit.*")
        
        raw_image_url = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro%20propojen%C3%AD.png"
        st.image(raw_image_url, use_container_width=True)

with pravy_sloupec:
    st.header("💡 Tipy a triky")
    st.markdown("""
    **🎥 Videonávody:**
    * [Jak správně uchytit GoPro na rám stroje](https://www.youtube.com/watch?v=LXb3EKWsInQ)
    * [Jak nastavit expozici v temné hale](https://www.youtube.com/watch?v=LXb3EKWsInQ)
    
    ---
    **📚 Manuály:**
    """)
    
    # Přímé RAW odkazy na GitHub
    url_gopro = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro13%20manual.pdf"
    url_dji = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/DJI_Mic_3_User_Manual_CS%20(1).pdf"
    
    # Unified Material Icon for manuals - using menu_book as suggested for opening
    st.markdown(f"""
    <a href="{url_gopro}" target="_blank" style="text-decoration: none; width: 100%;">
        <div class="manual-card">
            <span class="manual-card-icon">:material/menu_book:</span>
            <span class="manual-card-text">Otevřít manuál k GoPro 13 (v novém okně)</span>
        </div>
    </a>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <a href="{url_dji}" target="_blank" style="text-decoration: none; width: 100%;">
        <div class="manual-card">
            <span class="manual-card-icon">:material/menu_book:</span>
            <span class="manual-card-text">Otevřít manuál k DJI Mic 3 (v novém okně)</span>
        </div>
    </a>
    """, unsafe_allow_html=True)
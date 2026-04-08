import streamlit as st

# 1. NASTAVENÍ STRÁNKY (Nová cool ikona videokamery)
st.set_page_config(page_title="GoPro Asistent", page_icon=":material/videocam:", layout="wide")

# 2. VLASTNÍ MODERNÍ DESIGN (Zůstává beze změny z verze 1.0)
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

/* Podnadpisy menší a bílé */
h3 {{
    color: #FFFFFF !important;
    font-weight: 700 !important;
    font-size: 1.3rem !important;
    margin-top: 1.5rem !important;
    padding-bottom: 0.3rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.15);
}}

/* Obecný text */
p, label, div.stRadio > div {{
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

/* Větší mezery mezi přepínači */
div[role="radiogroup"] > label {{
    margin-bottom: 0.8rem !important;
}}

/* Bílé odkazy s modrým podtržením */
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

/* Videa */
div[data-testid="stVideo"] {{
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
}}
</style>
""", unsafe_allow_html=True)

# --- ZBYTEK TVÉ APLIKACE ---

st.title("🎬 GoPro & DJI Asistent")
st.write("Vyber si typ připojení zvuku, který jdeš zrovna zapojit, a já ti dám přesný návod.")

# Hlavní rozdělení (Levý pro návod, Pravý pro tipy)
levy_sloupec, pravy_sloupec = st.columns([3, 2], gap="large")

with levy_sloupec:
    scenar = st.radio(
        "Co máš dnes v plánu?",
        (
            "1. Připojení JEDNOHO mikrofonu (Napřímo přes Bluetooth)",
            "2. Připojení BEZDRÁTOVÉHO PŘIJÍMAČE (Celý DJI set s kabelem)",
            "3. Fast manual propojení (Rychlý obrázkový tahák)"
        )
    )

    if scenar == "1. Připojení JEDNOHO mikrofonu (Napřímo přes Bluetooth)":
        st.header("🔵 Postup pro přímé Bluetooth spojení")
        
        # Poměr sloupců upraven ve prospěch videa [1.5, 1]
        video_sl, text_sl = st.columns([1.5, 1], gap="medium")
        
        with video_sl:
            st.write("**Videonávod:**")
            st.video("https://www.youtube.com/watch?v=LXb3EKWsInQ")
            st.markdown("*Ideální pro maximální minimalismus.*")

        with text_sl:
            st.markdown("""
            ### Příprava mikrofonu
            1. **Vyjmi mikrofon** z dokovací stanice DJI.
            2. **Zkontroluj napájení:** Zapnutý = bliká zelené tlačítko.
               * *Tip: Pokud nesvítí, zapni ho podržením červeného tlačítka.*

            ### Nastavení kamery
            3. **Zapni kameru** (tlačítko `MODE`).
            4. Na displeji **přejeď prstem seshora dolů**.
            5. Následně **přejeď prstem doleva**.
            6. Stiskni možnost **„Pair device“**.

            ### Samotné párování
            7. Na mikrofonu **podrž tlačítko Link** (bliká modro-zeleně).
            8. Na displeji kamery se objeví **DJI Mic 3 TX**.
            9. **Klikni na tento řádek.**
            """)

    elif scenar == "2. Připojení BEZDRÁTOVÉHO PŘIJÍMAČE (Celý DJI set s kabelem)":
        st.header("📡 Propojení kamery s Media Modem a přijímačem RX")
        
        # Poměr sloupců upraven ve prospěch videa [1.5, 1]
        video_sl, text_sl = st.columns([1.5, 1], gap="medium")
        
        with video_sl:
            st.write("**Videonávod:**")
            # --- ZDE JE TVŮJ NOVÝ ODKAZ Z SHAREPOINTU ---
            st.markdown("""
            <iframe src="https://legogroup-my.sharepoint.com/personal/jan_drvota_lego_com/_layouts/15/embed.aspx?UniqueId=061cd250-a744-4be2-8bd8-d404aed6f8d8&embed=%7B%22ust%22%3Atrue%2C%22hv%22%3A%22CopyEmbedCode%22%7D&referrer=StreamWebApp&referrerScenario=EmbedDialog.Create" width="100%" height="360" frameborder="0" scrolling="no" allowfullscreen title="GoPro přijímač.mp4"></iframe>
            """, unsafe_allow_html=True)

        with text_sl:
            st.markdown("""
            ### Instalace Media Modu
            1. **Odstraň dvířka** kamery.
            2. **Otevři Media Mod**.
            3. **Vlož kameru** a propoj konektory.
            4. **Zavři Media Mod**.

            ### Příprava DJI přijímače
            5. **Vyjmi přijímač** z pouzdra.
            6. **Potvrď informaci** s QR kódem (Confirm).
            7. **Vyjmi oba mikrofony** (kontroluj zelené diody).

            ### Fyzické propojení
            8. **Nasuň přijímač** z boku Media Modu displejem k sobě.
            9. **Zapoj kabel** do přijímače (OUT).
            10. **Zapoj kabel do kamery** (spodní vstup na Media Modu).
            11. **Zapni kameru**.
            """)
            
    # --- NOVÁ SEKCE PRO FAST MANUAL ---
    elif scenar == "3. Fast manual propojení (Rychlý obrázkový tahák)":
        st.header("⚡ Fast manual propojení")
        st.markdown("*Rychlý přehled pro zapojení bez zbytečných řečí. Kliknutím na obrázek si ho můžeš zvětšit.*")
        
        # Surový (raw) odkaz na tvůj obrázek na GitHubu
        raw_image_url = "
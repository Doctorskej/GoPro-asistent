import streamlit as st

# 1. NASTAVENÍ STRÁNKY (Musí být na úplném začátku)
st.set_page_config(page_title="GoPro & DJI Asistent", page_icon="🎬", layout="centered")

# 2. VLASTNÍ MODERNÍ DESIGN (CSS Injekce)
# Zde si můžeš do uvozovek vložit odkaz na jakoukoliv jinou fotku (např. staženou z Unsplash.com)
pozadi_url = "https://images.unsplash.com/photo-1464822759023-fed622ff2c3b?q=80&w=2000&auto=format&fit=crop"

st.markdown(f"""
<style>
/* Obrázek na pozadí přes celou obrazovku */
.stApp {{
    background-image: url("{pozadi_url}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

/* Tmavý, poloprůhledný podklad pod textem (Glassmorphism) */
.block-container {{
    background-color: rgba(15, 15, 15, 0.85); 
    padding: 3rem;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8);
    backdrop-filter: blur(5px);
}}

/* Změna barvy hlavních nadpisů na dynamickou "GoPro modrou" */
h1, h2, h3 {{
    color: #00AEEF !important;
    font-weight: 800 !important;
}}

/* Světlejší text pro lepší čitelnost na tmavém pozadí */
p, li {{
    color: #F0F0F0;
    font-size: 1.1rem;
}}

/* Cool vzhled pro rozbalovací menu */
div[data-baseweb="select"] > div {{
    background-color: #222222;
    border: 2px solid #00AEEF;
    border-radius: 10px;
    color: white;
}}
</style>
""", unsafe_allow_html=True)

# --- ZBYTEK TVÉ APLIKACE ---

st.title("🎬 GoPro & DJI Asistent")
st.write("Vyber si typ připojení zvuku, který jdeš zrovna zapojit, a já ti dám přesný návod.")

scenar = st.selectbox(
    "Co máš dnes v plánu?",
    (
        "Vyber postup zapojení...",
        "1. Připojení JEDNOHO mikrofonu (Napřímo přes Bluetooth)",
        "2. Připojení BEZDRÁTOVÉHO PŘIJÍMAČE (Celý DJI set s kabelem)"
    )
)

if scenar == "1. Připojení JEDNOHO mikrofonu (Napřímo přes Bluetooth)":
    st.header("🔵 Postup pro přímé Bluetooth spojení")
    
    st.write("**Videonávod: Jak přepnout mikrofon a spárovat ho**")
    st.video("https://www.youtube.com/watch?v=AuJlC2V7XEQ&t=613s")

    st.markdown("""
    *Ideální pro maximální minimalismus. Nepotřebuješ Media Mod ani přijímač.*

    ### 1. Příprava mikrofonu (Vysílače DJI Mic 2):
    * Zapni mikrofon (podrž boční zapínací tlačítko, rozsvítí se zelená dioda).
    * **Přepnutí do Bluetooth režimu:** Podrž tlačítko **Nahrávání (Record)** s červenou tečkou zhruba na 3 vteřiny, dokud boční kontrolka nezmění barvu ze zelené na **modrou** (začne pomalu blikat).
    * **Párovací režim:** Nyní podrž tlačítko **Link** (Párování - hned vedle diody) asi na 2 vteřiny, dokud modrá kontrolka nezačne **rychle blikat**. Mikrofon teď hledá kameru.

    ### 2. Nastavení na GoPro HERO13:
    * Zapni kameru a stáhni horní menu prstem dolů (Dashboard).
    * Přejdi prstem doleva na **Předvolby (Preferences)** ➔ **Bezdrátová připojení (Wireless Connections)** ➔ **Připojit zařízení (Connect Device)**.
    * Vyber možnost **Bluetooth zařízení**. Kamera začne vyhledávat.

    ### 3. Spojení a kontrola:
    * Jakmile se na displeji kamery objeví **"DJI Mic 2"**, klikni na něj.
    * Dioda na mikrofonu přestane blikat a začne svítit **nepřerušovaně modře**.
    """)

elif scenar == "2. Připojení BEZDRÁTOVÉHO PŘIJÍMAČE (Celý DJI set s kabelem)":
    st.header("📡 Postup pro plný DJI Mic 2 systém")
    
    st.write("**Videonávod: Fyzické zapojení sestavy**")
    st.video("https://www.youtube.com/watch?v=9L9m5B8pXxE")

    st.markdown("""
    *Profesionální řešení pro 100% spolehlivost a interní zálohu zvuku.*

    ### Co potřebuješ:
    1.  **GoPro HERO13 Black** v nasazeném **Media Modu**.
    2.  **DJI Mic 2 Receiver** (Přijímač) a **Transmitter** (Vysílač).
    3.  **3.5mm TRS kabel** (kroucený, s černými kroužky).

    ### Postup instalace:
    1.  **Uchycení:** Nasuň DJI Mic 2 Receiver do horních nebo bočních sáněk na Media Modu. Displej směřuje k tobě.
    2.  **Propojení zvuku kabelem:** Jeden konec kabelu zapoj do výstupu na DJI přijímači ("OUT") a druhý konec do vstupu na zadní straně Media Modu (ikona mikrofonu).

    ### Konfigurace a kontrola:
    1.  **Nastavení v menu GoPro:** Jdi do: **Předvolby (Preferences)** ➔ **Vstupy/Výstupy (Audio Input)** a zvol možnost **Standardní mikrofon (Standard Mic)**.
    2.  **Zisk na DJI:** Na displeji přijímače nastav výstupní úroveň (Gain) na **-6 dB**, abys zvuk nepřebudil.
    3.  **Kontrola:** Na displeji kamery i přijímače musí při mluvení skákat zelené audio sloupečky.
    """)
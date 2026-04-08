import streamlit as st

# 1. NASTAVENÍ STRÁNKY
st.set_page_config(page_title="GoPro Asistent", page_icon="🎬", layout="wide")

# 2. VLASTNÍ MODERNÍ DESIGN
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

/* --------------------------------------------------- */
/* NOVÝ HACK NA ZNIČENÍ ČERVENÝCH PUNTÍKŮ              */
/* --------------------------------------------------- */

/* 1. Úplně skryjeme ten otravný vykreslený puntík (SVG) */
div[data-testid="stRadio"] svg {{
    display: none !important;
}}

/* 2. Základní vzhled neaktivní karty */
div[data-testid="stRadio"] label {{
    background-color: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(0, 174, 239, 0.3);
    padding: 12px 20px;
    border-radius: 10px;
    margin-bottom: 8px;
    cursor: pointer;
    transition: all 0.2s ease;
}}

/* 3. Vzhled karty, když na ni jen najedeš myší */
div[data-testid="stRadio"] label:hover {{
    background-color: rgba(0, 174, 239, 0.15) !important;
    border-color: #00AEEF !important;
}}

/* 4. MAGIE: Vzhled karty, když je VYBRANÁ (rozsvítí se modře) */
div[data-testid="stRadio"] label:has(input[type="radio"]:checked) {{
    background-color: rgba(0, 174, 239, 0.3) !important;
    border: 2px solid #00AEEF !important;
    box-shadow: 0 0 15px rgba(0, 174, 239, 0.4);
}}

div[role="radiogroup"] {{
    gap: 10px;
}}
/* --------------------------------------------------- */

/* Provzdušnění odrážek */
li {{
    color: #FFFFFF !important;
    font-size: 1.1rem;
    font-weight: 500;
    margin-bottom: 0.8rem;
    line-height: 1.5;
}}

/* Odkazy */
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
div[data-testid="stVideo"], iframe {{
    border-radius: 10px;
    overflow: hidden;
    box-shadow: 0 4px 15px rgba(0, 0, 0, 0.5);
}}
</style>
""", unsafe_allow_html=True)

# --- HLAVNÍ OBSAH ---

st.title("🎬 GoPro Asistent")
st.write("Vyber si typ připojení:")

levy_sloupec, pravy_sloupec = st.columns([3, 2], gap="large")

with levy_sloupec:
    scenar = st.radio(
        "label_hidden",
        (
            "1. Připojení JEDNOHO mikrofonu (Napřímo přes Bluetooth)",
            "2. Připojení BEZDRÁTOVÉHO PŘIJÍMAČE (Celý DJI set s kabelem)"
        ),
        label_visibility="collapsed"
    )

    if scenar == "1. Připojení JEDNOHO mikrofonu (Napřímo přes Bluetooth)":
        st.header("🔵 Postup pro přímé Bluetooth spojení")
        
        video_sl, text_sl = st.columns([1.5, 1], gap="medium")
        
        with video_sl:
            st.write("**Videonávod:**")
            st.video("https://www.youtube.com/watch?v=LXb3EKWsInQ")

        with text_sl:
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

    elif scenar == "2. Připojení BEZDRÁTOVÉHO PŘIJÍMAČE (Celý DJI set s kabelem)":
        st.header("📡 Propojení kamery s Media Modem a přijímačem RX")
        
        video_sl, text_sl = st.columns([1.5, 1], gap="medium")
        
        with video_sl:
            st.write("**Videonávod:**")
            st.video("https://youtu.be/2fdjLctioTs")

        with text_sl:
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

with pravy_sloupec:
    st.header("💡 Tipy a triky")
    st.markdown("""
    **🎥 Videonávody:**
    * [Jak správně uchytit GoPro na rám stroje](https://www.youtube.com/watch?v=LXb3EKWsInQ)
    * [Jak nastavit expozici v temné hale](https://www.youtube.com/watch?v=LXb3EKWsInQ)
    
    ---
    **Další užitečné odkazy:**
    * 📄 [Kompletní manuál k DJI Mic (PDF)](#)
    * ⚙️ [Objednávka náhradních baterií (Intranet)](#)
    """)
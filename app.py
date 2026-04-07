import streamlit as st

# 1. NASTAVENÍ STRÁNKY
st.set_page_config(page_title="GoPro & DJI Asistent", page_icon="🎬", layout="wide")

# 2. VLASTNÍ MODERNÍ DESIGN
pozadi_url = "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=2000&auto=format&fit=crop"

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
    background-color: rgba(15, 15, 15, 0.65); 
    padding: 3rem;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8);
    backdrop-filter: blur(2px);
}}

/* Změna barvy hlavních nadpisů na dynamickou "GoPro modrou" */
h1, h2, h3 {{
    color: #00AEEF !important;
    font-weight: 800 !important;
    text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.9);
}}

/* Světlejší text pro lepší čitelnost na tmavém pozadí */
p, li, label, div.stRadio > div {{
    color: #FFFFFF !important;
    font-size: 1.1rem;
    font-weight: 500;
    text-shadow: 1px 1px 4px rgba(0, 0, 0, 0.9);
}}

/* Lehké zakulacení a stín pro samotná videa */
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

# --- ZMĚNA: Úprava poměru sloupců pro širší pravý panel (poměr 3:2) ---
levy_sloupec, pravy_sloupec = st.columns([3, 2], gap="large")

# --- HLAVNÍ OBSAH (LEVÝ SLOUPEC) ---
with levy_sloupec:
    scenar = st.radio(
        "Co máš dnes v plánu?",
        (
            "1. Připojení JEDNOHO mikrofonu (Napřímo přes Bluetooth)",
            "2. Připojení BEZDRÁTOVÉHO PŘIJÍMAČE (Celý DJI set s kabelem)"
        )
    )

    if scenar == "1. Připojení JEDNOHO mikrofonu (Napřímo přes Bluetooth)":
        st.header("🔵 Postup pro přímé Bluetooth spojení")
        
        video_sl, text_sl = st.columns([1, 1.2], gap="medium")
        
        with video_sl:
            st.write("**Videonávod:**")
            st.video("https://www.youtube.com/watch?v=9L9m5B8pXxE")
            st.markdown("*Ideální pro maximální minimalismus.*")

        with text_sl:
            st.markdown("""
            ### Příprava mikrofonu:
            1. **Vyjmi mikrofon** z dokovací stanice DJI.
            2. **Zkontroluj napájení:** Mikrofon musí být zapnutý (bliká zelené tlačítko).
               * *Tip: Pokud nesvítí, zapni ho podržením červeného tlačítka.*

            ### Nastavení kamery:
            3. **Zapni kameru** stisknutím bočního tlačítka `MODE`.
            4. Na displeji **přejeď prstem seshora dolů**.
            5. Následně **přejeď prstem doleva**.
            6. Stiskni možnost **„Pair device“**.

            ### Samotné párování:
            7. Na mikrofonu **podrž tlačítko Link** na 3 vteřiny (bliká modro-zeleně).
            8. Na displeji kamery se objeví **DJI Mic 3 TX**.
            9. **Klikni na tento řádek.** Zařízení se úspěšně propojí.
            """)

    elif scenar == "2. Připojení BEZDRÁTOVÉHO PŘIJÍMAČE (Celý DJI set s kabelem)":
        st.header("📡 Propojení kamery s Media Modem a přijímačem RX")
        
        video_sl, text_sl = st.columns([1, 1.2], gap="medium")
        
        with video_sl:
            st.write("**Videonávod:**")
            st.video("https://www.youtube.com/watch?v=9L9m5B8pXxE")

        with text_sl:
            st.markdown("""
            ### Instalace Media Modu:
            1. **Odstraň dvířka** kamery.
            2. **Otevři Media Mod**.
            3. **Vlož kameru** do Media Modu.
            4. **Zavři Media Mod**.

            ### Příprava DJI přijímače:
            5. **Vyjmi přijímač** z pouzdra.
            6. **Potvrď informaci** s QR kódem na displeji (Confirm).
            7. **Vyjmi oba mikrofony** a zkontroluj zelené diody.

            ### Fyzické propojení:
            8. **Nasuň přijímač** z boku Media Modu displejem k sobě.
            9. **Zapoj kabel** do přijímače (konektor OUT).
            10. **Zapoj kabel do kamery** (spodní vstup na Media Modu).
            11. **Zapni kameru**.
            """)

# --- TIPY A TRIKY (PRAVÝ SLOUPEC) ---
with pravy_sloupec:
    st.header("💡 Tipy a triky")
    st.markdown("*Užitečné rady pro natáčení na linkách.*")
    
    # --- ZMĚNA: Odstraněna videa, nahrazeno odkazy s ikonkami ---
    st.markdown("""
    **🎥 Videonávody:**
    * [Jak správně uchytit GoPro na rám stroje](https://www.youtube.com/watch?v=9L9m5B8pXxE)
    * [Jak nastavit expozici (obraz) v temné hale](https://www.youtube.com/watch?v=9L9m5B8pXxE)
    
    ---
    **Další užitečné odkazy:**
    * 📄 [Kompletní manuál k DJI Mic (PDF)](#)
    * ⚙️ [Objednávka náhradních baterií (Intranet)](#)
    """)
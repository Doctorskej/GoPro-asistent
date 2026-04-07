import streamlit as st

# 1. NASTAVENÍ STRÁNKY (Nyní jako "wide", aby se vešel boční panel)
st.set_page_config(page_title="GoPro & DJI Asistent", page_icon="🎬", layout="wide")

# 2. VLASTNÍ MODERNÍ DESIGN (Průmyslová linka pozadí)
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

# Vytvoření dvou sloupců (levý je 2x širší než pravý)
levy_sloupec, pravy_sloupec = st.columns([2, 1], gap="large")

# --- HLAVNÍ OBSAH (LEVÝ SLOUPEC) ---
with levy_sloupec:
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
        st.video("https://www.youtube.com/watch?v=9L9m5B8pXxE")

        st.markdown("""
        ### Příprava mikrofonu:
        1. **Vyjmi mikrofon** z dokovací stanice DJI.
        2. **Zkontroluj napájení:** Mikrofon musí být zapnutý (bliká zelené tlačítko).
           * *Tip: Pokud nesvítí, zapni ho podržením červeného tlačítka, dokud se nerozbliká zelená dioda.*

        ### Nastavení kamery:
        3. **Zapni kameru** stisknutím bočního tlačítka `MODE`.
        4. Na displeji **přejeď prstem seshora dolů** (otevře se horní menu).
        5. Následně **přejeď prstem doleva** na další obrazovku.
        6. Stiskni možnost **„Pair device“** (Spárovat zařízení).

        ### Samotné párování:
        7. Na mikrofonu **podrž tlačítko Link** na 3 vteřiny (dioda začne blikat modro-zeleně).
        8. Na displeji kamery se po chvíli objeví nápis **DJI Mic 3 TX**.
        9. **Klikni na tento řádek.** Zařízení se úspěšně propojí (text na kameře zmodrá a dioda na mikrofonu začne svítit nepřerušovaně modře).
        """)

    elif scenar == "2. Připojení BEZDRÁTOVÉHO PŘIJÍMAČE (Celý DJI set s kabelem)":
        st.header("📡 Propojení kamery s Media Modem a přijímačem RX")
        
        st.write("**Videonávod: Fyzické zapojení sestavy**")
        st.video("https://www.youtube.com/watch?v=9L9m5B8pXxE")

        st.markdown("""
        ### Instalace Media Modu:
        1. **Odstraň dvířka** kamery.
        2. **Otevři Media Mod**.
        3. **Vlož kameru** do Media Modu, aby se konektory propojily.
        4. **Zavři Media Mod**.

        ### Příprava DJI přijímače a mikrofonů:
        5. **Vyjmi přijímač** z pouzdra.
        6. **Potvrď informaci** s QR kódem na displeji přijímače (Confirm).
        7. **Vyjmi oba mikrofony** a zkontroluj, že jejich diody svítí zeleně.

        ### Fyzické propojení:
        8. **Nasuň přijímač** z boku Media Modu displejem směrem k sobě.
        9. **Zapoj kabel** do přijímače (konektor OUT).
        10. **Zapoj kabel do kamery** (do spodního vstupu na zadní straně Media Modu).
        11. **Zapni kameru**.
        """)

# --- TIPY A TRIKY (PRAVÝ SLOUPEC) ---
with pravy_sloupec:
    st.header("💡 Tipy a triky")
    st.markdown("*Užitečné rady pro natáčení na linkách.*")
    
    st.write("**Jak správně uchytit GoPro na rám stroje:**")
    st.video("https://www.youtube.com/watch?v=9L9m5B8pXxE")
    
    st.write("**Jak nastavit expozici (obraz) v temné hale:**")
    st.video("https://www.youtube.com/watch?v=9L9m5B8pXxE")

    st.markdown("""
    ---
    **Další užitečné odkazy:**
    * 📄 [Kompletní manuál
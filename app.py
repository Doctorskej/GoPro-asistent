import streamlit as st

st.set_page_config(
    page_title="GoPro Asistent",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== CSS - FIX CHYBY + ZSĚVĚTLENÍ ====================
pozadi_url = "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=2000&auto=format&fit=crop"

# Používáme zdvojené závorky {{ }}, aby Python nehlásil NameError
st.markdown(f"""
<style>
    /* ZESVĚTLENÍ POZADÍ - filtr snížen na 0.5, aby byla fotka lépe vidět */
    .stApp {{
        background-image: linear-gradient(rgba(8, 12, 22, 0.5), rgba(8, 12, 22, 0.45)), url("{pozadi_url}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    .stTabs [data-baseweb="tab-highlight"] {{ background-color: transparent !important; height: 0 !important; }}
    .stTabs [data-baseweb="tab-border"] {{ display: none !important; }}

    .stTabs [data-baseweb="tab-list"] {{ gap: 14px; padding-bottom: 15px; }}
    .stTabs [data-baseweb="tab"] {{
        background: rgba(0, 0, 0, 0.4);
        border-radius: 14px;
        padding: 15px 26px;
        font-size: 1.1rem;
        font-weight: 600;
        color: #FFFFFF;
        border: 1px solid rgba(0, 174, 239, 0.4);
        transition: all 0.3s ease;
    }}
    .stTabs [data-baseweb="tab"]:hover {{ background: rgba(0, 174, 239, 0.3); border-color: #00AEEF; }}
    .stTabs [data-baseweb="tab"][aria-selected="true"] {{
        background: rgba(0, 174, 239, 0.5) !important;
        border: 2px solid #00AEEF !important;
        box-shadow: 0 0 25px rgba(0, 174, 239, 0.4);
    }}

    .glass-card {{
        background: rgba(0, 0, 0, 0.5) !important;
        backdrop-filter: blur(8px);
        border: 1px solid rgba(255, 255, 255, 0.2);
        border-radius: 18px;
        padding: 2.2rem;
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.5);
    }}

    h1, h2, h3 {{ color: #00AEEF !important; font-weight: 800; text-shadow: 2px 2px 4px rgba(0,0,0,0.5); }}
    p, li, label {{ color: #FFFFFF !important; font-weight: 500; }}

    /* OPRAVA SEKCE ŘEŠENÍ PROBLÉMŮ - Maximální kontrast */
    div[data-testid="stExpander"] {{
        border: 2px solid #00AEEF !important;
        border-radius: 12px !important;
        background-color: #FFFFFF !important;
    }}
    div[data-testid="stExpander"] summary {{
        background-color: #FFFFFF !important;
        color: #000000 !important;
        border-radius: 12px !important;
        padding: 10px !important;
    }}
    /* Vynucení černé barvy textu uvnitř bílého expanderu */
    div[data-testid="stExpander"] p, 
    div[data-testid="stExpander"] li, 
    div[data-testid="stExpander"] span,
    div[data-testid="stExpander"] td,
    div[data-testid="stExpander"] th {{
        color: #000000 !important;
        font-weight: 600 !important;
    }}
    
    .manual-card {{
        background: rgba(0, 174, 239, 0.2);
        border: 1px solid #00AEEF;
        border-radius: 16px;
        padding: 1.2rem;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        transition: 0.3s;
    }}
    .manual-card:hover {{ background: rgba(0, 174, 239, 0.4); transform: scale(1.02); }}
</style>
""", unsafe_allow_html=True)

# ==================== OBSAH ====================
st.title("📹 GoPro Asistent")
st.markdown("### Návody pro Hero 13 + DJI Mic 3")

tab1, tab2, tab3 = st.tabs([
    "🔵 Bluetooth připojení",
    "📡 Media Mod (Kabel)",
    "⚡ Rychlý tahák"
])

with tab1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("🔵 Přímé připojení Bluetooth")
    col_v, col_t = st.columns([1.6, 1], gap="medium")
    with col_v:
        st.markdown(f'<iframe src="https://legogroup-my.sharepoint.com/personal/jan_drvota_lego_com/_layouts/15/embed.aspx?UniqueId=ebf4b46d-f64e-485b-be85-5bcba5ba497d&embed=%7B%22ust%22%3Atrue%2C%22hv%22%3A%22CopyEmbedCode%22%7D&referrer=StreamWebApp&referrerScenario=EmbedDialog.Create" width="100%" height="350" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
    with col_t:
        st.markdown("1. Vyndej mikrofon (bliká zeleně).\n2. Zapni GoPro (**MODE**).\n3. Přejeď dolů -> doleva.\n4. Zvol **Pair device**.\n5. Na mikrofonu 2x stiskni Link (modrá).\n6. Podrž Link 3s (modro-zelená).\n7. Klikni na DJI Mic 3 na displeji.")
    st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("📡 Připojení přes Media Mod")
    col_v, col_t = st.columns([1.6, 1], gap="medium")
    with col_v:
        st.markdown(f'<iframe src="https://legogroup-my.sharepoint.com/personal/jan_drvota_lego_com/_layouts/15/embed.aspx?UniqueId=061cd250-a744-4be2-8bd8-d404aed6f8d8&embed=%7B%22ust%22%3Atrue%2C%22hv%22%3A%22CopyEmbedCode%22%7D&referrer=StreamWebApp&referrerScenario=EmbedDialog.Create" width="100%" height="350" frameborder="0" allowfullscreen></iframe>', unsafe_allow_html=True)
    with col_t:
        st.markdown("1. Nasaď kameru do Media Modu.\n2. Zapni přijímač (**Confirm**).\n3. Nasuň jej do sáněk Modu.\n4. Zapoj kabel (OUT -> spodní jack).\n5. Sleduj sloupečky zvuku na displeji.")
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("⚡ Rychlý tahák")
    st.image("https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro%20propojen%C3%AD.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== TIPY A REŠENÍ ====================
st.divider()
c1, c2 = st.columns([3, 2])

with c2:
    st.header("💡 Tipy a řešení")
    
    with st.expander("📸 Nastavení kamery (Doporučeno)"):
        st.write("| Režim | Rozlišení | Čočka | Stabilizace |")
        st.write("| :--- | :--- | :--- | :--- |")
        st.write("| **Linka** | 4K / 30 | Wide | AutoBoost |")
        st.write("| **Detail** | 4K / 30 | **Linear** | Horizon Lock |")
        st.write("| **Šero** | 4K / 24 | Linear | Standard |")

    with st.expander("🛠️ Řešení problémů"):
        st.markdown("**Bluetooth:** Vypni BT na mobilu, mikrofon se k němu často 'přilepí'.")
        st.markdown("**Kabel:** Kamera musí v Media Modu sedět nadoraz. Kabel musí v jacku 'cvaknout'.")
        st.markdown("**Hluk:** Pokud sloupce svítí červeně, sniž Gain na přijímači na -6dB.")

    st.subheader("📚 Manuály")
    u_g = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro13%20manual.pdf"
    u_d = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/DJI_Mic_3_User_Manual_CS%20(1).pdf"
    st.markdown(f'<a href="{u_g}" target="_blank" style="text-decoration:none;"><div class="manual-card">📘 Manuál GoPro 13</div></a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{u_d}" target="_blank" style="text-decoration:none;"><div class="manual-card">📘 Manuál DJI Mic 3</div></a>', unsafe_allow_html=True)

with c1:
    st.info("Tip: Čočka LINEAR je nejlepší pro nahrávání strojů – nedeformuje obraz.")
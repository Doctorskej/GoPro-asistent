import streamlit as st

st.set_page_config(
    page_title="GoPro Asistent",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== CSS ====================
# Tyrkysová barva: #00AEEF
# Tmavé poloprůhledné pozadí pro karty: rgba(0, 0, 0, 0.4)
# Světlejší tyrkysový okraj: rgba(0, 174, 239, 0.4)
# Světlejší tyrkysová box-shadow: rgba(0, 174, 239, 0.3)
# Tmavší tyrkysová barva pro text na hover: #0088cc

st.markdown("""
<style>
    h1, h2, h3 { color: #00AEEF !important; }
    p, li { color: #00AEEF !important; }

    /* Styl pro nadpisy sekcí s ikonou, které jsou volně na pozadí */
    .section-header {
        display: flex;
        align-items: center;
        margin-bottom: 20px;
    }
    .section-header-icon {
        font-size: 2rem;
        margin-right: 15px;
    }
    .section-header-text {
        color: #00AEEF;
        font-size: 1.8rem;
        font-weight: 800;
    }

    /* Styl pro expandery "Tipy a řešení" a "Řešení problémů" */
    .stExpander {
        background-color: rgba(0, 0, 0, 0.4) !important; /* Tmavší, poloprůhledné pozadí */
        border-radius: 12px !important;
        border: 1px solid rgba(0, 174, 239, 0.4) !important; /* Tyrkysový okraj */
        box-shadow: 0 0 15px rgba(0, 174, 239, 0.3) !important; /* Tyrkysová box-shadow pro "záři" */
        margin-bottom: 10px !important;
        transition: transform 0.2s ease, box-shadow 0.2s ease !important;
    }
    .stExpander:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 0 20px rgba(0, 174, 239, 0.4) !important;
    }
    .stExpander summary {
        color: #00AEEF !important; /* Tyrkysový text */
        font-weight: 600 !important;
    }

    /* Styl pro banery "Manuály", aby vypadaly stejně jako expandery */
    .glass-card-banner {
        background-color: rgba(0, 0, 0, 0.4);
        backdrop-filter: blur(8px);
        border-radius: 12px;
        border: 1px solid rgba(0, 174, 239, 0.4);
        box-shadow: 0 0 15px rgba(0, 174, 239, 0.3);
        padding: 12px 15px;
        margin-bottom: 10px;
        display: flex;
        align-items: center;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }
    .glass-card-banner:hover {
        transform: translateY(-2px);
        box-shadow: 0 0 20px rgba(0, 174, 239, 0.4);
    }
    .glass-card-text {
        color: #00AEEF;
        font-weight: 600;
        margin-left: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ==================== OBSAH ====================
# Nadpis s tyrkysovou barvou textu a ikonou sešitu, volně na pozadí
st.markdown("""
<div class="section-header">
    <span class="section-header-icon">📘</span>
    <span class="section-header-text">GoPro Asistent</span>
</div>
""", unsafe_allow_html=True)
st.markdown("<p>Návod pro nahrávání údržby a technických instruktáží (Hero 13 + DJI Mic 3)</p>", unsafe_allow_html=True)

# ... (Kód pro záložky a videa, s tyrkysovými nadpisy a textem) ...

st.divider()

col_left, col_right = st.columns(2)

with col_left:
    # Sekce Tipy a řešení s tyrkysovým nadpisem a ikonou žárovky, volně na pozadí
    st.markdown("""
    <div class="section-header">
        <span class="section-header-icon">💡</span>
        <span class="section-header-text">Tipy a řešení</span>
    </div>
    """, unsafe_allow_html=True)
    # Expandery s tyrkysovým textem, tmavým pozadím, svítícím tyrkysovým okrajem.
    # Ikona a text na začátku textu expanderu zůstávají.
    with st.expander("Doporučené průmyslové profily"):
        st.write("- **Pohyb u linky:** 4K / 30 FPS, Čočka: Wide, Stabilizace: AutoBoost, Barvy: Natural")
        st.write("- **Technický detail a údržba:** 4K / 30 FPS, Čočka: Linear (Zcela zásadní!), Horizon Lock: Zapnuto, Barvy: Vibrant")
        st.write("- **Inspekce v temných prostorech:** 24 FPS, ISO Max: 1600, Ostrost (Sharpness): Medium, Stabilizace: Standard")

    with st.expander("Řešení problémů (Troubleshooting)"):
        st.write("- **Kamera nevidí mikrofon:** Vypni Bluetooth v mobilu, mikrofon se k němu možná 'přilepil'.")
        st.write("- **Není slyšet zvuk:** Zkontroluj, zda je kamera v Modu doražená až nadoraz na USB-C.")
        st.write("- **Příliš hlasitý zvuk:** Pokud indikátor hlasitosti na displeji dosahuje červených hodnot, v menu přijímače snižte zesílení (Gain) na -6 nebo -12 dB.")

with col_right:
    # Sekce Manuály s tyrkysovým nadpisem a ikonou sešitu, volně na pozadí
    st.markdown("""
    <div class="section-header">
        <span class="section-header-icon">📘</span>
        <span class="section-header-text">Manuály</span>
    </div>
    """, unsafe_allow_html=True)
    # Banery: Odstranit modrou poloprůhlednou kartu, ve které byly manuály.
    # Vytvořit divy s novou třídou "glass-card-banner", aby vypadaly stejně jako expandery (tmavé pozadí, tyrkysový svítící okraj, tyrkysový text).
    # Zachovat ikony sešitu a text manuálů.
    # Odkazy na manuály nastavit tak, aby se otevíraly v nové záložce.
    url_gopro = "https://example.com/gopro_manual.pdf" # Nahraďte skutečnou URL
    url_dji = "https://example.com/dji_manual.pdf" # Nahraďte skutečnou URL

    st.markdown(f'<a href="{url_gopro}" target="_blank" style="text-decoration:none;"><div class="glass-card-banner"><span class="glass-card-icon">📘</span><span class="glass-card-text">Manuál GoPro Hero 13</span></div></a>', unsafe_allow_html=True)
    st.markdown(f'<a href="{url_dji}" target="_blank" style="text-decoration:none;"><div class="glass-card-banner"><span class="glass-card-icon">📘</span><span class="glass-card-text">Manuál DJI Mic 3</span></div></a>', unsafe_allow_html=True)
import streamlit as st

# ==================== KONSTANTY ====================
BACKGROUND_URL = "https://images.unsplash.com/photo-1581091226825-a6a2a5aee158?q=80&w=2000&auto=format&fit=crop"
MANUAL_GOPRO = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro%20manual.pdf"
MANUAL_DJI = "https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/DJI_Mic_3_User_Manual_CS%20(1).pdf"

# ==================== CONFIG ====================
st.set_page_config(
    page_title="GoPro Asistent",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==================== STYLY ====================
def load_styles():
    st.markdown(f"""
    <style>
        .stApp {{
            background-image: linear-gradient(rgba(8, 12, 22, 0.82), rgba(8, 12, 22, 0.78)), url('{BACKGROUND_URL}');
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}

        .glass-card {{
            background: rgba(0, 0, 0, 0.68);
            backdrop-filter: blur(16px);
            border: 1px solid rgba(255,255,255,0.18);
            border-radius: 20px;
            padding: 2.5rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.6);
        }}

        h1, h2, h3 {{
            color: #00AEEF;
        }}

        p, li {{
            color: white;
            line-height: 1.6;
        }}

        .manual-card {{
            background: rgba(255,255,255,0.08);
            border: 1px solid rgba(0,174,239,0.4);
            border-radius: 16px;
            padding: 1.2rem;
            margin-bottom: 10px;
            display: block;
            text-decoration: none;
            color: white;
            font-weight: 600;
        }}

        .manual-card:hover {{
            background: rgba(0,174,239,0.2);
        }}

        header[data-testid="stHeader"] {{
            opacity: 0;
            pointer-events: none;
        }}
    </style>
    """, unsafe_allow_html=True)

# ==================== KOMPONENTY ====================
def manual_card(url, text):
    st.markdown(f"""
        <a href="{url}" target="_blank" style="text-decoration:none;">
            <div class="manual-card">📘 {text}</div>
        </a>
    """, unsafe_allow_html=True)


def video_embed(url):
    st.markdown(f"""
    <iframe src="{url}" style="width: 100%; aspect-ratio: 16/9; border:none;" allowfullscreen></iframe>
    """, unsafe_allow_html=True)

# ==================== APP ====================
load_styles()

st.title("📹 GoPro Asistent")
st.markdown("**Průvodce pro Hero 13 + DJI Mic 3**")

tab1, tab2, tab3 = st.tabs([
    "🔵 Jeden mikrofon",
    "📡 Oba mikrofony",
    "⚡ Tahák"
])

# ==================== TAB 1 ====================
with tab1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("Připojení přes Bluetooth")

    col1, col2 = st.columns([2,1])

    with col1:
        video_embed("https://legogroup-my.sharepoint.com/personal/jan_drvota_lego_com/_layouts/15/embed.aspx?UniqueId=ebf4b46d-f64e-485b-be85-5bcba5ba497d")

    with col2:
        st.markdown("""
        1. Vyjmi mikrofon
        2. Zapni GoPro
        3. Pair device
        4. Podrž link
        """)

    st.success("Připraveno k připojení")
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== TAB 2 ====================
with tab2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("Media Mod")

    col1, col2 = st.columns([2,1])

    with col1:
        video_embed("https://legogroup-my.sharepoint.com/personal/jan_drvota_lego_com/_layouts/15/embed.aspx?UniqueId=061cd250-a744-4be2-8bd8-d404aed6f8d8")

    with col2:
        st.markdown("""
        1. Vlož kameru
        2. Připoj přijímač
        3. Propoj kabel
        4. Zkontroluj zvuk
        """)

    st.success("Audio aktivní")
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== TAB 3 ====================
with tab3:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.image("https://raw.githubusercontent.com/Doctorskej/GoPro-asistent/main/GoPro%20propojen%C3%AD.png", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ==================== FOOTER ====================
st.divider()

col_left, col_right = st.columns([3,2])

with col_left:
    st.info("Tip: LINEAR čočka = žádné zkreslení")

with col_right:
    st.subheader("Manuály")
    manual_card(MANUAL_GOPRO, "GoPro Hero 13")
    manual_card(MANUAL_DJI, "DJI Mic 3")

st.caption("GoPro Asistent • Refaktor 2026")

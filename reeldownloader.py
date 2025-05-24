import streamlit as st
from PIL import Image
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="ReelDownloader Pro",
    page_icon="💧",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Color Scheme (Primarily from the first image, login inputs from second) ---
PRIMARY_BACKGROUND_COLOR = "#F8F9FA"
SIDEBAR_BACKGROUND_COLOR = "#FFFFFF"
ACCENT_BLUE_COLOR = "#0D6EFD"  # Main buttons, highlights
TEXT_COLOR_DARK = "#212529"
TEXT_COLOR_LIGHT = "#6C757D"
GREEN_COLOR = "#198754"
PURPLE_ACCENT_COLOR = "#6F42C1"  # Premium features
LOGIN_INPUT_BG_COLOR = "#2D3748" # Dark color for login inputs from new image
LOGIN_INPUT_TEXT_COLOR = "#FFFFFF"
LOGIN_INPUT_BORDER_COLOR = "#4A5568"


# --- Custom CSS ---
st.markdown(
    f"""
    <style>
        /* Main app background */
        .stApp {{
            background-color: {PRIMARY_BACKGROUND_COLOR};
        }}

        /* Sidebar */
        [data-testid="stSidebar"] > div:first-child {{
            background-color: {SIDEBAR_BACKGROUND_COLOR};
            border-right: 1px solid #dee2e6;
        }}

        /* Sidebar General Text & Headers */
        [data-testid="stSidebar"] h1,
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3,
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] label {{
            color: {TEXT_COLOR_DARK};
        }}

        /* Sidebar Logo */
        [data-testid="stSidebar"] .stImage {{
            display: flex;
            justify-content: center; /* Center logo if you use st.image */
            margin-bottom: 10px;
        }}
        [data-testid="stSidebar"] .logo-title {{ /* Custom class for text logo */
            font-size: 1.5em;
            font-weight: bold;
            text-align: left;
            padding-left: 10px; /* Align with other sidebar content */
            margin-bottom: 1rem;
        }}


        /* --- LOGIN FORM STYLING (from new screenshot) --- */
        [data-testid="stSidebar"] div[data-testid="stVerticalBlock"]  /* Target login section */
        label[data-testid="stWidgetLabel"] p {{ /* Labels: Email, Password */
            color: {TEXT_COLOR_DARK} !important;
            font-weight: 500 !important; /* Medium weight */
            font-size: 0.95rem !important;
            margin-bottom: 0.25rem !important; /* Space between label and input */
        }}

        [data-testid="stSidebar"] div[data-testid="stVerticalBlock"]
        input[type="email"],
        [data-testid="stSidebar"] div[data-testid="stVerticalBlock"]
        input[type="password"] {{
            background-color: {LOGIN_INPUT_BG_COLOR} !important;
            color: {LOGIN_INPUT_TEXT_COLOR} !important;
            border: 1px solid {LOGIN_INPUT_BORDER_COLOR} !important;
            border-radius: 0.375rem !important; /* 6px */
            padding: 0.75rem 0.75rem !important; /* Adjust padding */
        }}
        [data-testid="stSidebar"] div[data-testid="stVerticalBlock"]
        input[type="email"]::placeholder,
        [data-testid="stSidebar"] div[data-testid="stVerticalBlock"]
        input[type="password"]::placeholder {{
            color: #A0AEC0; /* Lighter placeholder text */
        }}

        /* Login Button in Sidebar */
        [data-testid="stSidebar"] button[data-testid="baseButton-secondary"] {{
            background-color: {ACCENT_BLUE_COLOR} !important;
            color: white !important;
            border-radius: 0.375rem !important;
            width: 100% !important;
            border: none !important;
            padding: 0.6rem 0 !important; /* Adjust padding for height */
            font-weight: 600 !important;
        }}
        [data-testid="stSidebar"] button[data-testid="baseButton-secondary"]:hover {{
            background-color: #0B5ED7 !important; /* Darker blue on hover */
        }}
        /* --- END LOGIN FORM STYLING --- */


        /* Main content area */
        .main .block-container {{
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }}

        h1, h2, h3, h4, h5, h6 {{ /* Main content headers */
            color: {TEXT_COLOR_DARK};
        }}
        p, .stMarkdown, .stTextInput > div > div > input, .stTextArea > div > div > textarea {{
            /* General text inputs outside login form */
            color: {TEXT_COLOR_DARK};
        }}
        .stButton > button:not([data-testid="baseButton-secondary"]) {{ /* General buttons, not login */
            background-color: {ACCENT_BLUE_COLOR};
            color: white;
            border-radius: 0.5rem;
        }}
        .stButton > button:not([data-testid="baseButton-secondary"]):hover {{
            background-color: #0B5ED7;
            color: white;
        }}
        .stCheckbox > label > span {{
            color: {TEXT_COLOR_DARK};
        }}
        .stAlert {{
            border-radius: 0.5rem;
        }}
        .premium-feature-box {{
            background-color: {PURPLE_ACCENT_COLOR}1A;
            border: 1px solid {PURPLE_ACCENT_COLOR};
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
        }}
        .premium-feature-box h3 {{
            color: {PURPLE_ACCENT_COLOR};
        }}
    </style>
    """,
    unsafe_allow_html=True,
)


# --- Mock Functions (Unchanged from previous version) ---
def mock_login(email, password):
    if email and password:
        if email.lower() == "premium@example.com":
            return True, "premium"
        return True, "standard"
    return False, None

def mock_download_reel(url, watermark_text=None, download_captions=False):
    if not url or not ("instagram.com/reel/" in url or "instagram.com/p/" in url): # Basic check
        return False, "Invalid Instagram Reel URL.", None, None
    time.sleep(2)
    mock_video_filename = f"reel_{url.split('/')[-2 if url.endswith('/') else -1]}.mp4"
    mock_caption_filename = f"reel_{url.split('/')[-2 if url.endswith('/') else -1]}_caption.txt" if download_captions else None
    if watermark_text:
        print(f"Simulating watermarking video with: {watermark_text}")
    if download_captions:
        print(f"Simulating caption download to {mock_caption_filename}")
        with open(mock_caption_filename, "w") as f: f.write("Mock caption.")
    with open(mock_video_filename, "w") as f: f.write("Mock video.")
    return True, f"Reel downloaded: {mock_video_filename}", mock_video_filename, mock_caption_filename

def mock_generate_transcript(video_path):
    time.sleep(3)
    transcript_filename = video_path.replace(".mp4", "_transcript.txt")
    with open(transcript_filename, "w") as f: f.write("Mock transcript.")
    return True, f"Transcript: {transcript_filename}", transcript_filename

# --- Session State Initialization ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""
if "user_tier" not in st.session_state:
    st.session_state.user_tier = None
if "download_queue" not in st.session_state:
    st.session_state.download_queue = []


# --- Sidebar ---
with st.sidebar:
    # Logo/Title as per new screenshot
    st.markdown("<p class='logo-title'>💧 ReelDownloader</p>", unsafe_allow_html=True)
    # st.image("logo.png", width=40) # Alternative if you have a small icon image

    st.markdown("---") # Visual separator

    if not st.session_state.logged_in:
        st.subheader("Login") # "Login" title as in screenshot
        with st.form(key="login_form"):
            email = st.text_input(
                "Email",
                key="login_email_input",
                placeholder="you@example.com",
                type="default" # Use default to allow email type input
            )
            password = st.text_input(
                "Password",
                type="password",
                key="login_password_input",
                placeholder="••••••••"
            )
            login_button = st.form_submit_button(label="Login")

            if login_button:
                success, tier = mock_login(email, password)
                if success:
                    st.session_state.logged_in = True
                    st.session_state.user_email = email
                    st.session_state.user_tier = tier
                    st.rerun()
                else:
                    st.error("Invalid email or password.")
    else:
        st.markdown(f"Welcome, **{st.session_state.user_email.split('@')[0]}**!")
        if st.session_state.user_tier == "premium":
            st.markdown(f"<span style='color:{PURPLE_ACCENT_COLOR}; font-weight:bold;'>Premium User ✨</span>", unsafe_allow_html=True)
        else:
            st.markdown("Standard User")

        if st.button("Logout", key="logout_button_sidebar", type="secondary"): # Use secondary for different styling if needed
            st.session_state.logged_in = False
            st.session_state.user_email = ""
            st.session_state.user_tier = None
            st.session_state.download_queue = []
            st.rerun()

    st.markdown("---")
    st.subheader("Navigation") # "Navigation" title as in screenshot
    st.page_link("app.py", label="Dashboard", icon="🏠")

    if st.session_state.logged_in and st.session_state.user_tier != "premium":
        st.markdown("---")
        st.markdown(
            f"""
            <div style="background-color:{PURPLE_ACCENT_COLOR}20; padding:15px; border-radius:8px; text-align:center;">
                <h4 style="color:{PURPLE_ACCENT_COLOR}; margin-bottom:10px;">Upgrade to Pro!</h4>
                <p style="font-size:0.9em; color:{TEXT_COLOR_DARK};">Unlock bulk downloads and video transcripts.</p>
                <a href="#" target="_blank" style="text-decoration: none;">
                    <button style="background-color:{PURPLE_ACCENT_COLOR}; color:white; border:none; padding:10px 20px; border-radius:5px; cursor:pointer; width:100%;">
                        Upgrade Now
                    </button>
                </a>
            </div>
            """,
            unsafe_allow_html=True
        )


# --- Main Page Content ---
if not st.session_state.logged_in:
    st.title("Welcome to ReelDownloader Pro 💧")
    st.markdown("Please log in using the sidebar to access the downloader.")
    st.info("Use `premium@example.com` and any password for premium features demo. Any other email/password for standard.")
    # The main area will show this if not logged in, avoiding the blank pink screen.
else:
    st.title("Reel Downloader Dashboard")
    # ... (The rest of the dashboard content from the previous version) ...
    # This is where your main app functionality (download forms, etc.) goes.
    # For brevity, I'm including the structure from before.

    col1, col2 = st.columns([2,1])

    with col1:
        st.subheader("Download Single Reel")
        reel_url = st.text_input("Enter Instagram Reel URL:", placeholder="https://www.instagram.com/reel/Cxyz...")

        with st.expander("Download Options"):
            watermark_enabled = st.checkbox("Add Watermark?")
            watermark_text = ""
            if watermark_enabled:
                watermark_text = st.text_input("Watermark Text:", value=f"@{st.session_state.user_email.split('@')[0]}")

            download_captions_main = st.checkbox("Download Captions (.txt)?", key="dl_captions_main")

        if st.button("Download Reel", key="download_single_reel_main"):
            if reel_url:
                with st.spinner("Processing..."):
                    success, message, video_file, caption_file = mock_download_reel(
                        reel_url,
                        watermark_text if watermark_enabled else None,
                        download_captions_main
                    )
                if success:
                    st.success(message)
                    if video_file:
                        with open(video_file, "rb") as fp:
                            st.download_button(
                                label="Download Video File", data=fp, file_name=video_file, mime="video/mp4"
                            )
                    if caption_file:
                         with open(caption_file, "rb") as fp:
                            st.download_button(
                                label="Download Caption File", data=fp, file_name=caption_file, mime="text/plain"
                            )
                else:
                    st.error(message)
            else:
                st.warning("Please enter a Reel URL.")

    with col2:
        st.subheader("Feature Spotlight")
        st.markdown(
            f"""
            <div style="background-color: {GREEN_COLOR}20; padding: 1rem; border-radius: 0.5rem; margin-top:1.5rem;">
                <h4 style="color:{GREEN_COLOR};">Real-Time Alerts</h4>
                <p style="color:{TEXT_COLOR_DARK}; font-size:0.9em;">Get notified of download completions or new features (mock).</p>
                <span style="font-size:1.5em;">🔔</span>
            </div>
            """, unsafe_allow_html=True
        )
        st.markdown( # Example of another box like in the first UI
            f"""
            <div style="background-color: #E9ECEF; padding: 1rem; border-radius: 0.5rem; margin-top:1rem;">
                <h4 style="color:{TEXT_COLOR_DARK};">Greed Index (Mock)</h4>
                <p style="color:{TEXT_COLOR_DARK}; font-size:2em; text-align:center; font-weight:bold;">82</p>
                <p style="color:{TEXT_COLOR_LIGHT}; font-size:0.9em; text-align:center;">Greed</p>
            </div>
            """, unsafe_allow_html=True
        )


    st.markdown("---")

    if st.session_state.user_tier == "premium":
        st.subheader("🚀 Premium Features")
        prem_col1, prem_col2 = st.columns(2)
        with prem_col1:
            with st.container(border=True):
                st.markdown(f"<h3 style='color:{PURPLE_ACCENT_COLOR};'>Bulk Reel Downloader</h3>", unsafe_allow_html=True)
                bulk_urls = st.text_area("Enter Reel URLs (one per line):", height=150, placeholder="https://...\nhttps://...")
                if st.button("Add to Bulk Download Queue", key="add_to_bulk_main"):
                    urls = [url.strip() for url in bulk_urls.split("\n") if url.strip()]
                    if urls:
                        st.session_state.download_queue.extend(urls)
                        st.success(f"{len(urls)} URLs added.")
                    else:
                        st.warning("Please enter at least one URL.")
                if st.session_state.download_queue:
                    st.write("Current Queue:", st.session_state.download_queue)
                    if st.button("Process Queue (Mock)", key="process_queue_main"):
                        with st.spinner("Processing bulk..."):
                            for i, url_in_q in enumerate(st.session_state.download_queue):
                                time.sleep(0.5)
                                st.progress((i + 1) / len(st.session_state.download_queue), text=f"Processing {url_in_q[:30]}...")
                            st.session_state.download_queue = []
                        st.success("Bulk download queue processed (mock).")
        with prem_col2:
            with st.container(border=True):
                st.markdown(f"<h3 style='color:{PURPLE_ACCENT_COLOR};'>Video Transcript Generator (TXT)</h3>", unsafe_allow_html=True)
                uploaded_video = st.file_uploader("Upload a downloaded Reel (.mp4):", type=["mp4"], key="transcript_upload")
                if uploaded_video:
                    if st.button("Generate Transcript", key="generate_transcript_main"):
                        with open(uploaded_video.name, "wb") as f: f.write(uploaded_video.getbuffer())
                        with st.spinner("Generating transcript..."):
                            success, message, transcript_file = mock_generate_transcript(uploaded_video.name)
                        if success:
                            st.success(message)
                            with open(transcript_file, "rb") as fp:
                                st.download_button("Download Transcript", fp, transcript_file, "text/plain")
                        else:
                            st.error(message)
    elif st.session_state.logged_in : # Show this only if logged in AND not premium
        st.info("Upgrade to Premium to unlock Bulk Downloads and Video Transcripts!")


# --- Footer ---
st.markdown("---")
st.markdown(
    f"<p style='text-align:center; color:{TEXT_COLOR_LIGHT};'>© {time.strftime('%Y')} ReelDownloader Pro. For educational purposes.</p>",
    unsafe_allow_html=True
)

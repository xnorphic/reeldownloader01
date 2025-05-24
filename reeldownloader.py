import streamlit as st
from PIL import Image
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="ReelDownloader Pro",
    page_icon="💧", # You can use an emoji or a path to an image
    layout="wide",
    initial_sidebar_state="expanded",
)

# --- Color Scheme (from your image) ---
PRIMARY_BACKGROUND_COLOR = "#F8F9FA"
SIDEBAR_BACKGROUND_COLOR = "#FFFFFF"
ACCENT_BLUE_COLOR = "#0D6EFD" # Main buttons, highlights
TEXT_COLOR_DARK = "#212529"
TEXT_COLOR_LIGHT = "#6C757D"
GREEN_COLOR = "#198754"
PURPLE_ACCENT_COLOR = "#6F42C1" # Premium features

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
            border-right: 1px solid #dee2e6; /* Light border for separation */
        }}
        [data-testid="stSidebar"] .stButton > button {{
            background-color: {ACCENT_BLUE_COLOR};
            color: white;
            border-radius: 0.5rem;
            width: 100%;
        }}
        [data-testid="stSidebar"] .stButton > button:hover {{
            background-color: #0B5ED7; /* Darker blue on hover */
            color: white;
        }}
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {{
            color: {TEXT_COLOR_DARK};
        }}
        [data-testid="stSidebar"] .stImage {{ /* Center logo in sidebar */
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }}


        /* Main content area */
        .main .block-container {{
            padding-top: 2rem;
            padding-bottom: 2rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }}

        h1, h2, h3, h4, h5, h6 {{
            color: {TEXT_COLOR_DARK};
        }}
        p, .stMarkdown, .stTextInput > div > div > input, .stTextArea > div > div > textarea {{
            color: {TEXT_COLOR_DARK};
        }}
        .stButton > button {{
            background-color: {ACCENT_BLUE_COLOR};
            color: white;
            border-radius: 0.5rem;
        }}
        .stButton > button:hover {{
            background-color: #0B5ED7;
            color: white;
        }}
        .stCheckbox > label > span {{
            color: {TEXT_COLOR_DARK};
        }}
        .stAlert {{ /* For messages */
            border-radius: 0.5rem;
        }}
        .premium-feature-box {{
            background-color: {PURPLE_ACCENT_COLOR}1A; /* Light purple */
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


# --- Mock Functions (Replace with actual implementations) ---
def mock_login(email, password):
    """Simulates a login attempt."""
    if email and password:  # Basic check
        if email == "premium@example.com":
            return True, "premium"
        return True, "standard"
    return False, None

def mock_download_reel(url, watermark_text=None, download_captions=False):
    """Simulates downloading a reel."""
    if not url.startswith("https://www.instagram.com/reel/"):
        return False, "Invalid Instagram Reel URL.", None, None
    time.sleep(2) # Simulate download time
    mock_video_filename = f"reel_{url.split('/')[-2]}.mp4"
    mock_caption_filename = f"reel_{url.split('/')[-2]}_caption.txt" if download_captions else None

    # Simulate watermarking
    if watermark_text:
        print(f"Simulating watermarking video with: {watermark_text}")

    # Simulate caption download
    if download_captions:
        print(f"Simulating caption download to {mock_caption_filename}")
        with open(mock_caption_filename, "w") as f:
            f.write("This is a mock caption for the reel.")

    with open(mock_video_filename, "w") as f: # Create a dummy file
        f.write("This is a mock video file.")
    return True, f"Reel downloaded as {mock_video_filename}!", mock_video_filename, mock_caption_filename

def mock_generate_transcript(video_path):
    """Simulates generating a transcript."""
    time.sleep(3) # Simulate transcript generation
    transcript_filename = video_path.replace(".mp4", "_transcript.txt")
    with open(transcript_filename, "w") as f:
        f.write("This is a mock transcript of the video content. Word for word...")
    return True, f"Transcript generated: {transcript_filename}", transcript_filename

# --- Session State Initialization ---
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""
if "user_tier" not in st.session_state: # 'standard' or 'premium'
    st.session_state.user_tier = None
if "download_queue" not in st.session_state:
    st.session_state.download_queue = []


# --- Sidebar ---
with st.sidebar:
    # You can add a logo here if you have one
    # For example, if you have logo.png in the same directory:
    try:
        logo = Image.open("logo.png") # Replace with your logo path
        st.image(logo, width=80)
    except FileNotFoundError:
        st.markdown("💧 **ReelDownloader**", unsafe_allow_html=True) # Fallback text logo

    st.markdown("---")

    if not st.session_state.logged_in:
        st.subheader("Login")
        email = st.text_input("Email", key="login_email")
        password = st.text_input("Password", type="password", key="login_password")
        if st.button("Login", key="login_button"):
            success, tier = mock_login(email, password)
            if success:
                st.session_state.logged_in = True
                st.session_state.user_email = email
                st.session_state.user_tier = tier
                st.rerun() # Rerun to update UI
            else:
                st.error("Invalid email or password.")
    else:
        st.markdown(f"Welcome, **{st.session_state.user_email}**!")
        if st.session_state.user_tier == "premium":
            st.markdown(f"<span style='color:{PURPLE_ACCENT_COLOR}; font-weight:bold;'>Premium User ✨</span>", unsafe_allow_html=True)
        else:
            st.markdown("Standard User")

        if st.button("Logout", key="logout_button"):
            st.session_state.logged_in = False
            st.session_state.user_email = ""
            st.session_state.user_tier = None
            st.session_state.download_queue = []
            st.rerun()

    st.markdown("---")
    st.markdown("### Navigation")
    # Could add more pages here if needed, e.g., using st.page_link (for multipage apps)
    st.page_link("app.py", label="Dashboard", icon="🏠") # Link to self for now

    if st.session_state.user_tier != "premium" and st.session_state.logged_in:
        st.markdown("---")
        st.markdown(
            f"""
            <div style="background-color:{PURPLE_ACCENT_COLOR}20; padding:15px; border-radius:8px; text-align:center;">
                <h4 style="color:{PURPLE_ACCENT_COLOR}; margin-bottom:10px;">Upgrade to Pro!</h4>
                <p style="font-size:0.9em; color:{TEXT_COLOR_DARK};">Unlock bulk downloads and video transcripts.</p>
                <a href="#" target="_blank">
                    <button style="background-color:{PURPLE_ACCENT_COLOR}; color:white; border:none; padding:10px 20px; border-radius:5px; cursor:pointer;">
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
    st.info("Use `premium@example.com` and any password for premium features demo.")

else:
    st.title("Reel Downloader Dashboard")
    st.markdown(f"Hello, {st.session_state.user_email}! Let's download some Reels.")

    col1, col2 = st.columns([2,1])

    with col1:
        st.subheader("Download Single Reel")
        reel_url = st.text_input("Enter Instagram Reel URL:", placeholder="https://www.instagram.com/reel/Cxyz...")

        with st.expander("Download Options"):
            watermark_enabled = st.checkbox("Add Watermark?")
            watermark_text = ""
            if watermark_enabled:
                watermark_text = st.text_input("Watermark Text:", value=f"@{st.session_state.user_email.split('@')[0]}")

            download_captions = st.checkbox("Download Captions (.txt)?")

        if st.button("Download Reel", key="download_single_reel"):
            if reel_url:
                with st.spinner("Processing..."):
                    success, message, video_file, caption_file = mock_download_reel(
                        reel_url,
                        watermark_text if watermark_enabled else None,
                        download_captions
                    )
                if success:
                    st.success(message)
                    if video_file: # Provide download button for the mock file
                        with open(video_file, "rb") as fp:
                            st.download_button(
                                label="Download Video File",
                                data=fp,
                                file_name=video_file,
                                mime="video/mp4"
                            )
                    if caption_file:
                         with open(caption_file, "rb") as fp:
                            st.download_button(
                                label="Download Caption File",
                                data=fp,
                                file_name=caption_file,
                                mime="text/plain"
                            )
                else:
                    st.error(message)
            else:
                st.warning("Please enter a Reel URL.")

    with col2:
        st.subheader("Feature Spotlight")
        st.markdown(
            f"""
            <div style="background-color: {GREEN_COLOR}20; padding: 1rem; border-radius: 0.5rem;">
                <h4 style="color:{GREEN_COLOR};">Real-Time Alerts</h4>
                <p style="color:{TEXT_COLOR_DARK}; font-size:0.9em;">Get notified of download completions or new features (mock).</p>
                <span style="font-size:1.5em;">🔔</span>
            </div>
            """, unsafe_allow_html=True
        )


    st.markdown("---")

    # --- Premium Features Section ---
    if st.session_state.user_tier == "premium":
        st.subheader("🚀 Premium Features")
        prem_col1, prem_col2 = st.columns(2)

        with prem_col1:
            with st.container(border=True): # Using st.container with border
                st.markdown(f"<h3 style='color:{PURPLE_ACCENT_COLOR};'>Bulk Reel Downloader</h3>", unsafe_allow_html=True)
                bulk_urls = st.text_area("Enter Reel URLs (one per line):", height=150, placeholder="https://www.instagram.com/reel/Cxyz...\nhttps://www.instagram.com/reel/Abcd...")
                if st.button("Add to Bulk Download Queue", key="add_to_bulk"):
                    urls = [url.strip() for url in bulk_urls.split("\n") if url.strip()]
                    if urls:
                        st.session_state.download_queue.extend(urls)
                        st.success(f"{len(urls)} URLs added to the queue.")
                        # In a real app, you'd process this queue
                    else:
                        st.warning("Please enter at least one URL.")

                if st.session_state.download_queue:
                    st.write("Current Queue:", st.session_state.download_queue)
                    if st.button("Process Queue (Mock)", key="process_queue"):
                        with st.spinner("Processing bulk downloads..."):
                            for i, url_in_q in enumerate(st.session_state.download_queue):
                                st.write(f"Downloading {url_in_q}...")
                                # Simulate download
                                time.sleep(1)
                                st.progress((i + 1) / len(st.session_state.download_queue), text=f"Processing {url_in_q}")
                            st.session_state.download_queue = [] # Clear queue
                        st.success("Bulk download queue processed (mock).")


        with prem_col2:
            with st.container(border=True):
                st.markdown(f"<h3 style='color:{PURPLE_ACCENT_COLOR};'>Video Transcript Generator (TXT)</h3>", unsafe_allow_html=True)
                uploaded_video = st.file_uploader("Upload a downloaded Reel (.mp4) for transcription:", type=["mp4"])
                if uploaded_video is not None:
                    if st.button("Generate Transcript", key="generate_transcript"):
                        # Save temp file to pass to mock function
                        with open(uploaded_video.name, "wb") as f:
                            f.write(uploaded_video.getbuffer())

                        with st.spinner("Generating transcript..."):
                            success, message, transcript_file = mock_generate_transcript(uploaded_video.name)
                        if success:
                            st.success(message)
                            with open(transcript_file, "rb") as fp:
                                st.download_button(
                                    label="Download Transcript",
                                    data=fp,
                                    file_name=transcript_file,
                                    mime="text/plain"
                                )
                        else:
                            st.error(message)
    else:
        st.info("Upgrade to Premium to unlock Bulk Downloads and Video Transcripts!")

# --- Footer ---
st.markdown("---")
st.markdown(
    f"<p style='text-align:center; color:{TEXT_COLOR_LIGHT};'>© 2025 ReelDownloader Pro. For educational purposes only.</p>",
    unsafe_allow_html=True
)


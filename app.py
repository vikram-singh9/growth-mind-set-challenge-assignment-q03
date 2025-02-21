import streamlit as st
import base64
from PIL import Image
import io

def set_theme():
    st.markdown("""
    <style>
    .stApp {
        transition: background-color 0.5s ease;
    }
    .light-theme {
        background-color: #f8f9fa;
        color: #212529;
    }
    .dark-theme {
        background-color: #1E1E1E;
        color: #ffffff;
    }
    .big-font {
        font-size:22px !important;
        font-weight: bold;
        text-align: center;
    }
    .user-card {
        padding: 20px;
        border-radius: 12px;
        margin: 20px 0;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    .light-theme .user-card {
        background-color: #ffffff;
    }
    .dark-theme .user-card {
        background-color: #2E2E2E;
    }
    .user-image {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        object-fit: cover;
        display: block;
        margin: 0 auto 15px auto;
        border: 3px solid #1E88E5;
    }
    .highlight {
        color: #1E88E5;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Growth Mindset Challenge", layout="wide")
    set_theme()

    if 'theme' not in st.session_state:
        st.session_state.theme = 'light'
    if 'user_data' not in st.session_state:
        st.session_state.user_data = None

    st.title("🌱 Growth Mindset Challenge")
    st.markdown('<p class="big-font">Welcome! Share your journey and aspirations with us.</p>', unsafe_allow_html=True)
    
    st.sidebar.header("👤 Enter Your Details")
    name = st.sidebar.text_input("Name")
    bio = st.sidebar.text_area("Describe yourself in a few words")
    hobby = st.sidebar.text_input("Your Dream Goal")
    uploaded_file = st.sidebar.file_uploader("Upload Your Image", type=["jpg", "png"])

    if st.sidebar.button("Submit ✅"):
        if name and bio and hobby:
            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                img_buffer = io.BytesIO()
                image.save(img_buffer, format="PNG")
                img_str = base64.b64encode(img_buffer.getvalue()).decode()
                
                st.session_state.user_data = {
                    'name': name,
                    'bio': bio,
                    'hobby': hobby,
                    'image': img_str
                }
            else:
                st.warning("⚠️ Please upload an image.")
        else:
            st.warning("⚠️ All fields are required!")

    if st.session_state.user_data:
        st.markdown(f"""
        <div class="user-card">
            <img class="user-image" src="data:image/png;base64,{st.session_state.user_data['image']}">
            <h2 class="highlight">{st.session_state.user_data['name']}</h2>
            <p><em>{st.session_state.user_data['hobby']}</em></p>
            <p>{st.session_state.user_data['bio']}</p>
        </div>
        """, unsafe_allow_html=True)

    st.header("🚀 What is a Growth Mindset?")
    st.write("""
    A **growth mindset** is the belief that abilities can be developed through dedication, learning, and persistence.
    This mindset helps you embrace challenges and view failures as opportunities to improve.
    """)
    
    st.header("🌟 Why Develop a Growth Mindset?")
    reasons = [
        "✅ Embrace challenges as learning opportunities",
        "✅ Learn from mistakes and failures",
        "✅ Stay persistent even during difficulties",
        "✅ Celebrate efforts, not just results",
        "✅ Keep an open mind and adapt when needed"
    ]
    st.markdown("\n".join(reasons))
    
    st.header("📌 How to Practice a Growth Mindset?")
    practices = [
        "🎯 Set learning goals beyond just achievements",
        "📝 Reflect on challenges and successes",
        "💡 Seek feedback and use it for improvement",
        "😊 Stay positive and encourage others"
    ]
    st.markdown("\n".join(practices))
    
    st.markdown("""
    🌱 **Your journey is about continuous growth, not just proving yourself.** Keep pushing forward and improving! 🚀
    """)

if __name__ == "__main__":
    main()

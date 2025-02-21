import streamlit as st
import base64
from PIL import Image
import io

def set_theme():
    # Define custom CSS for light and dark themes
    st.markdown("""
    <style>
    .stApp {
        transition: background-color 0.5s ease;
    }
    .light-theme {
        background-color: #ffffff;
        color: #000000;
    }
    .dark-theme {
        background-color: #1E1E1E;
        color: #ffffff;
    }
    .big-font {
        font-size:20px !important;
    }
    .user-card {
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .light-theme .user-card {
        background-color: #f0f2f6;
    }
    .dark-theme .user-card {
        background-color: #2E2E2E;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Growth Mindset Challenge", layout="wide")
    set_theme()

    # Initialize session state
    if 'theme' not in st.session_state:
        st.session_state.theme = 'light'
    if 'user_data' not in st.session_state:
        st.session_state.user_data = None


    st.title("Growth Mindset Challenge")
    st.markdown('<p class="big-font">Welcome to the Growth Mindset Challenge! Share your journey and aspirations.</p>', unsafe_allow_html=True)

    # Sidebar for user input
    st.sidebar.header("Enter Your Details")
    
    name = st.sidebar.text_input("Name")
    bio = st.sidebar.text_area("Describe about you in a descriptive way")
    hobby = st.sidebar.text_input("What do you want to become?")
    uploaded_file = st.sidebar.file_uploader("Choose an image...", type="jpg")

    if st.sidebar.button("Submit"):
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
                st.warning("Please upload an image.")
        else:
            st.warning("Please fill in all fields.")

    # Display user data if available
    if st.session_state.user_data:
        st.markdown(f"""
        <div class="user-card">
            <img src="data:image/png;base64,{st.session_state.user_data['image']}" style="
            width: 150px;
            height: 150px;
            border-radius: 50%;
            object-fit: cover;
            display: block;
            margin: 0 auto 20px auto;">
            <h2 style="text-align: center; color: {'#1E88E5' if st.session_state.theme == 'light' else '#64B5F6'};">
            {st.session_state.user_data['name']}
            </h2>
            <p style="text-align: center;"><em>{st.session_state.user_data['hobby']}</em></p>
            <p style="text-align: center;">{st.session_state.user_data['bio']}</p>
        </div>
        """, unsafe_allow_html=True)

    # Growth Mindset Information
    st.header("What is a Growth Mindset?")
    st.write("""
    A growth mindset is the belief that your abilities and intelligence can be developed through hard work, 
    perseverance, and learning from your mistakes. This concept was popularized by psychologist Carol Dweck, 
    and it challenges the notion that our skills are fixed from the start. Instead, it reminds us that every 
    challenge is an opportunity to learn and improve.
    """)

    st.header("Why Adopt a Growth Mindset?")
    reasons = [
        "Embrace Challenges: View obstacles as opportunities to learn rather than as setbacks.",
        "Learn from Mistakes: Understand that making mistakes is a natural part of learning. Each error is a chance to improve.",
        "Persist Through Difficulties: Stay determined, even when things get tough. Hard work and persistence can lead to growth.",
        "Celebrate Effort: Recognize and reward the effort you put into learning, not just the final result.",
        "Keep an Open Mind: Stay curious and be willing to adapt your approach based on what you learn."
    ]
    for reason in reasons:
        st.markdown(f"- {reason}")

    st.header("How Can You Practice a Growth Mindset?")
    practices = [
        "Set Learning Goals: Instead of only focusing on grades, set goals that help you develop new skills and understand complex concepts.",
        "Reflect on Your Learning: Regularly take time to think about what you've learned from both your successes and your challenges.",
        "Seek Feedback: Embrace constructive criticism and use it as a tool for improvement.",
        "Stay Positive: Believe in your capacity to grow, and encourage your peers to do the same."
    ]
    for practice in practices:
        st.markdown(f"- {practice}")

    st.markdown("""
    Remember, your journey in education isn't just about proving your intelligence—it's about developing it. 
    By adopting a growth mindset, you empower yourself to overcome challenges, innovate, and continuously improve. 
    Every step you take, whether forward or backward, is part of the learning process. Embrace your potential and 
    never stop striving to be better.
    """)

    # Close the theme div
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()

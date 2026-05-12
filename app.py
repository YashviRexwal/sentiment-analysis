import streamlit as st 

# Add custom CSS for styled title box
st.markdown("""
    <style>
    .title-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .title-box h1 {
        color: white;
        margin: 0;
        font-size: 2.5em;  
    }
    </style>
    <div class="title-box">
        <h1>🎯 Sentiment Analysis Dashboard 🎯</h1>
    </div>
""", unsafe_allow_html=True)

st.markdown("### 💬 **Enter text to analyze sentiment**")

user_input = st.text_area("Enter your text")

if st.button("🔍 Analyze"):
    st.write ("Analyzing...")

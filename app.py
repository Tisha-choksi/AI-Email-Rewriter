import streamlit as st
from backend.email_rewriter import EmailRewriter, EmailConfig
import difflib
import markdown

# Page config
st.set_page_config(
    page_title="AI Email Rewriter",
    page_icon="✉️",
    layout="wide"
)

# Add custom CSS
st.markdown("""
<style>
    .stTextArea textarea {
        font-size: 16px !important;
    }
    .output-container {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
    }
    .diff-add {
        background-color: #e6ffe6;
        color: #006400;
    }
    .diff-remove {
        background-color: #ffe6e6;
        color: #640000;
        text-decoration: line-through;
    }
    .main-header {
        text-align: center;
        padding: 2rem 0;
    }
    .feature-box {
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

def generate_diff(original: str, rewritten: str) -> str:
    """Generate HTML diff between original and rewritten text."""
    diff = difflib.ndiff(original.splitlines(), rewritten.splitlines())
    html_diff = []
    for line in diff:
        if line.startswith('+ '):
            html_diff.append(f'<div class="diff-add">{line[2:]}</div>')
        elif line.startswith('- '):
            html_diff.append(f'<div class="diff-remove">{line[2:]}</div>')
        elif line.startswith('  '):
            html_diff.append(f'<div>{line[2:]}</div>')
    return ''.join(html_diff)

def main():
    # Title and description
    st.markdown('<div class="main-header">', unsafe_allow_html=True)
    st.title("✨ AI Email Rewriter")
    st.markdown("Transform your emails with AI-powered tone and clarity enhancement")
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Sidebar configuration
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # API Key input
        api_key = st.text_input("Enter your OpenAI API key", type="password")
        
        # Initialize EmailRewriter if API key is provided
        if api_key:
            rewriter = EmailRewriter(api_key)
            if not rewriter.validate_api_key():
                st.error("Invalid API key. Please check and try again.")
                api_key = None
            
        # Model selection
        model = st.selectbox(
            "Select GPT Model",
            ["gpt-3.5-turbo", "gpt-4"],
            help="GPT-4 provides better results but costs more"
        )
        
        # Show diff option
        show_diff = st.checkbox("Show changes", value=False)
        
        st.markdown("---")
        st.markdown("### 📝 How to use")
        st.markdown("""
        1. Enter your OpenAI API key
        2. Paste your email text
        3. Choose desired tone
        4. Select GPT model
        5. Click 'Rewrite Email'
        """)
        
        st.markdown("---")
        st.markdown("### 🚀 Deployment")
        st.markdown("""
        This app can be deployed on:
        - Streamlit Cloud
        - Vercel
        - Your own server
        """)
    
    # Main content
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        st.subheader("Original Email")
        email_input = st.text_area(
            "Paste your email here",
            height=200,
            placeholder="Dear team,\n\nI wanted to follow up on..."
        )
        
        tone = st.selectbox(
            "Select Tone",
            ["Professional", "Friendly", "Persuasive", "Apologetic"]
        )
        
        # Rewrite button
        if st.button("✨ Rewrite Email", type="primary", disabled=not api_key):
            if not api_key:
                st.warning("Please enter your OpenAI API key in the sidebar.")
            elif not email_input.strip():
                st.warning("Please enter an email to rewrite.")
            else:
                with st.spinner("Rewriting your email..."):
                    config = EmailConfig(
                        tone=tone,
                        model=model,
                        temperature=0.7,
                        max_tokens=1000
                    )
                    result = rewriter.rewrite_email(email_input, config)
                    
                    if result["status"] == "success":
                        st.session_state.original = email_input
                        st.session_state.rewritten = result["rewritten_email"]
                    else:
                        st.error(f"Error: {result['error']}")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="feature-box">', unsafe_allow_html=True)
        st.subheader("Rewritten Email")
        if 'rewritten' in st.session_state:
            if show_diff:
                st.markdown("### Changes:")
                diff_html = generate_diff(st.session_state.original, st.session_state.rewritten)
                st.markdown(diff_html, unsafe_allow_html=True)
            else:
                st.markdown(st.session_state.rewritten)
            
            # Copy button
            if st.button("📋 Copy to Clipboard"):
                st.write("Copied to clipboard!")
                st.session_state.clipboard = st.session_state.rewritten
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center">
        Made with ❤️ using Streamlit and OpenAI GPT
        <br>
        <small>Deploy this app on Streamlit Cloud or Vercel for production use</small>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

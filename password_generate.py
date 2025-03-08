import streamlit as st
import random
import string

# Function to generate a password
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if not characters:
        return "Error: No character set selected!"
    
    return "".join(random.choice(characters) for _ in range(length))

# Custom Styling
st.markdown(
    """
    <style>
        .password-box {
            font-size: 24px;
            font-weight: bold;
            color: #ff4b4b;
            background: #ffffff;
            padding: 10px;
            border-radius: 10px;
            text-align: center;
            margin-top: 20px;
            border: 2px solid #ff4b4b;
            display: inline-block;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# UI Components
st.title("🔑 Stylish Password Generator")
st.write("Generate a **secure** and **random** password instantly!")

# Layout using columns
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    length = st.slider("📏 Select Password Length", min_value=6, max_value=32, value=12)
    use_digits = st.checkbox("🔢 Include Digits")
    use_special = st.checkbox("🔣 Include Special Characters")

    # Generate Password Button
    if st.button("🚀 Generate Password"):
        password = generate_password(length, use_digits, use_special)

        if "Error" in password:
            st.error(password)
        else:
            st.markdown(f"<div class='password-box'>{password}</div>", unsafe_allow_html=True)
            
            # Copy to clipboard button
            st.code(password, language="")

st.write("---")
st.markdown("👨‍💻 Built with ❤️ by [Abdul Waheed](https://github.com/AI-Balushi)")


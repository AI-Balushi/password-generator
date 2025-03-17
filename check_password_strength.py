import re  # Importing the regular expressions module
import streamlit as st  # Importing Streamlit for the web interface

# Function to check password strength
def check_password_strength(password):
    score = 0  # Initialize password strength score
    feedback = []  # List to store feedback messages

    # Check if password length is at least 8 characters
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    # Check for both uppercase and lowercase letters
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Include both uppercase and lowercase letters.")

    # Check if the password contains at least one digit (0-9)
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌ Add at least one number (0-9).")

    # Check if the password contains at least one special character (!@#$%^&*)
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("❌ Include at least one special character (!@#$%^&*).")

    # Determine password strength based on the score
    if score == 4:
        feedback.append("✅ Strong Password!")  # Strong password
    elif score == 3:
        feedback.append("⚠️ Moderate Password - Consider adding more security features.")  # Moderate password
    else:
        feedback.append("❌ Weak Password - Improve it using the suggestions above.")  # Weak password

    return feedback  # Return feedback messages

# Streamlit UI
st.title("🔐 Password Strength Checker")  # App title

# Input field for password (hides text for security)
password = st.text_input("Enter your password", type="password")

# Check password strength only if input is provided
if password:
    feedback = check_password_strength(password)  # Call function
    for message in feedback:  # Display each feedback message
        st.write(message)

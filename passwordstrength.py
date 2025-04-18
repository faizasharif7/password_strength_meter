import re
import streamlit as st

#Page styling
st.set_page_config(
    page_title="Password Strength Checker",
    page_icon="🔑",
    layout="centered",
)

#Custom CSS
st.markdown(
    """
    <style>
        .main {text-align: center;}
        .stTextInput {width: 60% !important; margin: auto;}
        .stButton button {
            width: 100%;
            background-color: green;
            color: white;
            font-size: 18px;
            border-radius: 8px;
        }
        .stButton button:hover {
            background-color: red;
            color: white;
        } 
    </style>
    """,
    unsafe_allow_html=True,
)

#Page title and description
st.title("🔐 Password Strength Generator")
st.write("Enter your password below to check its security level. ")

#Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❗ Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❗ Password should include both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❗ Password should include at least one number (0-9).")

    if re.search(r"[!@#$%^&]", password):
        score += 1
    else:
        feedback.append("❗ Include at least one special character (!@#$%^&).")

    # Display password strength result
    if score == 4:
        st.success("✅ Strong Password - Your password is secure.")
    elif score == 3:
        st.info("⚠️ Moderate Password - Consider adding more features for better security.")
    else:
        st.error("⚠️ Weak Password - Follow the suggestions below to strengthen it.")

#Feedback section
    if feedback:
        with st.expander("⚠️ Improve Your Password"):
            for item in feedback:
                st.write(item)

#Password input
password = st.text_input(
    "Enter Your Password:", type="password", help="Ensure your password is strong 🔒"
)

#Centered button using columns
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if st.button("Check Strength"):
        if password:
            check_password_strength(password)
        else:
            st.warning("⚠️ Please enter a password first!")


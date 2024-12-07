import streamlit as st

def show_forgot_password_page():
    st.markdown('<h3 style="font-size: 2rem; color: teal;">Forgot Password</h3>', unsafe_allow_html=True)

    email = st.text_input("Enter your email address")

    if st.button("Send Reset Link"):
    
        st.write("A password reset link has been sent to your email.")
        st.session_state["page"] = "login"
        st.rerun()
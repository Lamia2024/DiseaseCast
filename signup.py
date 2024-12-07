import streamlit as st

def show_signup_page():
    st.markdown('<h3 style="font-size: 2rem; color: teal;">Sign up for DiseaseCast</h3>', unsafe_allow_html=True)

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    phone_number = st.text_input("Phone Number")
    password = st.text_input("Password", type="password")
    confirm_password = st.text_input("Confirm Password", type="password")
    
    if st.button("Sign Up"):
        if password == confirm_password:
            st.write("Account created successfully!")
            st.balloons()
            st.session_state["page"] = "login"  
            st.rerun()
        else:
            st.error("Passwords do not match. Please try again.")
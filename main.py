import streamlit as st
from login import show_login_page
from signup import show_signup_page
from forgotpass import show_forgot_password_page
from home import show_home_page
from about import show_about_page
from diabetic import show_diabetics_prediction_page
from logout import show_logout_button
def main():
    
    if "page" not in st.session_state:
        st.session_state.page = "login"

    if st.session_state.page == "login":
        show_login_page()
    elif st.session_state.page == "signup":
        show_signup_page()
    elif st.session_state.page == "forgot_password":
        show_forgot_password_page() 
    elif st.session_state.page == "about":
        show_about_page()
    elif st.session_state.page == "home":
        show_home_page() 
    elif st.session_state["page"] == "diabetic":
        show_diabetics_prediction_page()
    elif st.session_state["page"] == "logout":
        show_login_page()





if __name__ == "__main__":
    main()
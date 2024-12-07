import streamlit as st

def show_logout_button():
    
    if st.button("Logout"):
        
        st.session_state.clear()

    
        st.session_state["page"] = "login"
        st.rerun()

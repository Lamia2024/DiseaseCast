import streamlit as st
def show_login_page():
    st.markdown('<h1 style="font-size: 3.5rem; color: teal;">DiseaseCast</h1>', unsafe_allow_html=True)
    st.subheader("Log in to DiseaseCast")

    username = st.text_input("Email or Phone")
    password = st.text_input("Password", type="password")

    col1, col2 = st.columns([3, 1])
    
    with col1:
        if st.button("Log In"):
            st.session_state["page"] = "home"
            st.rerun()
    
    with col2:
        if st.button("Forgotten password?"):
            st.session_state["page"] = "forgot_password"
            st.rerun()
    st.markdown("---")
    col3,col4,col5 = st.columns([1, 1,1])
    with col4:
        if st.button("Create New Account"):
           st.session_state["page"] = "signup"
           st.rerun()
    st.markdown('<p1 style="text-align: center; font-size: 1.00rem; color: red;">"Explore personalized health predictions and expert tips to guide you towards a balanced, healthier lifestyle with proactive choices."</p1>', unsafe_allow_html=True)

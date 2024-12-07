import streamlit as st
from streamlit_option_menu import option_menu



def show_about_page():
    st.title("Welcome to the Health Prediction App X")
    st.write("Explore various health prediction tools and resources.")
    
    with st.sidebar:
        selected = option_menu(
            menu_title="Navigation",  
            options=["Home", "Diabetics Prediction", "Heart Disease Prediction", "About", "Logout"],
            icons=["house-fill", "activity", "heart", "info-circle-fill", "box-arrow-right"],
            menu_icon="cast",
            default_index=0,
            styles={
                "container": {"padding": "5!important", "background-color": "black"},
                "icon": {"color": "white", "font-size": "23px"},
                "nav-link": {"color": "white", "font-size": "20px", "text-align": "left", "margin": "5px", "--hover-color": "blue"},
                "nav-link-selected": {"background-color": "#02ab21"},
            }
        )
        st.title("About")
        st.write("Learn more about this application and how it can help you.")
        
        
    if selected == "About":
            
        st.session_state["page"] = "about"
        #st.title("About")
        #st.write("Learn more about this application and how it can help you.")
        
    elif selected == "Home":
        st.session_state["page"] = "home"
        st.title("Welcome to the Health Prediction App again")
        st.write("Explore various health prediction tools and resources.")
        st.rerun()
            
        

    


# Call the function to render the About page
#show_about_page()

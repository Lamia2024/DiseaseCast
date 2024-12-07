import streamlit as st
from streamlit_option_menu import option_menu
import openai

# Set your OpenAI API key (ensure it's valid and secure)
openai.api_key = "sk-6s-qXvBwc8_nmlAOGoa4jtTMI1MpuwTxg9x-er_AZTT3BlbkFJzqc7jwmI7oXpJ_ZuZnjpex4eR60okl_5Xc8kgsC-0A"
# Initialize session state for chat history if not already set
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Function to generate chatbot response using OpenAI's GPT
def generate_response(user_input):
    try:
        # Use gpt-3.5-turbo instead of gpt-4
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Changed to gpt-3.5-turbo
            messages=[
                {"role": "system", "content": "You are a helpful health assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        st.error(f"Error generating response: {str(e)}")
        return "Error generating response. Please try again later."

# Function to render the home page
def show_home_page():
    st.title("Welcome to the Health Prediction App")
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


  
     # Page content based on selection
    if selected == "Home":
        st.session_state["page"] = "home"
        st.title("Welcome to the Health Prediction App again")
        st.write("Explore various health prediction tools and resources.")
        
          # Chatbot interface
    st.subheader("You can ask from our Chatbot")
    user_input = st.text_input("Ask me anything about health:")

    # Process user input and generate response
    if user_input:
        st.session_state.chat_history.append(f"User: {user_input}")
        
        # Generate chatbot response using OpenAI API
        response = generate_response(user_input)
        st.session_state.chat_history.append(f"Bot: {response}")

    # Display chat history
    if st.session_state.chat_history:
        st.write("### Chat History")
        for chat in st.session_state.chat_history:
            st.write(chat)
    
    
    elif selected == "Diabetics Prediction":
        st.session_state["page"] = "diabetic"
        st.rerun()

    elif selected == "Heart Disease Prediction":
        st.session_state["page"] = "heart"
        st.title("Heart Disease Prediction")
        st.write("Use our tool to predict the likelihood of heart disease.")

    elif selected == "About":
        st.session_state["page"] = "about"
        st.title("About")
        st.write("Learn more about this application and how it can help you.")
        st.rerun()

    elif selected == "Logout":
        st.session_state["page"] = "login"
        st.title("Logout")
        st.write("You have been logged out successfully.")
        st.rerun()

    
    
# Function to render the Diabetics Prediction page
def show_diabetics_prediction_page():
    st.title("Diabetics Prediction")
    st.write("Use our tool to predict the likelihood of diabetes.")

# Function to render the Heart Disease Prediction page
def show_heart_disease_prediction_page():
    st.title("Heart Disease Prediction")
    st.write("Use our tool to predict the likelihood of heart disease.")

# Function to render the About page
def show_about_page():
    st.title("About")
    st.write("Learn more about this application and how it can help you.")

# Function to handle navigation and rendering of different pages


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
import streamlit as st
from fpdf import FPDF
from streamlit_option_menu import option_menu

# Function to generate PDF report with prediction result
def dict_to_pdf(data, result, pdf_file):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_text_color(0, 102, 204)  # Set title color to dark blue (RGB: 0, 102, 204)
    pdf.set_font("Arial", size=20, style='B')
    pdf.cell(0, 10, txt="Diseasecast", ln=True, align='C')
    pdf.ln(1)  # Space below title

    # Subtitle
    pdf.set_font("Arial", size=16, style='B')
    pdf.cell(0, 10, txt="Diabetics Prediction Result", ln=True, align='C')
    pdf.ln(1)  # Space below subtitle

    pdf.set_font("Arial", size=10)
    pdf.cell(0, 10, txt="Website: www.diseasecast.com", ln=True, align='C')
    pdf.cell(0, 10, txt="Email: contact@diseasecast.com", ln=True, align='C')
    pdf.cell(0, 10, txt="Phone: +1 234 567 890", ln=True, align='C')
    pdf.ln(2)
    
    # Set font for the data
    pdf.set_font("Arial", size=12)
    pdf.set_text_color(0, 0, 0)  # Black text

    # Add user data to the PDF
    for idx, (key, value) in enumerate(data.items()):
        if idx % 2 == 0:
            pdf.set_fill_color(0, 255, 255)  # Alternate row color
        else:
            pdf.set_fill_color(255, 255, 255)  # White background

        pdf.cell(180, 10, txt=f"{key}: {value}", border=0, ln=True, align='L', fill=True)

    pdf.ln(20)
    pdf.set_font("Arial", size=10, style='B')
    pdf.cell(0, 10, txt="About Diseasecast", ln=True, align='L')
    pdf.set_font("Arial", size=8)
    pdf.multi_cell(0, 10, txt=(
        "Diseasecast is a healthcare prediction platform that leverages machine learning to help "
        "individuals predict and manage their health conditions. With accurate models and an easy-to-use "
        "interface, we strive to provide a reliable and accessible tool for both patients and healthcare providers. "
        "Visit our website for more details and updates on our services."
    ))

    # Add space before footer
    pdf.ln(10)

    # Footer with thank you note
    pdf.set_y(-40)
    pdf.set_font("Arial", size=10, style='I')
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 10, txt="Thank you for using Diseasecast. Stay healthy!", ln=True, align='C')

    pdf.output(pdf_file)

# Function to perform KNN prediction
def perform_prediction(X_train, y_train, sc_X, user_data):
    # Convert user data to array and scale it
    user_data_array = np.array([[ 
        user_data['Pregnancies'],
        user_data['Glucose'],
        user_data['Blood Pressure'],
        user_data['Skin Thickness'],
        user_data['Insulin'],
        user_data['BMI'],
        user_data['Diabetics Pedigree Function'],
        user_data['Age']
    ]])

    # Scale user data
    userdata_scaled = sc_X.transform(user_data_array)

    # KNN classifier
    classifier = KNeighborsClassifier(n_neighbors=11, p=2, metric='euclidean')
    classifier.fit(X_train, y_train)
    prediction = classifier.predict(userdata_scaled)

    # Return prediction result
    return 'Negative' if prediction[0] == 0 else 'Positive'

# Function to change field color based on input
def change_field_color(value):
    if value:
        return "lightblue"  # If the field has input, return blue
    return "lightcoral"   # If empty, return red

# Function to display the Diabetics Prediction Page
# Function to display the Diabetics Prediction Page
# Function to display the Diabetics Prediction Page
def show_diabetics_prediction_page():
    # Sidebar navigation menu
    with st.sidebar:
        selected = option_menu(
            menu_title="DEASEASE",
            options=["Home", "Diabetics Prediction", "Heart Disease Prediction", "About", "Logout"],
            icons=["house-fill", "activity", "heart", "info-circle-fill", "box-arrow-right"],
            menu_icon="cast",
            #menu_tittle_color="red",
            default_index=1,
            styles={
                "container": {"padding": "5!important", "background-color": "black"},
                "icon": {"color": "white", "font-size": "23px"},
                "nav-link": {
                    "color": "white",
                    "font-size": "20px",
                    "text-align": "left",
                    "margin": "0px",
                    "--hover-color": "blue"
                },
                "nav-link-selected": {"background-color": "#02ab21"},
            }
        )
    
    # Handle navigation based on the selected option
    if selected == "Home":
        st.session_state["page"] = "home"
        st.rerun()
    elif selected == "Heart Disease Prediction":
        st.session_state["page"] = "heart_disease"
        st.rerun()
    elif selected == "About":
        st.session_state["page"] = "about"
        st.rerun()
    elif selected == "Logout":
        st.session_state["page"] = "login"
        st.rerun()
        st.write("Thank you for using DiseaseCast!")

    data = pd.read_csv('https://raw.githubusercontent.com/azaz6216/Diabforecast/main/diabetes.csv')

    nonzero = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']
    for feature in nonzero:
        data[feature] = data[feature].replace(0, np.nan)
        mean = int(data[feature].mean(skipna=True))
        data[feature] = data[feature].replace(np.nan, mean)

    # Enhanced title and subtitle
    st.markdown('<h1 style="text-align: center; font-size: 3.5rem;color:teal;">DiseaseCast</h1>', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: #2c3e50;'>Predict Diabetes</h2>", unsafe_allow_html=True)

    X = data.iloc[:, 0:8]
    y = data.iloc[:, 8]
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0, test_size=0.2)

    sc_X = StandardScaler()
    X_train = sc_X.fit_transform(X_train)
    X_test = sc_X.transform(X_test)

    # Add a light sky blue background for the entire input information form
    st.markdown(
        """
        <style>
            .input-container {
                background-color: lightblue;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }
        </style>
        """, unsafe_allow_html=True
    )

    with st.form(key='input_form'):
        st.markdown('<div class="input-container">', unsafe_allow_html=True)  # Opening div with light sky blue background
        st.title('Input all information')

        # Columns layout for input fields
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            name = st.text_input('Name', placeholder="Enter your name")
            gender = st.selectbox('Gender', ['Male', 'Female', 'Others'])
            age = st.number_input('Age', step=1, min_value=0, placeholder="Enter your age")

        with col2:
            pregnancies = st.number_input('Pregnancies', step=1, min_value=0)
            glucose = st.number_input('Glucose', step=1, min_value=0)
            bp = st.number_input('Blood Pressure', step=1, min_value=0)

        with col3:
            skinthickness = st.number_input('Skin Thickness', step=1, min_value=0)
            insulin = st.number_input('Insulin', step=1, min_value=0)
            bmi = st.number_input('BMI', min_value=0.0)

        with col4:
            dpf = st.number_input('Diabetics Pedigree Function', min_value=0.0)

        submit_button = st.form_submit_button(label='Submit', help="Click to submit your information")
        st.markdown('</div>', unsafe_allow_html=True)  # Closing div

    if submit_button:
        # Collect user data
        user_data = {
            'Name': name,
            'Gender': gender,
            'Age': age,
            'Pregnancies': pregnancies,
            'Glucose': glucose,
            'Blood Pressure': bp,
            'Skin Thickness': skinthickness,
            'Insulin': insulin,
            'BMI': bmi,
            'Diabetics Pedigree Function': dpf,
        }

        # Change field colors based on user input
        field_colors = {
            'name': change_field_color(name),
            'age': change_field_color(age),
            'pregnancies': change_field_color(pregnancies),
            'glucose': change_field_color(glucose),
            'bp': change_field_color(bp),
            'skinthickness': change_field_color(skinthickness),
            'insulin': change_field_color(insulin),
            'bmi': change_field_color(bmi),
            'dpf': change_field_color(dpf)
        }

        # Update the field colors dynamically
        for field, color in field_colors.items():
            st.markdown(f"""<style>
                input[name='{field}'] {{
                    background-color: {color} !important;
                }}
            </style>""", unsafe_allow_html=True)

        # Make predictions
        knn_result = perform_prediction(X_train, y_train, sc_X, user_data)

        user_data_result = {
            'Name': name,
            'Gender': gender,
            'Age': age,
            'Pregnancies': pregnancies,
            'Glucose': glucose,
            'Blood Pressure': bp,
            'Skin Thickness': skinthickness,
            'Insulin': insulin,
            'BMI': bmi,
            'Diabetics Pedigree Function': dpf,
            'Result': knn_result
        }

        pdf_file = f"{name}_diseasecast_report.pdf"
        dict_to_pdf(user_data_result, knn_result, pdf_file)

        # Displaying the result with enhanced formatting
        st.markdown("---")
        st.markdown(f"<h3 style='text-align: center;'>Prediction Result: <span style='color: {'green' if knn_result == 'Positive' else 'red'};'>{knn_result}</span></h3>", unsafe_allow_html=True)
        st.markdown("---")

        # Download button for the PDF report
        with open(pdf_file, "rb") as f:
            pdf_data = f.read()
            st.download_button(
                label="Download Report",
                data=pdf_data,
                file_name=pdf_file,
                mime="application/pdf"
            )

# Main function to run the app
def main():
    st.set_page_config(page_title="DiseaseCast", layout="wide")
    show_diabetics_prediction_page()
   
    

    
if __name__ == "__main__":
    

    main()
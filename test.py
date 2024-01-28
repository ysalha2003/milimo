# Imports
import streamlit as st
from streamlit_option_menu import option_menu

# Theme
theme_color = "#F63366"
st.set_page_config(page_title="M1 Limousine", page_icon="", layout="wide")

# Menu
with st.container():
    chosen = option_menu(
        menu_title="Main Menu",
        options=["Home", "Our Fleet", "Reservation", "Services", "Contact"],
        icons=["house", "car", "calendar-check", "gear", "envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
        styles={
            "container": {"padding": "0!important"},
            "icon": {"color": "orange"},
            "nav-link": {"--hover-color": theme_color},
            "nav-link-selected": {"background-color": theme_color},
        }
    )

# Page Content
if chosen == "Home":
    st.title("Welcome to M1 Limousine! Abdo")
    st.write("Luxury Vehicles for Every Occasion")
    st.image("logo.png")

elif chosen == "Our Fleet":
    st.header("Our Luxury Fleet")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("sedan.jpg")
        st.caption("Luxury Sedans")

    with col2:
        st.image("suv.jpg")
        st.caption("Premium SUVs")

    with col3:  
        st.image("limo.jpg")
        st.caption("Stretch Limousines")
       
    st.write("Modern, luxury vehicles for any occasion!")

elif chosen == "Reservation":
    st.header("Make a Reservation")
    with st.form("reservation_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email")
        pickup_date = st.date_input("Pickup Date")
        pickup_time = st.time_input("Pickup Time")
        pickup_location = st.text_input("Pickup Location")
        dropoff_location = st.text_input("Dropoff Location")
        special_requests = st.text_area("Special Requests")
        submit_button = st.form_submit_button("Submit Reservation")
        if submit_button:
            st.success("Thank you, your reservation request has been submitted.")

elif chosen == "Contact":
    st.header("Contact Us")
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        submit_button = st.form_submit_button("Send Message")
        if submit_button:
            st.info("Thank you for your message. We will get back to you soon.")

# Footer    
footer_template = """<p style="font-family:sans-serif; color:{color}; text-align:center;">
    Copyright {year} M1 Limousine</p>"""

st.markdown(footer_template.format(year=2024, color=theme_color), unsafe_allow_html=True)

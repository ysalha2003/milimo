import streamlit as st
import hydralit_components as hc

st.set_page_config(layout="wide")


# Menu definitions
menu_data = [
    {'label': 'Home'},
    {'label': 'Our Fleet'},
    {'label': 'Get Quote'},
    {'label': 'Contact'},
    {'label': 'Login'}
]

# Create navigation menu
menu_id = hc.nav_bar(
    menu_definition=menu_data,
    hide_streamlit_markers=False,
    sticky_nav=True,
    sticky_mode='pinned',
)

# Check if "Get Quote" menu item clicked
if menu_id == "Get Quote":
    # Booking form
    st.header("Limousine Booking Form")
    with st.form("booking_form"):
        # Add fields for first name and last name
        first_name = st.text_input("First Name")
        last_name = st.text_input("Last Name")

        # Add fields for email and phone number
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")

        pickup = st.text_input("Pickup Address")
        dropoff = st.text_input("Dropoff Address")
        passengers = st.number_input("Number of Passengers", 1, 6, 1)

        # You can add more fields as needed

        submit = st.form_submit_button("Submit")

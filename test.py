# Import the Streamlit library
import streamlit as st
from datetime import datetime

# Define test data for the limousine company
company_data = {
    "Company Name": "M1 Limousine, Inc.",
    "Services": "CHAUFFEUR SERVICE, LIMO SERVICE, TRANSPORTATION SERVICE",
    "Phone Number": "(224) 301-4623",
    "Location": "Chicago",
    "Website Designer": "Yaser Salha",
    "Full Name": "",
    "Email Address": "",
    "Pick-up Address": "",
    "Drop-off Address": "",
    "Number of Passengers": "0",  # Default value is "0"
    "Number of Bags": "0",  # Default value is "0"
}

# Define the main function for your Streamlit app
def main():
    # Use Streamlit's built-in features for navigation
    st.sidebar.title("M1 Limousine, Inc.")

    # Create horizontal tabs for navigation
    tabs = ["Home", "Services", "Get a Quote", "Contact"]
    selected_tab = st.sidebar.radio("Navigation", tabs)

    if selected_tab == "Home":
        home()
    elif selected_tab == "Services":
        services()
    elif selected_tab == "Get a Quote":
        get_quote()
    elif selected_tab == "Contact":
        contact()

# Define your page functions with enriched content
def home():
    st.title("Welcome to M1 Limousine, Inc.")
    st.markdown(f"Current Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    st.markdown("""
        M1 Limousine, Inc. is your premier chauffeur and limo service in Chicago. We provide top-notch transportation services to make your journey comfortable and luxurious.
    """)
    st.markdown(f"Designed by: {company_data['Website Designer']}")

def services():
    st.title("Our Services")
    st.markdown(f"We offer a wide range of services, including: {company_data['Services']}")

def get_quote():
    st.title("Get a Quote")

    # Input fields for customer details
    full_name = st.text_input("Full Name", value=company_data["Full Name"])
    email = st.text_input("Email Address", value=company_data["Email Address"])
    phone_number = st.text_input("Phone Number", value=company_data["Phone Number"])

    # Input fields for quote request
    st.subheader("Quote Request Details")
    pick_up_address = st.text_input("Pick-up Address", value=company_data["Pick-up Address"])
    drop_off_address = st.text_input("Drop-off Address", value=company_data["Drop-off Address"])
    num_passengers = st.number_input("Number of Passengers", value=int(company_data["Number of Passengers"]), min_value=0)
    num_bags = st.number_input("Number of Bags", value=int(company_data["Number of Bags"]), min_value=0)

    # Button to submit the quote request
    if st.button("Get a Quote"):
        # Validate the email format
        if not validate_email(email):
            st.error("Please enter a valid email address.")
        else:
            # Process submitted quote request
            st.success(f"Thank you, {full_name}! Your quote request has been received. We will contact you shortly with a quote.")

# Function to validate email format
def validate_email(email):
    import re
    # Regular expression pattern for basic email validation
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

def contact():
    st.title("Contact Us")
    # Display company details with contact information
    st.markdown(f"""
        For inquiries and reservations, please contact us:

        Company Name: {company_data["Company Name"]}
        Phone Number: {company_data["Phone Number"]}
        Location: {company_data["Location"]}
        Website Designer: {company_data["Website Designer"]}
    """)

# Run the Streamlit app
if __name__ == "__main__":
    main()

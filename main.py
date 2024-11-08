import streamlit as st
import pytz
import random
import string
from datetime import datetime

def timezone_checker():
    st.header("Timezone Checker")
    # Get the list of all available time zones
    timezones = pytz.all_timezones

    # User selects a timezone from the dropdown
    selected_timezone = st.selectbox("Select a Timezone", timezones)

    # Display the current time in the selected timezone
    if selected_timezone:
        tz = pytz.timezone(selected_timezone)
        current_time = datetime.now(tz)
        st.write(f"Current time in {selected_timezone}:")
        st.info(current_time.strftime("%Y-%m-%d %H:%M:%S"))

def password_generator():
    st.header("Password Generator")
    
    # User inputs for password length and inclusion of special characters
    length = st.slider("Select password length", min_value=8, max_value=32, value=12)
    include_uppercase = st.checkbox("Include Uppercase Letters")
    include_numbers = st.checkbox("Include Numbers")
    include_special = st.checkbox("Include Special Characters")

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ""
    digits = string.digits if include_numbers else ""
    special_chars = string.punctuation if include_special else ""

    # Combine the selected character sets
    all_characters = lowercase + uppercase + digits + special_chars

    # Generate the password
    if st.button("Generate Password"):
        if all_characters:
            password = ''.join(random.choice(all_characters) for _ in range(length))
            st.success(f"Generated Password: {password}")
        else:
            st.error("Please select at least one character set.")

def main():
    st.title("Control Panel Web App")

    with st.sidebar:
        options = ["Timezone Checker", "Password Generator"]
        selected_option = st.selectbox("Select a tool", options)

    if selected_option == "Timezone Checker":
        timezone_checker()
    elif selected_option == "Password Generator":
        password_generator()

if __name__ == "__main__":
    main()


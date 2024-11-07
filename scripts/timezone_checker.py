import streamlit as st

def timezone_checker():
    # ... Your timezone checker logic here ...

def password_generator():
    # ... Your password generator logic here ...

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
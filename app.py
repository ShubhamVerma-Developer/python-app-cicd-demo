import streamlit as st

def main():
    st.title('Admin Dashboard')

    # Create a sidebar
    st.sidebar.title('Navigation')
    selected_page = st.sidebar.radio('Select Page', ['Home', 'Analytics', 'Settings'])

    # Display different pages based on sidebar selection
    if selected_page == 'Home':
        st.write("Welcome to the Admin Dashboard.")
    elif selected_page == 'Analytics':
        st.write("Analytics Page - Under Construction.")
    elif selected_page == 'Settings':
        st.write("Settings Page - Under Construction.")

if __name__ == '__main__':
    main()

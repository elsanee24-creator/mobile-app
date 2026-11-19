import streamlit as st
import os

# Ensure clean environment settings without disabling SSL globally
# (Removed os.environ.setdefault("PYTHONHTTPSVERIFY", "0"))

st.set_page_config(
    page_title="Mobile App Dashboard",
    page_icon="📱",
    layout="wide"
)

def main():
    st.title("📱 Mobile App Dashboard")
    st.write("Welcome! Your application has been successfully updated and is running without SSL security bypass warnings.")

    # Sidebar
    st.sidebar.header("Navigation")
    option = st.sidebar.selectbox("Choose a section:", ["Home", "Settings", "Analytics"])

    if option == "Home":
        st.subheader("Home View")
        st.success("App is running smoothly with no errors!")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(label="Active Users", value="1,234", delta="+12%")
        with col2:
            st.metric(label="Server Status", value="Online", delta="Stable")
        with col3:
            st.metric(label="Response Time", value="45 ms", delta="-2ms")

    elif option == "Settings":
        st.subheader("Settings")
        st.text_input("API Endpoint", value="https://api.example.com")
        st.checkbox("Enable Notifications", value=True)
        if st.button("Save Settings"):
            st.success("Settings saved successfully!")

    elif option == "Analytics":
        st.subheader("Analytics Overview")
        st.line_chart([10, 25, 30, 45, 55, 60, 85])

if __name__ == "__main__":
    main()

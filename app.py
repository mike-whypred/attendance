import streamlit as st

# Streamlit app layout
def main():
    # Sidebar
    st.sidebar.header("Attendance System")
    
    # Sidebar text
    st.sidebar.text("Please Register")

    # Using markdown to create a clickable link that looks like a button
    url = "https://go.retable.io/projUiMsA4QTLtQuQN5w"
    button_html = f'<a href="{url}" target="_blank"><button style="color: black; background-color: #FF4B4B; border-radius: 10px; padding: 10px; cursor: pointer; border: none; width: 100%;">Register Attendance</button></a>'
    st.sidebar.markdown(button_html, unsafe_allow_html=True)

    
    
     # Creating columns for centering the image
    col1, col2, col3 = st.columns([1,2,1])

    # Displaying the image in the center column
    with col2:
        # Main panel
        st.title("Welcome to your Capstone Unit")
        st.write("This app is created by AI, use the button or the QR code, link will only work during class hours.")
        st.image('qrCode.png', caption="Scan this QR code", width=500)
   

if __name__ == "__main__":
    main()

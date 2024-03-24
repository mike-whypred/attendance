import streamlit as st

import requests






retable_key = st.secrets["RETABLE_KEY"]


# Streamlit app layout
def main():

    st.title("🚀 Class Attendance")

    st.write("Welcome students of DATA6000 please record your attendance here on this app each week, the app will only be available during class time. Thank you.")
    st.sidebar.title("📓 Register here")
    st.sidebar.image("study.png", caption="Study Hard!", use_column_width=True) 
    
    # Input fields in the sidebar
    full_name = st.sidebar.text_input("Full Name")
    sid = st.sidebar.text_input("SID")
    # Class input as a dropdown
    class_options = ["SYD1", "SYD3"]  # Add more class options as needed
    class_name = st.sidebar.selectbox("Class", class_options)
    class_date = st.sidebar.date_input("Class Date")
    record_button = st.sidebar.button("Record")
    #first_name = full_name.split()[0]
    if record_button:
        # Prepare the data payload
        payload = {
            "data": [
                {
                    "columns": [
                        {"column_id": "F3S58WD5nsKv45K8", "cell_value": full_name},
                        {"column_id": "oVaNOBXLtP7queZm", "cell_value": sid},
                        {"column_id": "q4PcKeDfiKBpicyo", "cell_value": class_name},
                        {"column_id": "iINv3MajS3WOhH5G", "cell_value": class_date.strftime("%d-%m-%Y")},
                        # Add additional columns here as needed
                    ]
                }
            ]
        }

        # Post request to the Retable API
        response = post_data_to_retable(payload)

        if response.status_code == 201:
            st.success(f"Thank you {full_name}, your attendance was recorded successfully.")
        else:
            st.error("Failed to record attendance. Please email your details to the lecturer")
            

def post_data_to_retable(payload):
    """Function to send POST request to the Retable API."""
    url = "https://api.retable.io/v1/public/retable/c6iQUuyvBcF8fZwa/data"
    headers = {
        "ApiKey": retable_key,
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response

if __name__ == "__main__":
    main()

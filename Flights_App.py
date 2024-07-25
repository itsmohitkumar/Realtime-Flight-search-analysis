import os
import datetime
import json
import logging
import streamlit as st
from dotenv import load_dotenv
import serpapi
from openai import OpenAI
from utils import load_config, get_flight_search_params, prepare_prompt, call_openai

# Load environment variables from .env file
load_dotenv()

# Load configuration from JSON file
config = load_config('config.json')

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Get API keys from environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
SERPAPI_API_KEY = os.getenv('SERPAPI_API_KEY')

if not OPENAI_API_KEY or not SERPAPI_API_KEY:
    logging.error("API keys are not set.")
    st.error("Both OPENAI_API_KEY and SERPAPI_API_KEY are required.")
    st.stop()

# Set up the OpenAI client
Client = OpenAI(api_key=OPENAI_API_KEY)

# Custom CSS to apply a background image
css_style = f"""
    <style>
    .stApp {{
        background-image: url('{config['custom_css']['background_image_url']}');
        background-size: cover;
        background-position: center;
    }}
    {"footer {{ display: none !important; }}" if config['custom_css']['hide_footer'] else ""}
    .css-1xv4j9c {{ /* Hide Streamlit's footer container */
        display: none !important;
    }}
    </style>
    """
st.markdown(css_style, unsafe_allow_html=True)

# Streamlit app layout with blurred background
st.markdown('<div class="blurred-background">', unsafe_allow_html=True)

st.title("✈️ Flight Search and Analysis")

# User inputs
departure_id = st.text_input("📍 Departure Airport Code (e.g., DEL)", value="DEL")
arrival_id = st.text_input("📍 Arrival Airport Code (e.g., BOM)", value="BOM")
flight_type = st.selectbox("🛫 Flight Type", ["One-Way", "Return"])
outbound_date = st.date_input("📅 Journey Date", min_value=datetime.date.today())
return_date = st.date_input("📅 Return Date", min_value=datetime.date.today()) if flight_type == "Return" else None
currency = st.selectbox("💱 Currency", config['flight_search']['currency_options'], index=0)

if st.button("🔍 Search Flights"):
    # Get current time and add 2 hours
    current_time = datetime.datetime.now()
    search_time = current_time + datetime.timedelta(hours=2)

    # Define parameters for the flight search
    search_params = get_flight_search_params(
        departure_id, arrival_id, outbound_date, return_date, search_time, currency, SERPAPI_API_KEY, config['flight_search']['engine']
    )

    try:
        # Perform the flight search
        search_response = serpapi.search(search_params)
        flight_data_dict = search_response.data

        # Convert flight data to JSON format
        flight_data_json = json.dumps(flight_data_dict, indent=4)

        # Prepare prompt
        prompt = prepare_prompt(flight_data_json)

        # Call the OpenAI API
        result = call_openai(Client, config['openai']['model'], config['openai']['temperature'], prompt)

        # Display the result
        st.write("Processed result from Chatbot:")
        st.write(result)

    except json.JSONDecodeError:
        st.error("Failed to decode the result as JSON.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
        logging.error(f"An error occurred: {e}")

st.markdown('</div>', unsafe_allow_html=True)

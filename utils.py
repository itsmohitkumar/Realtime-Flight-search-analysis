import json
import serpapi
from openai import OpenAI

def load_config(file_path):
    """Load configuration from a JSON file."""
    with open(file_path) as config_file:
        return json.load(config_file)

def get_flight_search_params(departure_id, arrival_id, outbound_date, return_date, search_time, currency, api_key, engine):
    """Define parameters for the flight search."""
    return {
        "engine": engine,
        "departure_id": departure_id,
        "arrival_id": arrival_id,
        "outbound_date": outbound_date.strftime('%Y-%m-%d'),
        "outbound_time": search_time.strftime('%H:%M'),
        "currency": currency,
        "hl": "en",
        "api_key": api_key,
        "return_date": return_date.strftime('%Y-%m-%d') if return_date else outbound_date.strftime('%Y-%m-%d')
    }

def prepare_prompt(flight_data_json):
    """Prepare the prompt for the OpenAI API."""
    return (
        "You have been provided with flight data in JSON format. Please analyze the data and provide a comprehensive response including the following details:\n\n"
        "### 1. **Flight Overview** 📊\n"
        "   - **Total Number of Flights**: Indicate the total number of flight options available based on the search criteria.\n"
        "   - **Flight Availability Insights**: Provide an overview of flight availability, such as any notable peaks or limitations in flight options.\n\n"
        "### 2. **Detailed Flight Comparison** 🔍\n"
        "   - **Price Analysis** 💵:\n"
        "     - **Price Range**: Specify the lowest, highest, and average prices for the flights.\n"
        "     - **Price Patterns**: Identify any patterns or anomalies in flight prices, such as significant price variations based on time or airline.\n\n"
        "   - **Duration Analysis** ⏱️:\n"
        "     - **Duration Range**: Provide the shortest, longest, and average flight durations.\n"
        "     - **Duration Patterns**: Highlight any patterns or anomalies in flight durations, such as longer layovers or unusually short flights.\n\n"
        "   - **Carbon Emissions Analysis** 🌍:\n"
        "     - **Emissions Range**: Specify the lowest, highest, and average carbon emissions for the flights.\n"
        "     - **Emissions Patterns**: Point out any patterns or anomalies in carbon emissions, including variations by airline or flight duration.\n\n"
        "### 3. **Flight Data in DataFrame Format** 📝\n"
        "   - **DataFrame Columns**:\n"
        "     - **Departure Airport**: Name and exact time of departure.\n"
        "     - **Arrival Airport**: Name and exact time of arrival.\n"
        "     - **Airline**: Name of the airline operating the flight.\n"
        "     - **Flight Duration**: Duration of the flight in minutes.\n"
        "     - **Price**: Price of the flight in the selected currency.\n"
        "     - **Carbon Emissions**: Carbon emissions for this flight.\n\n"
        "   - **Instructions**:\n"
        "     - Convert the flight data into a structured DataFrame format. Each flight should be represented as a row in the DataFrame with the columns specified above.\n"
        "     - Ensure that the DataFrame is well-organized and easy to read.\n"
        "     - Provide the DataFrame in a format that can be easily converted into a CSV or Excel file, including headers for each column.\n\n"
        "### 4. **Summary and Recommendations** 📋\n"
        "   - **Best Value Flights**: Identify flights that offer the best value considering price, duration, and emissions. Highlight any particularly good or bad options.\n"
        "   - **Cheapest Flight** 💸:\n"
        "     - **Details**: Provide details of the cheapest flight including the departure and arrival airports, airline, flight duration, price, and carbon emissions.\n"
        "     - **Cheapest Flight DataFrame**: Present the details of the cheapest flight in a structured DataFrame format with columns: Departure Airport, Departure Time, Arrival Airport, Arrival Time, Airline, Flight Duration, Price, Carbon Emissions.\n"
        "   - **Environmental Impact**: Summarize the environmental impact of the flights and recommend options that minimize carbon emissions.\n\n"
        "### 5. **Travel Hack and Tips** 🛠️✈️\n"
        "   - **Travel Tips**: Provide additional tips for choosing flights, such as the best times to book or advice on reducing carbon footprint.\n"
        "   - **Travel Hack** 🛠️: As a travel professional, offer a specific travel hack for this journey to help the traveler save money, reduce travel time, or enhance their travel experience.\n\n"
        "### 6. **Destination Suggestions** 🌎\n"
        "   - **Places to Visit**: Based on the arrival location, suggest a few must-visit places or attractions. Include a mix of popular tourist spots and hidden gems to enhance the traveler's experience.\n\n"
        "### Note:\n"
        "   - If no flight data is available, suggest checking for different dates or adjusting the search criteria to find available flight options.\n\n"
        f"Here is the flight data in JSON format:\n{flight_data_json}\n\n"
        "Please ensure that the data is presented in a DataFrame with the following columns: No., Departure Airport, Departure Time, Arrival Airport, Arrival Time, Airline, Flight Duration, Price. The output should be clear and easy to interpret, and the DataFrame should not include any code."
    )

def call_openai(client, model, temperature, prompt):
    """Call the OpenAI API with the provided prompt."""
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature
    )
    return response.choices[0].message.content

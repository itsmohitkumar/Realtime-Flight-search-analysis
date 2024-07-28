# Flight Search and Analysis

## Overview

This project is a web application for searching and analyzing flights using Streamlit, SerpAPI, and OpenAI. It allows users to search for flights, analyze flight data, and receive detailed insights on flight options.

## Features

- Search for flights based on departure and arrival airport codes.
- Analyze flight data including price, duration, and carbon emissions.
- Get a comprehensive comparison of flight options.
- Receive recommendations and travel tips.

## Installation

### Prerequisites

Ensure you have Python 3.7 or later installed.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/flight-search-analysis.git
cd flight-search-analysis
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Certainly! Here's an updated version of the README with instructions for generating the OpenAI and SerpApi keys:

---

### 4. Set Up Environment Variables

Create a `.env` file in the root directory and add your API keys:

```plaintext
OPENAI_API_KEY=your_openai_api_key_here
SERPAPI_API_KEY=your_serpapi_api_key_here
```

#### Generating API Keys

1. **OpenAI API Key:**
   - Visit the [OpenAI website](https://beta.openai.com/signup/) and sign up for an account if you don't already have one.
   - After logging in, navigate to the API section in your dashboard.
   - Create a new API key and copy it.
   - Paste the API key in the `.env` file as shown above.

2. **SerpApi Key:**
   - Visit the [SerpApi website](https://serpapi.com/users/sign_up) and sign up for an account if you don't already have one.
   - After logging in, go to the API section in your dashboard.
   - Create a new API key and copy it.
   - Paste the API key in the `.env` file as shown above.

---
### 5. Create the `config.json` File

Create a `config.json` file in the root directory with the following content:

```json
{
    "custom_css": {
        "background_image_url": "https://images.unsplash.com/photo-1513922203437-86dc31ea478f?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTJ8fGRhcmslMjBwbGFuZXxlbnwwfHwwfHx8MA%3D%3D",
        "hide_footer": true
    },
    "flight_search": {
        "engine": "google_flights",
        "currency_options": ["INR", "USD", "EUR", "GBP", "JPY"]
    },
    "openai": {
        "model": "gpt-4o",
        "temperature": 0
    }
}
```

## Usage

### Run the Application

```bash
streamlit run Flights_App.py
```

Open your browser and navigate to `http://localhost:8501` to access the application.

## How It Works

1. **User Input:** Enter departure and arrival airport codes, select flight type, outbound date, return date (if applicable), and currency.
2. **Flight Search:** The application queries SerpAPI for flight data.
3. **Data Analysis:** The flight data is analyzed and a detailed comparison is generated using OpenAI.
4. **Results:** The results, including best value flights, cheapest flight details, and environmental impact, are displayed to the user.

## Introduction Video

Check out our [introduction video on YouTube](https://youtu.be/g5st4b4gPmY) to learn more about the project!

[![Introduction Video]([https://i9.ytimg.com/vi_webp/g5st4b4gPmY/mq2.webp?sqp=CNi8irUG-oaymwEmCMACELQB8quKqQMa8AEB-AH-CYACvgWKAgwIABABGEcgVyhlMA8=&rs=AOn4CLCm1rb7goBiOtw-W5kpFAQivrO--g](https://i.ytimg.com/an_webp/g5st4b4gPmY/mqdefault_6s.webp?du=3000&sqp=CJylmrUG&rs=AOn4CLDMu6q13UrV9ifirJfYOioH3geznw))](https://youtu.be/g5st4b4gPmY)

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix.
3. Commit your changes and push to your fork.
4. Open a pull request with a description of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or feedback, please contact [mohitpanghal12345@gmail.com](mailto:mohitpanghal12345@gmail.com).

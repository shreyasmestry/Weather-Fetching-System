# Weather Fetching System

A clean and interactive Command-Line Interface (CLI) application built with Python. It communicates with the OpenWeatherMap API to retrieve and display current weather details for any city globally.

## 🚀 Features

* **Real-Time Global Weather:** Fetches instant details including temperature, conditions, "feels like" temperature, humidity, and wind speed.
* **Metric System:** Displays metrics automatically in Celsius (°C) and meters per second (m/s).
* **Secure Credentials:** Utilizes a decoupled environment structure via a `.env` file to keep your API keys safe.
* **Error Handling:** Provides clear terminal feedback for invalid API keys, non-existent cities, or network connection issues.
* **Interactive Loop:** Runs continuously so you can check multiple locations, and closes gracefully when you type `exit`.

---

## 🛠️ Built With

* **Python 3**
* **requests** - For handling HTTP requests to the OpenWeatherMap API.
* **python-dotenv** - For reading environment variables from a local `.env` file.

---

## 📋 Prerequisites

Before running this project, ensure you have Python 3 installed on your machine. You will also need a free API key from OpenWeatherMap.

1. Sign up at [OpenWeatherMap](https://openweathermap.org/api).
2. Generate an API Key (also called `appid`).

---

## 🔧 Installation & Setup

Follow these steps to get the application running locally:

### 1. Clone the Repository
```bash
git clone [https://github.com/shreyasmestry/Weather-Fetching-System.git](https://github.com/shreyasmestry/Weather-Fetching-System.git)
cd Weather-Fetching-System


2. Install Dependencies
Run the following command to install the required Python packages:

Bash
pip install requests python-dotenv


3. Configure Environment Variables
Create a file named .env in the root directory of the project and add your API key:
Code snippet
OPENWEATHER_API_KEY=your_actual_api_key_here


4. Run the Application
Launch the script using Python:
Bash
python main.py
(Note: Replace main.py with the actual name of your Python file if it is named differently).

💡 Usage Example

🌤️  Welcome to the Command-Line Weather App 🌤️
Enter a city name (or type 'exit' to quit): Mumbai

🌍 Weather Report for Mumbai, IN:
-----------------------------------
Condition:    Haze
Temperature:  31.94°C
Feels Like:   38.94°C
Humidity:     70%
Wind Speed:   3.6 m/s
-----------------------------------

Enter a city name (or type 'exit' to quit): exit
Goodbye!


📂 Project Structure
Plaintext
Weather-Fetching-System/
│
├── main.py             # Core Python script with API logic
├── .env                # Local file storing your private API key (do not commit)
└── README.md           # Project documentation

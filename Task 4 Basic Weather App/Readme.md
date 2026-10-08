# OIBSIP Task 4 - Basic Weather App 🌤️

A beginner-friendly command-line weather application built using Python and the OpenWeather API.

The application allows users to enter a city name and retrieve its current weather information, including temperature, humidity, and weather condition. It also includes input validation and error handling for invalid cities, API/network issues, and missing configuration.

---

## 📌 Task Information

**Program:** Oasis Infobyte Python Programming Internship (OIBSIP)
**Task:** Task 4 - Basic Weather App
**Level:** Beginner
**Language:** Python
**Application Type:** Command-Line / Terminal Application

---

## 🚀 Features

* Search for the current weather of any city
* Display:

  * City name
  * Temperature in Celsius
  * Humidity percentage
  * Current weather condition
* Validate empty city input
* Handle invalid city names
* Handle invalid API key errors
* Handle API rate-limit errors
* Handle other HTTP errors
* Handle network/request failures
* Handle missing weather data gracefully
* Allow users to search for multiple cities
* Validate `y/n` input when searching again
* Keep the API key secure using a `.env` file

---

## 🛠️ Technologies Used

* **Python**
* **Requests** - Used to send HTTP GET requests to the weather API
* **python-dotenv** - Used to load the API key securely from the `.env` file
* **OpenWeather API** - Provides current weather data

---

## 📂 Project Structure

```text
Task 4 Basic Weather App/
│
├── weather.py
├── README.md
├── .env
├── .gitignore
├── weatherapp_demo.mp4
│
└── screenshots/
    ├── successful-search.png
    ├── invalid-city.png
    └── input-validation.png
```

> **Note:** The `.env` file contains the API key and is excluded from GitHub using `.gitignore`.

---

## ⚙️ How It Works

The application follows this basic flow:

```text
Start
  ↓
Load API key from .env
  ↓
Ask user for city name
  ↓
Validate city input
  ↓
Send GET request to OpenWeather API
  ↓
Check HTTP response
  ↓
Parse JSON weather data
  ↓
Extract required information
  ↓
Display weather
  ↓
Ask whether to search another city
  ↓
Repeat or exit
```

---

## 🔑 API Configuration

This project uses the **OpenWeather Current Weather API**.

Create a `.env` file in the project folder and add:

```text
OPENWEATHER_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your own OpenWeather API key.

The application loads the key using `python-dotenv` instead of placing the key directly inside the Python source code.

### 🔒 Security

The `.env` file is included in `.gitignore` so that the API key is not uploaded to GitHub.

**Never publish your actual API key in the source code, README, screenshots, or demo video.**

---

## 📦 Installation

Make sure Python is installed on your system.

Install the required packages using:

```bash
pip install requests python-dotenv
```

Or:

```bash
python -m pip install requests python-dotenv
```

---

## ▶️ How to Run

Open the project folder in a terminal and run:

```bash
python weather.py
```

Enter a city when prompted:

```text
Enter city name: Kolkata
```

Example output:

```text
City: Kolkata
Temperature: 29.92°C
Humidity: 71%
Description: scattered clouds
```

The actual weather values will change depending on the current conditions.

The application then asks:

```text
Search another city? (y/n):
```

---

## 🛡️ Error Handling

The application handles several possible problems.

### Empty City Input

If the user submits an empty input:

```text
Please enter a city name.
```

The application asks for the city again.

### Invalid City

If the requested city cannot be found:

```text
City not found. Please check the spelling.
```

### Invalid API Key

If the API key is rejected:

```text
Invalid API key. Please check your API configuration.
```

### Network Failure

If the application cannot connect to the weather service:

```text
Unable to connect to the weather service.
```

### Rate Limit

If the API request limit is reached:

```text
Too many requests. Please try again later.
```

### Missing Weather Data

If an expected value is unavailable from the API response, the application displays:

```text
Unavailable
```

instead of crashing.

---

## 🧪 Testing

The application was tested for the following scenarios:

* ✅ Valid city search
* ✅ Multiple city searches
* ✅ Empty city input
* ✅ Invalid city name
* ✅ Uppercase/lowercase `Y/N` input
* ✅ Invalid search-again input
* ✅ Network/request failure
* ✅ Missing API key
* ✅ HTTP error responses
* ✅ Missing weather fields

---

## 📸 Screenshots

Screenshots demonstrating the application's functionality are available in the `screenshots` folder.

### Included screenshots

* `successful-search.png` - Successful weather search
* `invalid-city.png` - Invalid city handling
* `input-validation.png` - Input and search-again validation

---

## 🎥 Demo Video

A demonstration of the Basic Weather App is included in:

```text
weatherapp_demo.mp4
```

The demonstration covers:

* Running the application
* Searching for a city
* Displaying weather information
* Handling an invalid city
* Searching for another city
* Exiting the application

---

## 📚 Concepts Practiced

This project helped practice several Python and software-development concepts:

* Python variables
* Dictionaries and lists
* Nested data structures
* Conditional statements
* `while` loops
* `break`
* User input validation
* Exception handling with `try/except`
* HTTP requests
* REST API concepts
* JSON parsing
* Environment variables
* API authentication
* Error handling
* Basic application flow

---

## 🔮 Possible Future Improvements

The application could be extended in the future with:

* Multi-day weather forecasts
* Weather icons
* Wind speed and direction
* Sunrise and sunset information
* GUI interface
* Weather history
* More detailed location information

These features are outside the scope of this beginner-level task.

---

## 👨‍💻 Author

**Binayak Mukherjee**

BCA Graduate | Python Developer Aspirant

---

## 📄 Internship

This project was developed as part of the **Oasis Infobyte Python Programming Internship (OIBSIP)**.

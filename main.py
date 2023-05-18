import argparse
import pyfiglet
from simple_chalk import chalk
import  requests
#api key from opemweather 
API_KEY = "bde40fe662368cd52f1ab0a7762a5036"
#BASE URL FOR OPENWEATHER API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather?q="
#https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
#https://api.openweathermap.org/data/2.5/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid=0a5293ca5b97edfd537506d2154de7e6
#https://api.openweathermap.org/data/2.5/onecall?lat=33.44&lon=-94.04&exclude=hourly,daily&appid=0a5293ca5b97edfd537506d2154de7e6
#https://api.openweathermap.org/data/2.5/weather?q=${*cityName*}&appid=${*API_key*}&units=metric
#  |
#  |
# \/ This works now older one dosen't work
#https://api.openweathermap.org/data/2.5/weather?q=London&APPID=bde40fe662368cd52f1ab0a7762a5036
WEATHER_ICONS = {
    "01d": "🌞",
    "01n": "🌙",
    "02d": "⛅",
    "02n": "☁",
    "03d": "☁",
    "03n": "☁",
    "04d": "☁",
    "04n": "☁",
    "09d": "🌦",
    "09n": "🌦",
    "10d": "🌧",
    "10n": "🌧",
    "11d": "⛈",
    "11n": "⛈",
    "13d": "❄",
    "13n": "❄",
    "50d": "🌫",
    "50n": "🌫",
}
#construct API URL with query parameters
parser=argparse.ArgumentParser(description="Check the weather for a certain country/city")
parser.add_argument("city",help="Enter the name of the city/country to check the weather for-")
args=parser.parse_args()
url=f"{BASE_URL}{args.city}&APPID={API_KEY}&units=metric"

#make api request and parse the response using requests module
response= requests.get(url)

#check if the request was successful
if response.status_code!=200:
    print(chalk.red(f"Error: Unable to retrieve weather data for {args.country}!!!"))
    exit()
    
#parsing the JSON response from the API and extracting the weather information
data = response.json()

#extracting the weather information
temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
description = data["weather"][0]["description"]
icon = data["weather"][0]["icon"]
city = data["name"]
country = data["sys"]["country"]

#construct the output with th eweather icon
weather_icon=WEATHER_ICONS.get(icon, "")
output=f"{pyfiglet.figlet_format(city)},{country}\n\n"
output+=f"{weather_icon} {description}\n"
output+=f"Temprature: {temperature}°C\n" 
output+=f"Feels like: {feels_like}°C\n"
#print the output
print(chalk.cyan(output))





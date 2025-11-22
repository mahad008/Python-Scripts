import requests

API_KEY = "b4f3cf3f8255c407e78f54b369601c3e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()

        weather = {
            "City": data["name"],
            "Temperature": data["main"]["temp"],
            "Feels Like": data["main"]["feels_like"],
            "Humidity": data["main"]["humidity"],
            "Weather": data["weather"][0]["description"],
            "Wind Speed": data["wind"]["speed"]
}
        
        return weather
    
    else:
        print("Error:", response.status_code)
        return None
    
if __name__ =="__main__":
    city = input("Enter your city name: ")
    result = get_weather(city)


    if result:
        print("\n --WEATHER INFO--")
        for key, value in result.items():
            print(f"{key}: {value}")    


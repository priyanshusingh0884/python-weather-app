import requests
from weather import ApiKey
import win32com.client


speaker = win32com.client.Dispatch("SAPI.SpVoice")




city = input("Enter the name of the city: ")

url = f"http://api.weatherapi.com/v1/current.json?key={ApiKey}&q={city}"

try:
    r = requests.get(url, timeout=10)
    # print(r.text)



    if r.status_code == 200:
        weather_dic = r.json()

        loc = weather_dic.get("location", {})
        curr = weather_dic.get("current", {})
        condition = curr.get("condition", {})

        city = loc.get("name")
        region = loc.get("region")
        country = loc.get("country")
        time_zone = loc.get("tz_id")
        localtime = loc.get("localtime")

        last_updated = curr.get("last_updated")
        temp_c = curr.get("temp_c")
        feels_like = curr.get("feelslike_c")
        condition_text = condition.get("text")
        humidity = curr.get("humidity")
        wind_kph = curr.get("wind_kph")
        wind_dir = curr.get("wind_dir")
        precip = curr.get("precip_mm")
        uv = curr.get("uv")
        heat_index = curr.get("heatindex_c")
        chance_of_rain = curr.get("chance_of_rain")

        

        print(f"\n--- Weather Report for {city}, {region}, {country} ---")
        print(f"Time zone: {time_zone}")
        print(f"Local Time: {localtime}")
        print(f"Condition: {condition_text}")
        print(f"Temperature: {temp_c}°C")
        print(f"Feels like: {feels_like}")
        print(f"Humidity: {humidity}%")
        print(f"Heat index: {heat_index}")
        print(f"Wind: {wind_kph} kph ({wind_dir})")
        print(f"Chance of rain: {chance_of_rain}%")
        print(f"Precipitation: {precip} mm")
        print(f"UV Index: {uv}")
        print(f"Last updated: {last_updated}")

        speech_text = (
            f"Weather Report for {city}, {region}, {country}. "
            f"Time zone for {city}, {region} is {time_zone}."
            f"Local time currently is {localtime}."
            f"The current condition is {condition_text}. "
            f"Temperature of {city} is {temp_c} degrees Celsius, feeling like {feels_like} degrees. "
            f"Heat index of {city} is {heat_index}"
            f"Humidity is {humidity} percent. "
            f"Wind is blowing at {wind_kph} kilometers per hour from the {wind_dir}. "
            f"Chance of rain is {chance_of_rain} percent."
            f"The weather report is last updated {last_updated}"
        )
        speaker.Speak(speech_text)
        
    else:
        print(f"Error: Could not retrieve data for '{city}'. (Status code: {r.status_code})")

except Exception as e:
    print(f"An error occured as {e}")


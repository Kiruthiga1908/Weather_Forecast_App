import requests

api_key = '30d4741c779ba94c470ca1f63045390a'

user_input = input("Enter city for Weather Details: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")
# weather_data = requests.get(f"https")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    hum = weather_data.json()['main']['humidity']
    print()
    print(f"The weather in {user_input} is: {weather}")
    print()
    print(f"The temperature in {user_input} is: {temp}ºF")
    print()
    print(f"The humidity in {user_input} is: {hum}")

    # print(weather_data.json())




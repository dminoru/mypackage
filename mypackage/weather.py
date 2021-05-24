import sys
import requests

BASE_URI = "https://www.metaweather.com"

def search_city(query):
    response = requests.get(
        f'{BASE_URI}/api/location/search/?query={query}'
    ).json()
    if response:
        return response[0]
    return None


def weather_forecast(woeid):
    response = requests.get(
        f'{BASE_URI}/api/location/{woeid}'
    ).json()
    forecast = response['consolidated_weather']
    return forecast


def main():
    query = input("City?\n> ")
    location = search_city(query)
    woeid = location["woeid"]
    city  = location["title"]
    weathers = weather_forecast(woeid)
    weather = []
    for i in weathers:
        weather_state_name = i['weather_state_name']
        applicable_date = i['applicable_date']
        max_temp = round(i['max_temp'], 1)
        weather.append(f'{applicable_date} : {weather_state_name} {max_temp} °C')
    # if location == None:
        #return to input step
    print(f"Here's the weather in {city}")
    for i in weather:
        print(i)


if __name__ == '__main__':
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print('\nGoodbye!')
        sys.exit(0)
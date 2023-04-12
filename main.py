import requests
from twilio.rest import Client


MY_LAT = -32.907200
MY_LONG = 17.990530

# Twilio


api_key = "416c5295f4cf7096c9600b01f18fae04"
OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"

weather_parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily,",
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    cond_code = hour_data["weather"][0]["id"]
    if int(cond_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(body="Bring an umbrella ☔️!",
                                     from_='++19498282814',
                                     to='+27731024346'
                                     )
    print(message.status)










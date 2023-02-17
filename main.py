import requests
from twilio.rest import Client
# Twilio API
auth_token = "{Your Twilio Token}"
account_sid = "{Your Twilio sid}"

# Open Weather Map API
API_KEY = "{Your API key}"
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.8/onecall"

parameters = {
    "lat": "Your latitude in integer",
    "lon": "Your longitude in integer",
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alerts",
}

response = requests.get(OWM_ENDPOINT, params=parameters)
# print(response.status_code)
response.raise_for_status()
weather_data = response.json()
# print(weather_data)

weather_slice = weather_data["hourly"][0:12]
# print(weather_slice)

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]['id']
    print(condition_code)
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # The below code can be copied from twilio api
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, Please bring umbrella☂.",
        from_='{Your Twilio ph no}',
        to='{Your ph no with country code}'
    )
    print(message.status)
    # print("Bring Umbrella")

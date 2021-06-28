import requests
from twilio.rest import Client

# Infos to the openweathermap API
API_KEY = "YOUR OPENWEATHERMAP API KEY"
MY_LAT = -27.594870
MY_LON = -48.548222
EXCLUDE_PARAMS = "current,minutely,daily"

# Twilio
account_sid = "YOUR TWILIO ACCOUNT SID"
auth_token = "YOUR TWILIO AUTH TOKEN"

# use openweathermap API to get weather info
response = requests.get(f"https://api.openweathermap.org/data/2.5/onecall?lat={MY_LAT}&lon={MY_LON}&exclude={EXCLUDE_PARAMS}&appid={API_KEY}")
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

# Check if it will rain based on weather info
will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

# If it will rain send a message for a contact
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Rembember the umbrella! ☂️",
        from_="+18XXXXXXXXX",
        to="+5564XXXXXXXXX"
    )
    print(message.status)


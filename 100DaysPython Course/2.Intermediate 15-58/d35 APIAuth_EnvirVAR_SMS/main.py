import requests
from twilio.rest import Client

#KEYS
phone_number_twilio="XXXXXXXXXXXXXXXXX"
phone_number_mine ="XXXXXXXXXXXXXXXXXX"
account_sid_key ="XXXXXXXXXXXXXXXXXXXX"
auth_token_key = "XXXXXXXXXXXXXXXXXXXX"



def send_sms () :
    client = Client(account_sid_key, auth_token_key)
    message = client.messages \
                    .create(
                         body="ITS RAINNING BUDDY",
                         from_=phone_number_twilio,
                         to=phone_number_mine
                     )

    print(message.sid)

api_key = "e399abd51551b8b298e898dec688a89b"
open_weather_api = "https://api.openweathermap.org/data/2.5/onecall"

param = {
    "lat": 41.5518,
    "lon": -8.4229,
    "exclude": "current,minuetely,daily",
    "appid": api_key
}

request = requests.get(open_weather_api, params=param)
data = request.json()
weather_slice = data["hourly"][:12]
for var in weather_slice:
    if (var["weather"][0]["id"] > 701):
        send_sms()
        break
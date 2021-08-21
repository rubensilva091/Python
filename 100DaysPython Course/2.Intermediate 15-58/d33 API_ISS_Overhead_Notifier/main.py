import requests
from datetime import datetime
import smtplib
from email.message import EmailMessage
import time

MY_EMAIL = "ruben.python091@gmail.com"
MY_PASSWORD = "XXXXXXXXX"
MY_LAT = 41.5518  # Your latitude
MY_LONG = -8.4229  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


msg = EmailMessage()

msg["Subject"] = "MEEEKIEE MEU PUTO"
msg['From'] = MY_EMAIL
msg['To'] = "rubenfamalicao@live.com.pt"
msg.set_content("ISS NEAR YOU BUDDY; GO CHECK IT!")


# Your positio
#
# n is within +5 or -5 degrees of the ISS position.
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(
    "https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])


def send_email_server():
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.send_message(msg)
    connection.close()


# check if ISS near
def check_near_location():
    range_X = MY_LAT-iss_latitude
    range_y = MY_LONG-iss_longitude
    if ((range_X < 5 and range_X > -5) and (range_y < 5 and range_y > -5)):
        if (sunrise <= time_now or time_now <= sunrise):
            return True
    return False


time_now = datetime.now().hour


while(True):
    if check_near_location() == True:
        send_email_server()
        print("ISS!")
    else:
        print("NO ISS!")
    time.sleep(60)

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.

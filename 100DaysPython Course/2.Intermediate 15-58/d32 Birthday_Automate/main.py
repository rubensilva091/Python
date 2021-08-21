from email.message import EmailMessage
import datetime as dt
import smtplib
import random

#website_clouder = "PYTHON ANYWHERE"

QUOTES_RELATIVE_PATH = "d32 Birthday_Automate\quotes.txt"

MY_EMAIL = "ruben.python091@gmail.com"
MY_PASSWORD = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"


# IMPORTANTE, É ASSIM QUE SE CRIA UM E-MAIL

msg = EmailMessage()

msg["Subject"] = "MEEEKIEE MEU PUTO"
msg['From'] = MY_EMAIL
msg['To'] = "rubenfamalicao@live.com.pt"
msg.set_content("Hi")


time_now = dt.datetime.now()
time_my_birthday = dt.datetime(year=2001,month=1, day=6)
#time_my_birthday = dt.datetime.now()

quotes_list = []
message_body = ""


def open_file():
    with open(QUOTES_RELATIVE_PATH, "r") as quotes_file:
        for var in quotes_file:
            quotes_list.append(var)


def rotate_msg():
    message_body = random.choice(quotes_list)
    msg.set_content(message_body)


# connect gmail Server
# istoo precisa de ser coerente com o meu o e-mail que vai enviar
def send_email_server():
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
    connection.send_message(msg)
    connection.close()


def birthday_whisher():
    open_file()
    rotate_msg()
    send_email_server()


if ((time_now.month == time_my_birthday.month) and (time_now.day == time_my_birthday.day)):
    birthday_whisher()

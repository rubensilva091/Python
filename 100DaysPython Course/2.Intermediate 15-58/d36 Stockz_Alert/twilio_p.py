import twilio.rest as tw

account_sid_key = "XXXXXXXXXXXX"
auth_token_key = "XXXXXXXXXXXX"
phone_number_twilio ="XXXXXXXXXXXX"
phone_number_mine ="XXXXXXXXXXX"



def send_sms(title_article,body_article, tesla_percetage):
    string_to_send = "TSLA 🔻 "+tesla_percetage+" %\nHeading: "+title_article+"\nBrief: "+body_article
    client = tw.Client(account_sid_key, auth_token_key)
    message = client.messages \
                    .create(
                        body=string_to_send,
                        from_=phone_number_twilio,
                        to=phone_number_mine
                    )

    print(message.sid)

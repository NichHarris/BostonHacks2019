from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from flask import Flask, request, redirect

# Your Account SID from twilio.com/console
account_sid = "AC325fc81b8caab6accba141ee3253f9d8"
# Your Auth Token from twilio.com/console
auth_token  = "6bd1d57e2f59caafa8ce6eeacc016f6f"

client = Client(account_sid, auth_token)
message = client.messages.create(
    to="+14388327376", #My number
    from_="+17654055994", #twilio number
    body="Hello From Boston Hacks 2019. Robots are taking over now. -Nick")

print(message.sid)

app = Flask(__name__)
@app.route('/sms', methods=['GET', 'POST'])
def sms():
    msg = request.values.get('Body').lower().strip()
    res = MessagingResponse()
    if msg == "Hi":
        res.message("noice")
    else:
        res.message("meh")
    return str(res)

if __name__ == "__main__":
    app.run(debug=True)


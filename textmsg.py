from twilio.rest import Client

account_sid = "AC5527a294d4c6fb0d9b91698de8b6e9b2"
auth_token = "0becfe4953cefb8bea3431935d29066b"
client = Client(account_sid, auth_token)

message = client.messages.create(
        body='This is the ship that made the Kessel Run in fourteen parsecs?',
        from_='+12028915488',
        to='+916377281477'
    )

print(message.sid)

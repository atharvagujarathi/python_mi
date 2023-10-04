from twilio.rest import Client

account_sid = 'AC6ed43d841e317648827eab5da62128d6'
auth_token = 'db8be5cf86f3bc8ccba92030b2febd49'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='whatsapp:+919359723356',
  body='Ok',
  to='whatsapp:+919359723356'
)

print(message.sid)
import pywhatkit as kit

# Specify the recipient's phone number (with country code) and the message
recipient_number = "+919359723356"  # Replace with the recipient's number
message = "Hello, this is an automated message from Python!"

# Specify the time to send the message (24-hour format)
hour = 23  # Replace with the desired hour
minute = 10  # Replace with the desired minute

# Send the message
kit.sendwhatmsg(recipient_number, message, hour, minute)

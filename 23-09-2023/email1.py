import smtplib
from email.mime.text import MIMEText # Multipurpose Internet mail extensions
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from apscheduler.schedulers.blocking import BlockingScheduler

# Your email configuration
sender_email = "atharvagujarathi92@gmail.com"
receiver_email = "atharvagujarathi92@gmail.com"
subject = "Hello, Sir sorry to disturb"
message_body = "This is the message body of the email."
email_password = "jfka fpyr zwdv wqna"

# Email-sending function
def send_email():
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message_body, 'plain'))
    
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender_email, email_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

    finally:
        server.quit()

# Create a scheduler instance
scheduler = BlockingScheduler()

# Schedule the email to be sent at a specific time (e.g., every day at 8 AM)
scheduler.add_job(send_email, 'cron', hour=23, minute=29)

try:
    # Start the scheduler
    scheduler.start()
except KeyboardInterrupt:
    # Handle Ctrl+C to gracefully exit the scheduler
    pass

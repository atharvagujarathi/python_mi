import smtplib
import csv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Your Gmail account credentials
sender_email = "atharvagujarathi92@gmail.com"
subject = "Hello, Sir sorry to disturb"
email_password = "jfka fpyr zwdv wqna"

# Read data from the CSV file
with open("example.csv", mode="r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    for row in csv_reader:
        recipient_email = row["ID"]
        
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email

        # Connect to the SMTP server (in this case, Gmail's SMTP server)
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(sender_email, email_password)

            # Send the email
            server.sendmail(sender_email, recipient_email, msg.as_string())
            print(f"Email sent successfully to {recipient_email}")

        except Exception as e:
            print(f"An error occurred while sending the email to {recipient_email}: {str(e)}")

        finally:
            server.quit()

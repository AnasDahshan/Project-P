import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

def send_email(to, subject, body):
    # Set up the email
    msg = MIMEMultipart()
    msg['From'] = 'khanafer@hotmail.com'
    msg['To'] = to
    msg['Subject'] = subject

    # Add the body of the email
    msg.attach(MIMEText(body, 'plain'))

    # Add an image to the email (optional)
    # with open('image.png', 'rb') as f:
    #     img_data = f.read()
    # img = MIMEImage(img_data, name='image.png')
    # msg.attach(img)

    # Send the email
    try:
        server = smtplib.SMTP('localhost', 25) # localhost means send email locally
        server.sendmail(msg['From'], msg['To'], msg.as_string())
        print("Email sent successfully")
    except Exception as e:
        print(f"Something went wrong while sending the email: {e}")
    finally:
        server.quit()

# Example usage:
to = 'khanafer@hotmail.com'
subject = 'Test email from Python'
body = 'This is a test email sent from Python using the smtplib library.'
send_email(to, subject, body)

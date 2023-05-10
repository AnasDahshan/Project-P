import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender:
    def __init__(self, email, password):
        self.email = email
        self.password = password
    
    def send_email(self, to, subject, body):
        msg = MIMEMultipart()
        msg['From'] = self.email
        msg['To'] = to
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(self.email, self.password)
            text = msg.as_string()
            server.sendmail(self.email, to, text)
            print('Email sent successfully.')
        except Exception as e:
            print('Something went wrong while sending the email:', e)
        finally:
            server.quit()

def main():
    email_sender = EmailSender('your_email@gmail.com', 'your_password')
    to = 'recipient_email@gmail.com'
    subject = 'Test Email'
    body = 'This is a test email sent from Python!'
    email_sender.send_email(to, subject, body)

if __name__ == '__main__':
    main()

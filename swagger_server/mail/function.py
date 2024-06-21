import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

def send_mail(to_address: str, subject: str, body: str):
    from_address = os.getenv('MAIL_USERNAME')
    password = os.getenv('MAIL_PASSWORD')
    message = MIMEMultipart()
    message['From'] = from_address
    message['To'] = to_address
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_address, password)
    server.sendmail(from_address, to_address, body)
    server.quit()
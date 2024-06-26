import smtplib, os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

load_dotenv()

def send_mail(to_address: str, subject: str, body: str):
    from_address = os.getenv('MAIL_USERNAME')
    password = os.getenv('MAIL_PASSWORD')
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = to_address
    msg['Subject'] = subject
    content = MIMEText(body, 'plain', 'utf-8')
    msg.attach(content)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_address, password)
    server.sendmail(from_address, to_address, msg.as_string().encode('utf-8'))
    server.quit()

def send_admin(user_dni: str, event_id: int, subject: str, body: str):
    from_address = os.getenv('MAIL_USERNAME')
    password = os.getenv('MAIL_PASSWORD')
    body = f"{body}\nDNI: {user_dni}\nID Evento: {event_id}"
    msg = MIMEMultipart()
    msg['From'] = from_address
    msg['To'] = from_address
    msg['Subject'] = subject
    content = MIMEText(body, 'plain', 'utf-8')
    msg.attach(content)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_address, password)
    server.sendmail(from_address, from_address, msg.as_string().encode('utf-8'))
    server.quit()
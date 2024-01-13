from email.mime.text import MIMEText
from base64 import urlsafe_b64encode
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials

from googleapiclient.errors import HttpError

scopes=['https://www.googleapis.com/auth/gmail.send']
credentials = Credentials.from_authorized_user_file("token.json", scopes)

service = build('gmail', 'v1', credentials=credentials)


def create_message(sender, to, subject, body):
    message = MIMEText(body)
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    raw_message = urlsafe_b64encode(message.as_string().encode("utf-8"))
    print(raw_message)
    return {
        'raw': raw_message.decode("utf-8")
    }


def send_email(sender, to, subject, body):
    message = create_message(sender, to, subject, body)
    try:
        service.users().messages().send(userId="me", body=message).execute()
        print("Сообщение отправлено.")
    except HttpError as error:
        print(f"Возникла ошибка {error}")

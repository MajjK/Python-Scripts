import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import imaplib
import email
import time
# Simple script made for mailbox handling. It offers sending and receiving e-mail messages with image attachments.
smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port_send = 465
smtp_ssl_port = 'imap.gmail.com'
smtp_ssl_port_receive = 993


def create_message():
    msg = MIMEMultipart()
    msg['Subject'] = 'Test Picture'
    msg['From'] = username
    msg['To'] = ', '.join(targets)
    txt = MIMEText('Test text')
    msg.attach(txt)
    filepath = 'test.jpg'
    with open(filepath, 'rb') as f:
        img = MIMEImage(f.read())

    img.add_header('Content-Disposition', 'attachment', filename=os.path.basename(filepath))
    msg.attach(img)
    return msg


def get_last_message(mail):
    result, data = mail.search(None, "ALL")
    id_list = data[0].split()
    latest_email_id = id_list[-1]
    result, data = mail.fetch(latest_email_id, "(RFC822)")
    last_message = email.message_from_bytes(data[0][1])
    return last_message


def get_text(message):
    mail_from = message['from']
    mail_subject = message['subject']

    if message.is_multipart():
        mail_content = ''
        for part in message.get_payload():
            if part.get_content_type() == 'text/plain':
                mail_content += part.get_payload()
    else:
        mail_content = message.get_payload()
    print(f'From: {mail_from}')
    print(f'Subject: {mail_subject}')
    print(f'Content: {mail_content}')


def get_attachment(message):
    for part in message.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        filename = 'downloaded_' + part.get_filename()
        att_path = os.path.join(ROOT_DIR, filename)
        if not os.path.isfile(att_path):
            fp = open(att_path, 'wb')
            fp.write(part.get_payload(decode=True))
            fp.close()


username = 'your_mail_address@gmail.com'
password = 'your_password'
# You can send message to your own e-mail account, then download it and save picture with different name
# or send it to any other address, and download last message from your e-mail
targets = ['your_mail_address@gmail.com']

msg = create_message()
server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port_send)
server.login(username, password)
server.sendmail(username, targets, msg.as_string())
server.quit()

time.sleep(10)

mail = imaplib.IMAP4_SSL(smtp_ssl_host, smtp_ssl_port_receive)
mail.login(username, password)
mail.list()
mail.select("inbox")
message = get_last_message(mail)
get_text(message)
get_attachment(message)
mail.logout()

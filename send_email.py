'''The send_email module contains the send_email function, which uses the SMTP protocol and gmail to send emails.
'''
from config import config
import smtplib

def send_email(subject, msg):
    '''The send email function sends mail to a user and takes subject and msg as arguments. Subject is the subject of
    the mail item and msg is the body of the mail item. This function is currently formatted to work with gmail.
    '''
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(config.sending_email_address, config.sending_email_address_password)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.sending_email_address, config.receiving_email_address, message)
        server.quit()
        print("Success: Email sent!")
    except smtplib.SMTPAuthenticationError:
        print("Email failed to send.")





### for this function to work there needs to be a config.py file in the same directory
import requests
from config import mailgun_lamotors_api, production

host = "https://api.mailgun.net/v3/api.lamotorsdirect.com/messages"

def send_email(subject, body, attachment_url='',
               to=['moises@lamotorsdirect.com']):
    to.append('reports@lamotorsdirect.com')
    to_str = ';'.join(to)

    """Sending emails using Mailgun API"""
    if production == "false":
        to_str = 'moises@lamotorsdirect.com'

    if len(attachment_url) == 0:
        attachment = []

    else:
        f = open(attachment_url, 'rb')
        attachment = [("attachment", f)]
    print(to_str)
    payload = {"from": "moises@api.lamotorsdirect.com",
            "to": to_str,
            "subject": subject,
            "html": body}

    r1 = requests.post(host,
        auth=("api",mailgun_lamotors_api),
        files=attachment,
        data=payload)

    if len(attachment_url) != 0:
        f.close()

    return r1

# record of this email in your logs: https://app.mailgun.com/app/logs
import os, sys
import numpy as np
import pandas as pd
import json

from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.text import MIMEText as text
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

def SendMail(receiver,subject,message):
    config = json.loads(open(__location__+'/emailConfig.json').read())
    message = """\
    <html>
      <head></head>
      <body>
        <p> %s
        </p>
      </body>
    </html>
    """ %message
    m = text(message,'html')
    m['Subject'] = subject
    m['From'] = 'BazyliZwiazek'
    m['To'] = receiver
    try:
        mail_lib = smtplib.SMTP_SSL(config['server'], config['port'])
        mail_lib.login(config['address'], config['password'])
        mail_lib.sendmail(config['address'],receiver,m.as_string())
    except smtplib.SMTPException:
        print "Error: unable to send email"

def GetSoup(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')
    return soup

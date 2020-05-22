# -*- coding: utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys

mesaj = MIMEMultipart()
mesaj["From"] = "bilgi@mert.space"
mesaj["To"] = "mertinal1998@hotmail.com"
mesaj["Subject"] = "SMTP mail gönderme"
yazi = """
SMTP ile mail gönderiyorum 
Mert Space

-Mert İnal -

"""
mesajGovdesi = MIMEText(yazi, "plain")
mesaj.attach(mesajGovdesi)
try:
    mail = smtplib.SMTP("mail.mert.space", 587)
    mail.ehlo()
    mail.starttls()
    mail.login("bilgi@mert.space", "WRITEPASS")
    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
    print("Mail Başarıyla Gönderildi ..")
    mail.close()
except Exception as error:
    sys.stderr.write("Bir sorunoluştu .. {0}".format(error))
    sys.stderr.flush()

try:
    import os
    import datetime
    import smtplib
    import ssl
    import time as t
    import colorama
    from colorama import *

    colorama.init(autoreset=False)
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    from email.mime.base import MIMEBase
    from email import encoders
    from main import msg,subject

except:
    os.system("""
    apt install pip2
    pip install smtplib
    pip install datetime
    pip  install colorama
    """)


def mail_attack(mail_target):
    SSL = 465
    sender = "i2625644@gmail.com"
    phonenumber = "uvis nimf jlnt hsch"
    message = MIMEMultipart("alternative")
    message["From"] = sender
    message["To"] = mail_target
    message["Subject"] = subject
    part = MIMEText(msg, "html")
    message.attach(part)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", SSL, context=context) as server:
        print(Fore.GREEN + "Signing into the server")
        t.sleep(3)
        try:
            server.login(sender, phonenumber)
            print(Fore.GREEN + "[✓] Logged in sucessfully")
        except:
            print(Fore.RED + "[!] Login failed")
            t.sleep(3)
        print(Fore.GREEN + "Sending mail to", mail_target)
        t.sleep(3)
        try:
            server.sendmail(sender, mail_target, message.as_string()
                            )
            print(Fore.GREEN + "[✓] Mail sent sucessfully")
        except:
            print(Fore.RED + "Failed to send Mail!")
            t.sleep(3)
    return Fore.GREEN + "[✓] Mail sent sucessfully"

import os

os.environ["APP_PASSWORD"] = "nika kyjv dvhp nnso"
APP_PASSWORD = os.environ.get("APP_PASSWORD")
print(APP_PASSWORD)

from mailerpy import Mailer

my_mailer = Mailer("smtp.gmail.com", 587, "sugamgurung2004@gmail.com", APP_PASSWORD)

mail_subject = "Hello This is email"
mail_body = """

"""
to_list = ["pramilatmg.np@gmail.com"]
attachment_list = [
    r"C:\Users\Hp\OneDrive\Pictures\Screenshots\WhatsApp Image 2025-07-16 at 22.00.59_0152ab55.jpg"
]
for recipient in to_list:
    mail_subject = f"hello {recipient[:12]}"
    my_mailer.send_mail(
        [recipient], mail_subject, mail_body, attachments=attachment_list
    )

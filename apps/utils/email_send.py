import random

from django.core.mail import send_mail

from mx_online.settings import EMAIL_FROM
from users.models import EmailVerifyRecord


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    random_str = generate_random_str(16)
    email_record.code = random_str
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '在线激活链接'
        email_body = '请点击链接激活：http://127.0.0.1:8000/active'
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass


def generate_random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars)
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str

from django.conf import settings
from django.core.mail import send_mail
from django.utils.html import escape


def send_email(mail, name):
    send_mail(
        subject="Twój zapis",
        message=f"Gratulację {name} zapisu na wydarzenie koła, widzimy się niedługo!",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[mail],
        html_message=f"<strong>Gratulację {escape(name)} zapisu na wydarzenie koła, widzimy się niedługo!</strong>",
    )


def contact_mail(mail, message):
    send_mail(
        subject=f"Kontakt - {mail}",
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[settings.CONTACT_EMAIL],
        html_message=escape(message).replace("\n", "<br>"),
    )


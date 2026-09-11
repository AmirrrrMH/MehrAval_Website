from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.mail import send_mail


@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):

    if created:
        send_mail(
            subject="New User Registered",
            message=f"""
A new user has been registered.

Username: {instance.username}
Email: {instance.email}
""",
            from_email=None,
            recipient_list=["yosefiamirmohammas@gmail.com"],
        )

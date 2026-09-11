from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

from .models import User


@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject="New User Registered",
            message=f"""
A new user has been registered.

Full Name: {instance.full_name}
Current Field: {instance.current_field}
Degree: {instance.degree}
Grade: {instance.grade}
Current School: {instance.current_school}
Field of Study: {instance.field_of_study}
Home Phone: {instance.home_phone_number}
Dad Phone: {instance.dad_phone_number}
Mom Phone: {instance.mom_phone_number}
Student Phone: {instance.student_phone_number}
Address: {instance.address}
Reason: {instance.reason_for_changing_the_school}
""",
            from_email=None,
            recipient_list=["yosefiamirmohammas@gmail.com"],
            fail_silently=False,
        )

from django.dispatch import receiver
from allauth.socialaccount.signals import pre_social_login


@receiver(pre_social_login)
def reactivate_user(sender, request, sociallogin, **kwargs):
    if not sociallogin.user.is_active:
        sociallogin.user.is_active = True
        sociallogin.user.save()

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.conf import settings
from rest_framework.authtoken.models import Token


User = get_user_model()


class Command(BaseCommand):
    help = 'Create frontend user'

    def handle(self, *args, **options):
        try:
            user = User.objects.create_user(
                username=settings.VUE_APP_API_USERNAME,
                password=settings.VUE_APP_API_PASS,
            )
            user.save()
            user.is_active = True
            user.save()
            token = Token(user=user)
            token.save()
            print(token)
        except Exception as e:
            print(str(e))
    print('Done')

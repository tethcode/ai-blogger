from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Creates a default superuser'

    def handle(self, *args, **options):
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('EmmyBoos', 'emmyboss@gmail.com', 'EmmyDaBoss@2009')
            self.stdout.write(self.style.SUCCESS('Superuser created!'))
        else:
            self.stdout.write('Superuser already exists.')

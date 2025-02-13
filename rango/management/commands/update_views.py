import random
from django.core.management.base import BaseCommand
from rango.models import Page  

class Command(BaseCommand):
    help = 'Updates the views_count of all pages with random values'

    def handle(self, *args, **kwargs):
        pages = Page.objects.all()  
        for page in pages:
            page.views_count += random.randint(1, 100)
            page.save()  
            self.stdout.write(self.style.SUCCESS(f'Updated views for page: {page.title}'))

        self.stdout.write(self.style.SUCCESS('Successfully updated views for all pages'))

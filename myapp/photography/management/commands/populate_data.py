from typing import Any
from photography.models import Section2OurExpertise
from django.core.management.base import BaseCommand

SERVICE_DATA = [
    {
        'title': 'Wedding Photography',
        'image': 'images/web.jpg',
        'alt': 'Wedding Photography',
        'description': 'Capture your special day with timeless photos that reflect the beauty and emotion of your wedding.',
    },
    {
        'title': 'Event Photography',
        'image': 'images/even.jpg',
        'alt': 'Event Photography',
        'description': 'Professional photography for all your events, big or small, to preserve precious memories.',
    },
    {
        'title': 'Portrait Photography',
        'image': 'images/port.jpg',
        'alt': 'Portrait Photography',
        'description': 'Elegant and personalized portraits that highlight your unique personality and style.',
    },
]

class Command(BaseCommand):
    help = "This command inserts or updates service data"

    def handle(self, *args: Any, **options: Any):
        for service in SERVICE_DATA:
            # Update existing or create new if not found
            obj, created = Section2OurExpertise.objects.update_or_create(
                title=service['title'],  # used as lookup field
                defaults={
                    'image': service['image'],
                    'alt': service['alt'],
                    'description': service['description'],
                }
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"✅ Created: {obj.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"🔁 Updated: {obj.title}"))

        self.stdout.write(self.style.SUCCESS("🎉 Done updating/inserting service data!"))

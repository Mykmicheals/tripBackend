import os
import json
from django.core.management.base import BaseCommand
from api.models import Location

class Command(BaseCommand):
    help = 'Load locations from JSON into the database'

    def handle(self, *args, **options):
        file_path = os.path.join(os.path.dirname(__file__), 'locations.json')
        with open(file_path) as file:
            data = json.load(file)
            for key, value in data.items():
                Location.objects.create(
                    country_id=int(key),
                    name=value['name'],
                    latitude=value['latitude'],
                    longitude=value['longitude'],
                    country_name=value['country_name']
                )

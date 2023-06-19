import os
import json
from django.core.management.base import BaseCommand
from api.models import DirectRoutes

class Command(BaseCommand):
    help = 'Load locations from JSON into the database'

    def handle(self, *args, **options):
        file_path = os.path.join(os.path.dirname(__file__), 'routes.json')
        with open(file_path) as file:
            data = json.load(file)
            for key, value in data.items():
                flight_number = int(key)
                from_location = value['from']
                to_location = value['to']
                price = value['price']
                duration = value['duration']
                direct_routes = value['direct_routes']
                DirectRoutes.objects.create(
                    number=flight_number,
                    from_location=from_location,
                    to_location=to_location,
                    price=price,
                    duration=duration,
                    direct_routes=direct_routes
                )       

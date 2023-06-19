from django.db import models

class Location(models.Model):
    country_id = models.IntegerField()
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    country_name = models.CharField(max_length=100)

    def __str__ (self):
        return self.name


class Routes(models.Model):
    number = models.IntegerField()
    from_location = models.IntegerField()
    to_location = models.IntegerField()
    price = models.FloatField()
    duration = models.IntegerField()
    direct_routes = models.JSONField()

    def __str__(self):
        return f"{self.from_location} to {self.to_location}"


class FixedRoutes(models.Model):
    number = models.IntegerField()
    from_location = models.IntegerField()
    to_location = models.IntegerField()
    price = models.FloatField()
    duration = models.IntegerField()
    direct_routes = models.JSONField()

    def __str__(self):
        return f"{self.from_location} to {self.to_location}"


class FlyingRoutes(models.Model):
    number = models.IntegerField()
    from_location = models.IntegerField()
    to_location = models.IntegerField()
    price = models.FloatField()
    duration = models.IntegerField()
    direct_routes = models.JSONField()

    def __str__(self):
        return f"{self.from_location} to {self.to_location}"

class DirectRoutes(models.Model):
    number = models.IntegerField()
    from_location = models.IntegerField()
    to_location = models.IntegerField()
    price = models.FloatField()
    duration = models.IntegerField()
    direct_routes = models.JSONField()

    def __str__(self):
        return f"{self.from_location} to {self.to_location}"
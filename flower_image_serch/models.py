from django.db import models

# Create your models here.
class Colors(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)

class Flowers(models.Model):
    name = models.CharField(max_length=100)
    petal_number = models.IntegerField()
    color = models.ForeignKey(Colors, on_delete=models.SET_NULL, blank=True, null=True)

class Users(models.Model):
    name = models.CharField(max_length=100)
    old = models.IntegerField()
    email = models.EmailField()

class Locations(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()

class Favorite(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='favorite_user')
    flower = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='favorite_flower')

class FindLog(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='finder_user')
    flower = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='finder_flower')
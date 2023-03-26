from django.db import models

class Members(models.Model):
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=20)
    stadium = models.CharField(max_length=20)
    fans = models.IntegerField()
    founded = models.DateField()

    def __str__(self):
        return self.name



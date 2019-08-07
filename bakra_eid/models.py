from django.db import models

class EidModel(models.Model):
    greeter_name = models.CharField(max_length=100)

    def __str__(self):
        return self.greeter_name

from django.db import models


class User(models.Model):
    name = models.CharField(max_length=10, null=False, default='Machele')
    image = models.FileField(upload_to='users/', blank=True, null=True)

    def __str__(self):
        return self.name

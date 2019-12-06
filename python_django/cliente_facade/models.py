from django.db import models

class Client(models.Model):
    id   = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def get_name(self):
        return self.name
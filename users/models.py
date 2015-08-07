from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    user_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.id.__str__() + ": " + self.user_name
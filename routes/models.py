from django.db import models

# Create your models here.
class Route(models.Model):
    distance = models.DecimalField(max_digits=5,decimal_places=2)
    location = models.CharField(max_length=60)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    
    # created_at = models.DateTimeField(default=datetime.datetime.now)
    # updated_at = models.DateTimeField(default=datetime.datetime.now)  

    def __str__(self):
        return self.location + ": " + self.distance.__str__() + " mi"
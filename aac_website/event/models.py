from django.db import models

# Create your models here.
<<<<<<< HEAD

class Event(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    event_type = models.CharField(max_length=10)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    image = models.ImageField(upload_to='event',null=True, blank=True)
    registration_url = models.URLField(null=True, blank=True)
    def __str__(self):
    	return self.name
=======
>>>>>>> 2e81c0f2e07b77f4205f065bf060384c69eec4b1

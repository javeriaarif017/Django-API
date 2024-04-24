from django.db import models

# Create your models here.

class CameraData(models.Model):
    event_id=models.CharField(max_length = 1000)
    captured_at = models.CharField(max_length =1000)
    updated_at = models.CharField(max_length =1000)
    created_at = models.CharField(max_length =1000)
    camera_id = models.CharField(max_length =1000)
    file_url = models.CharField(max_length =1000)
    specie_id = models.CharField(max_length =1000)
    Date = models.CharField(max_length =1000)
    Time = models.CharField(max_length =1000)


    def __str__(self):
        return self.event_id


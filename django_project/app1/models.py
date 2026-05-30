from django.db import models

from django.utils import timezone
# Create your models here.
class appVarity(models.Model):

    APP_TYPE_CHOICE = [
        ('ML','MOBILE_LEAGE'),
        ('FF','FREE_FIRE'),
        ('YT','YOUTUBE'),
        ('VS','VSCODE'),
        ('WA','WHATSAPP'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='app1s/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2,choices=APP_TYPE_CHOICE)

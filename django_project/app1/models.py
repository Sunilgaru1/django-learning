from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User #inbuild database to store admin users data
# Create your models here.
class AppVarity(models.Model):

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
    description = models.TextField(default='')
    price = models.DecimalField(max_digits=3, decimal_places=2,default=0.00)

    def __str__(self):
        return self.name

#one to many
class AppReview(models.Model):
    RATE_CHOISE = [
        (1 , '*'),
        (2 , '**'),
        (3 , '***'),
        (4 , '****'),
        (5 , '*****'),
    ]
    App = models.ForeignKey(AppVarity,on_delete=models.CASCADE,related_name='reviews')
    #models.CASCADE tells Django to automatically delete dependent records when the referenced record is deleted.
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    rating = models.IntegerChoices(max_length = 1,choices = RATE_CHOISE)
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.App.name}' 
    

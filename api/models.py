from django.db import models
from django.contrib.auth.models import AbstractUser


from datetime import datetime  

class User(AbstractUser):
    usn = models.TextField(max_length=10, blank=True)
    department = models.TextField(max_length=500, blank=True)



class Events(models.Model):
    # song title - s
    #"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    event_id = models.IntegerField(primary_key=True)
    event_state = models.BooleanField(default=True)
    title = models.CharField(max_length=255, null=False, default='title')
    event_date = models.DateField('Event Date', default=datetime.now, blank=True)
    start_time = models.TimeField(default='12:00:00')
    end_time = models.TimeField(default='12:00:00',null=True,blank=True)
    venue = models.CharField(max_length=120,null=False, default='Venue')
    organizer = models.CharField(max_length=255, null=False,default='Organizer')
    description = models.TextField(blank=True)
    registration_link = models.CharField(max_length=255, null=True, blank=True)
    photos_link = models.CharField(max_length=255, null=True,blank=True)
    medium_link = models.CharField(max_length=255, null=True,blank=True)
    # name of artist or group/band
    def __str__(self):
        return "{} - {}".format(self.event_id, self.title)


class News(models.Model):
    # song title - s
    #"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
    news_id = models.IntegerField(primary_key=True)
    news_title = models.CharField(max_length=255, null=False, default='title')
    news_author = models.CharField(max_length=255, null=False, default='author')
    news_datetime = models.DateTimeField(default=datetime.now(), blank=True)
    news_image = models.ImageField(upload_to = 'images/', default = 'news/no-img.jpg')   
    def __str__(self):
        return "{} - {}".format(self.news_id, self.news_title)

class AttendRegister(models.Model):
    arid = models.IntegerField(primary_key=True)
    event_id = models.ForeignKey(Events, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return "{} - {}".format(self.arid, self.event_id)

    

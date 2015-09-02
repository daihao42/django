from django.db import models
import datetime

# Create your models here.
class Blog(models.Model):
	#id = models.StringField(primary_key=True, default=next_id, ddl='varchar(50)')
	title = models.CharField(max_length=50)
	content = models.TextField()
	created_at = models.DateTimeField(default=datetime.datetime.now())

class User(models.Model):
    email = models.CharField(max_length=50)
    passwd = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=datetime.datetime.now())
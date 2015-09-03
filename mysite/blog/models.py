#-*-coding:utf-8-*-
from django.db import models
import datetime,time,uuid

def next_id():
    return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)
# Create your models here.
class Blog(models.Model):
	id = models.CharField(max_length=50,primary_key = True, default=next_id)
	title = models.CharField(max_length=50)
	content = models.TextField()
	created_at = models.DateTimeField(default=datetime.datetime.now())

class User(models.Model):
    id = models.CharField(max_length=50,primary_key = True, default=next_id)
    email = models.CharField(max_length=50)
    passwd = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=50)
    created_at = models.DateTimeField(default=datetime.datetime.now())
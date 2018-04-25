from django.db import models

# Create your models here.
class Word(models.Model):
	word = models.CharField(max_length = 50)
	meaning = models.TextField()
	cdate = models.DateTimeField(auto_now_add = True)
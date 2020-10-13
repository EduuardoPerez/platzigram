""" Posts models """

# Django
from django.db import models

class User(models.Model):
  """ User model """

  email = models.EmailField(unique=True)
  password = models.CharField(max_length=12)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  bio = models.TextField(blank=True)
  birthday = models.DateField(blank=True, null=True)
  created_at = models.DateTimeField(auto_now_add=True) # When an instace is created in the DB, the datetime it's goint to be passed
  modify_at = models.DateTimeField(auto_now=True) # When an instace is modified in the DB, the datetime it's goint to be updated
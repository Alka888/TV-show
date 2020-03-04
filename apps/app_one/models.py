from __future__ import unicode_literals
from django.db import models

# Inside your app's models.py file

from django.db import models
# Our custom manager!
# No methods in our new manager should ever receive the whole request object as an argument! 
# (just parts, like request.POST)
class Tvshowmanager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        if len(postData['title']) < 2:
            errors["title"] = "Show title should be at least 2 characters"
        if len(postData['desc']) < 10:
            errors["desc"] = "Show description should be at least 10 characters"
        if len(postData['network']) < 3:
            errors["network"] = "Show network should be at least 3 characters"
        return errors

class Tvshow(models.Model):
	title = models.CharField(max_length=55)
	network = models.CharField(max_length=55)
	release_date = models.DateTimeField()
	description = models.TextField()
	objects = Tvshowmanager()




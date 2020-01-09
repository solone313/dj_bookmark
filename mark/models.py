from django.db import models

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=200)
    url = models.URLField('Site URL')

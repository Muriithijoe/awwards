from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Site(models.Model):
    screenshot = models.ImageField(upload_to = 'images/', blank = True)
    site_name = models.CharField(max_length = 30)
    description = HTMLField(max_length = 70)

    ef save_site(self):
        self.save()

    def delete_site(self):
        self.delete()

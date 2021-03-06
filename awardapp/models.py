from django.db import models
from django.core.validators import URLValidator
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Site(models.Model):
    title = models.CharField(max_length = 50)
    image = models.ImageField(upload_to = 'sites/')
    description = models.TextField(max_length = 500)
    link = models.TextField(validators=[URLValidator()],null=True)
    profile = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    design=models.PositiveIntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=1)
    usability=models.PositiveIntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=1)
    content=models.PositiveIntegerField(choices=list(zip(range(1, 11), range(1, 11))), default=1)

    def save_site(self):
        self.save()

    def delete_site(self):
        self.delete()

    @classmethod
    def get_all(cls):
        sites = cls.objects.all()
        return sites

    @classmethod
    def get_site(cls, site_id):
        site = cls.objects.get(id=site_id)
        return site

    @classmethod
    def search_by_title(cls,search_term):
        sites_title = cls.objects.filter(title__icontains=search_term)
        return sites_title

class Profile(models.Model):
    photo = models.ImageField(upload_to = 'profile/')
    profile = models.ForeignKey(User,on_delete=models.CASCADE,null = True)
    bio = models.TextField(max_length = 100)
    contact = models.IntegerField()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class AwardsProfiles(models.Model):
    name = models.CharField(max_length=40)
    bio = models.TextField()
    projects = models.CharField(max_length=70)
    dp = models.ImageField(upload_to = 'dp/')

class AwardsProjects(models.Model):
    project_name = models.CharField(max_length=40)
    description = models.TextField()

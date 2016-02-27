from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Project(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    url = models.URLField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    job = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    client = models.CharField(max_length=200, blank=True, null=True)
    categories = models.ForeignKey('Category', blank=True, null=True)
    skills = models.ManyToManyField('Skill')
    image = models.ImageField(upload_to='portfolio-featured', blank=True, null=True)
    user = models.OneToOneField(User, blank=True, null=True)

    class Meta:
        ordering = ['-start_date', '-end_date', ]

    def __unicode__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    position = models.PositiveIntegerField()

    class Meta:
        ordering = ["position"]

    def __unicode__(self):
        return self.name

class ProjectImage(models.Model):
    project = models.ForeignKey('Project')
    image = models.ImageField(upload_to='porfolio-images')
    desc = models.TextField()

    def __unicode__(self):
        return self.image.name

    def get_absolute_url(self):
        return self.image.url

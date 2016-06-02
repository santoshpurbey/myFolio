from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.forms import ModelForm

class Project(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=50, unique=True)
    url = models.URLField(blank=True, null=True)
    short_description = models.TextField(blank=True, null=True)
    description = RichTextField()
    job = models.CharField(max_length=200, blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    client = models.CharField(max_length=200, blank=True, null=True)
    categories = models.ForeignKey('Category', blank=True, null=True)
    skills = models.ManyToManyField('Skill')
    image = models.ImageField(upload_to='portfolio', blank=True, null=True)
    user = models.OneToOneField(User, blank=True, null=True)

    class Meta:
        ordering = [ '-end_date', ]

    def __unicode__(self):
        return self.name

    def publish(self):
        self.published_date = timezone.now()
        self.save()


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

    class Meta:
        ordering = ('name',)
        verbose_name = "category"
        verbose_name_plural = "categories"

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

#basic blog Model
class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
        )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    author = models.ForeignKey(User,related_name='blog_posts')
    short_description = models.CharField(max_length=300)
    body = RichTextField()
    category = models.ManyToManyField('Category')
    publish = models.DateTimeField(default=timezone.now, )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,choices=STATUS_CHOICES,default='draft')
    image = models.ImageField(upload_to='blog')

    class Meta:
        ordering = ('-publish',)


    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)


    def __str__(self):
        return 'Comment by {} on {}' . format(self.name, self.post)

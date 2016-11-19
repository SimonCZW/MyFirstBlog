from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.urls import reverse

@python_2_unicode_compatible
class Category(models.Model):
    name = models.CharField('NAME', max_length=32)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog:category_detail', kwargs={'category_id':self.pk})

@python_2_unicode_compatible
class Paper(models.Model):
    title = models.CharField('TITLE', max_length=32)
    abstract = models.CharField('ABSTRACT', max_length=256, null=True)
    content = models.TextField('CONTENT')
    created_time = models.DateTimeField('CREATED_TIME', auto_now_add=True)
    update_time = models.DateTimeField('UPDATE_TIME', auto_now=True)
    author = models.CharField('AUTHOR', max_length=32)
    category = models.ManyToManyField(Category, blank=True)
    images = models.ImageField(upload_to='photos',null=True,blank=True)

    def get_absolute_url(self):
        return reverse('blog:paper', kwargs={'paper_id':self.pk})

    def __str__(self):
        return self.title


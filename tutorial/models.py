# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


# Create your models here.
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)

    class Meta:
        ordering = ('created',)


class Account(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    bio = models.CharField(max_length=500)
    following = models.ManyToManyField('Account', related_name='followers', blank=True)

    def __str__(self):
        return self.firstname


class Kweet(models.Model):
    message = models.CharField(max_length=256)
    poster = models.ForeignKey('Account', related_name='kweets', on_delete=models.CASCADE)
    datePosted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.poster.firstname + ';' + self.message

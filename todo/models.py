# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Todo(models.Model):
    text = models.CharField(max_length=60)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text

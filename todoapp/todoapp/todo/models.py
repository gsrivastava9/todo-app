# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User

from django.db import models

# Create your models here.


class Item(models.Model):
    STATUS = (
                ('S', 'Scheduled'),
                ('P', 'In Progress'),
                ('C', 'Completed'),
            )
    title = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    owner = models.ForeignKey(User, db_column='referred_by')
    status = models.CharField(max_length=1, default="S", choices=STATUS)

    def __str__(self):
        return self.title

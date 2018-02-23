#!/usr/bin/env python
#coding:utf-8


from django.db import models

class mt(models.Model):
    num = models.TextField(null=True)
    ivr = models.TextField(null=True)

    def __unicode__(self):
        return '%s %s %s' % (self.num, self.ivr)

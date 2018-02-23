#!/usr/bin/env python
#coding:utf-8

from django.shortcuts import render
from .models import mt
from django.shortcuts import render_to_response

def index(request):
    mout = mt.objects.all()
    return render_to_response('index.html',{'mout': mout})
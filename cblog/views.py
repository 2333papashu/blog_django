# coding:utf-8
import logging
from django.shortcuts import render
logger = logging.getLogger('cblog.views')
# Create your views here.
from blog_practice import settings
def global_var(request):
    return {
    'SITE_NAME':settings.SITE_NAME,
    'SITE_DECS':settings.SITE_DECS,}


def hello(request):
    try:
        pass
    except Exception as e:
        logger.error(e)
    return render(request,'index.html',locals())
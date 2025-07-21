from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Section2OurExpertise, Section1Slideshow, Section3Background

# Create your views here.
def index(request):
    slides = Section1Slideshow.objects.order_by('order')
    services = Section2OurExpertise.objects.all()
    section3 = Section3Background.objects.first()
    return render(request, 'photography/index.html', {'slides':slides, 'services': services, 
                                                      'section3': section3  })

def contactus(request):
    #logger = logging.getLogger("testing")
    #logger.debug()
    return render(request, 'photography/contactus.html')








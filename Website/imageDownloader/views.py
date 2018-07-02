from django.shortcuts import render
from .models import Image
import os

def homePage(requests):

	imagelist = os.listdir('media/')
	# # 	Image(imgName=path).save()
	# imagelist = Image.objects.all()
	return render(requests, 'homePage/homePage.html', {'imagelist':imagelist})

import os
import requests
from .mainProcess import crowdCount
import sys
from subprocess import run, PIPE
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

def index(request):
    return render(request, 'index.html')


def dataProcess(request):
    input_image = request.FILES['images']
    fs = FileSystemStorage()
    input_image_name = fs.save(input_image.name, input_image)
    input_image_url = fs.url(input_image_name)
    total_count, output_image_name = crowdCount(input_image_name)
    output_image_url = fs.url(output_image_name)

    return render(request, 'index.html', {"count": total_count, "input_data": str(input_image_url), "output_data": str(output_image_url)})
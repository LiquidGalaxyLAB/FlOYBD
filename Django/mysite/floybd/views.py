from django.shortcuts import render
import os
import shutil
from django.http import HttpResponseRedirect
from .utils.utils import *
import requests
from django.http import JsonResponse
from django.core.urlresolvers import resolve
from django.utils.six.moves.urllib.parse import urlparse


def index(request):
    return render(request, 'floybd/index.html')


def weatherIndex(request):
    return render(request, 'floybd/indexWeather.html')


def eartquakesIndex(request):
    return render(request, 'floybd/indexEarthquakes.html')


def eartquakesHeatMapIndex(request):
    return render(request, 'floybd/earthquakes/earthquakesHeatMap.html')


def gtfs(request):
    return render(request, 'floybd/indexGTFS.html')


def clearKML(request):
    print("Deletings kmls folder")
    shutil.rmtree('static/kmls')
    os.makedirs("static/kmls")

    command = "echo '' | sshpass -p lqgalaxy ssh lg@" + getLGIp() + \
              " 'cat - > /var/www/html/kmls.txt'"
    os.system(command)

    command = "echo '' | sshpass -p lqgalaxy ssh lg@" + getLGIp() + \
              " 'cat - > /var/www/html/kmls_4.txt'"
    os.system(command)

    print("Deletings remote kmls folder")

    requests.get('http://' + getSparkIp() + ':5000/clearKML')

    return render(request, 'floybd/cleaningComplete.html')


def settingsIndex(request):
    settings = Setting.objects.all()
    return render(request, 'floybd/settings/settings.html', {'settings': settings})


def openHelp(request):
    refererPage = request.META.get('HTTP_REFERER')
    splittedUrl = refererPage.split("/")
    refererUrl = splittedUrl[len(splittedUrl)-1]
    print(refererUrl)
    return JsonResponse({'currentPage': refererUrl})


def weatherDemos(request):
    return render(request, 'floybd/weather/currentWeatherTour.html')
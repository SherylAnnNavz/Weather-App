from django.shortcuts import render
import urllib.request
import json

# Create your views here.
def index(request):
    if request.method == 'POST':
        pass
    else:
        city = 'mexico'
        source = urllib.request.urlopen('http://api.openweathermap.org/data2.5/weather?q='+city+'appid=770a17f9520e41124656aa601bc34b3c').read()
        list_of_data = json.loads(source)
        print(list_of_data)
        data = {}
    return render(request, 'main/index.html', data)
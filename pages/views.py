from django.shortcuts import render
import json
from django.conf import settings

BASE_DIR = settings.BASE_DIR

def index(request):
    data = open(str(BASE_DIR / 'pages/index.json'), 'r', encoding='utf-8')
    context = json.loads(data.read())
    data.close()

    return render(request, 'pages/index.html', context)


from django.shortcuts import render

# Create your views here.
# listings/views.py
from django.http import HttpResponse


from django.shortcuts import render

def index(request):
    return render(request, 'terrains/index.html')
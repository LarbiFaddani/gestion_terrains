
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

from terrains import views
def message_view(request):
    return HttpResponse("Ceci est un message ajouté dans urls.py !")
urlpatterns = [
    path('index/', views.index),
    path('', message_view),
    path('admin/', admin.site.urls),
]

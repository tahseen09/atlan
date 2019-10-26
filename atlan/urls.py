from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from data import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('start', csrf_exempt(views.start), name='index'),
    path('pause', csrf_exempt(views.pause)),
    path('stop', csrf_exempt(views.stop))
]

from django.contrib import admin
from django.urls import path
from ML.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('predict/',predict,name='predict'),
]

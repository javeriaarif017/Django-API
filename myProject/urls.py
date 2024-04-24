
from django.contrib import admin
from django.urls import path, include
from backend import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('backend.urls')),
    path('alldata', views.cameraData, name='cameraData'),
    path('allsummary', views.get_all_summary, name='allsummary'),

    
]

from django.urls import path
from . import views

urlpatterns = [
    ### URLS Reportes ###
    path('reportes/', views.getReportes),
    path('reportes/post/', views.postReporte),
    
]
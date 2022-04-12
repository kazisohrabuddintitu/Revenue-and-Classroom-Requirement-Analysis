from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index,name='index'),
    path('revenue/', views.revenue,name='revenue'),
    path('about/', views.about,name='about')
]
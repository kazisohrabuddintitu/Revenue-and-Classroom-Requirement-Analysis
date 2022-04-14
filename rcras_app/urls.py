from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('revenue/', views.revenue,name='revenue'),
    path('about/', views.about,name='about')
]
from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('revenue/', views.revenue,name='revenue'),
    path('about/', views.about,name='about'),
    path('view_enrolment_course_school',views.enrollment_wise_course_school,name='view_enrolment_course_school'),
    path('view_usage_resource', views.view_usage_resource, name='view_usage_resource'),
]
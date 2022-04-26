from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('about/', views.about,name='about'),
    
    
    path('view_enrolment_course_school',views.enrollment_wise_course_school,name='view_enrolment_course_school'),
    path('view_classroom_requirement_course_offer',views.view_classroom_requirement_course_offer,name='view_classroom_requirement_course_offer'),
    path('view_availabilityvscourse_offer',
         views.view_availabilityvscourse_offer, name='view_availabilityvscourse_offer'),
    path('view_revenue_of_iub',
         views.view_revenue_of_iub, name='view_revenue_of_iub')
]

from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('about/', views.about,name='about'),
    path('view_enrolment_course_school',views.enrollment_wise_course_school,name='view_enrolment_course_school'),
    path('view_revenue_of_iub',views.view_revenue_of_iub,name='view_revenue_of_iub')
    #path('classSizeDistribution', views.ClassSizeDistributionView, name='classSizeDistribution'),
]
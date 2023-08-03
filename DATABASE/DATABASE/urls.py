"""DATABASE URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# from django.contrib import admin
# from django.urls import path, include
# from django.contrib import admin
# from django.urls import path
# from django.urls.conf import include
# from RCRAS import views
# #from django.contrib.auth.views import 
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('RCRAS.urls')),
#      path('', views.index, name='index'),
#     path('login', views.loginUser, name='login'),
#     path('logout', views.logoutUser, name='logout'),
#     path('revenue/', views.revenue,name='revenue'),
#     path('about/', views.about,name='about'),
#     path('view_enrolment_course_school',views.enrollment_wise_course_school,name='view_enrolment_course_school'),
# ]



from django.contrib import admin
from django.urls import path, include
from RCRAS import views

urlpatterns = [
     path('admin/', admin.site.urls),
     path('', views.loginUser, name='login'),
     path('login/', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('about/', views.about,name='about'),
    
    
    path('view_enrolment_course_school',
         views.view_enrolment_course_school, name='view_enrolment_course_school'),
    path('view_classroom_requirement_course_offer',
         views.view_classroom_requirement_course_offer, name='view_classroom_requirement_course_offer'),
    path('view_availabilityvscourse_offer',
         views.view_availabilityvscourse_offer, name='view_availabilityvscourse_offer'),
    path('view_revenue_of_iub',
         views.view_revenue_of_iub, name='view_revenue_of_iub'),
    path('view_usage_resource',
         views.view_usage_resource, name='view_usage_resource'),
]

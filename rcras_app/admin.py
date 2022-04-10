from django.contrib import admin
from rcras_app.models import School_T,Department_T,Faculty_T,Course_T,CoOfferedCourse_T,Room_T,Section_T

# Register your models here.
admin.site.register(School_T)
admin.site.register(Department_T)
admin.site.register(Faculty_T)
admin.site.register(Course_T)
admin.site.register(CoOfferedCourse_T)
admin.site.register(Room_T)
admin.site.register(Section_T)

from django.contrib import admin
from .models import *
# Register your models here.
class School_TAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in School_T._meta.fields if field.name != "id"]


admin.site.register(School_T, School_TAdmin)


class Department_TAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Department_T._meta.fields if field.name != "id"]


admin.site.register(Department_T, Department_TAdmin)


class Faculty_TAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Faculty_T._meta.fields if field.name != "id"]


admin.site.register(Faculty_T, Faculty_TAdmin)


class Course_TAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Course_T._meta.fields if field.name != "id"]


admin.site.register(Course_T, Course_TAdmin)


class Room_TAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Room_T._meta.fields if field.name != "id"]


admin.site.register(Room_T, Room_TAdmin)


class Section_TAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in Section_T._meta.fields if field.name != "id"]


admin.site.register(Section_T, Section_TAdmin)

class CoOfferedCourse_TAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in CoOfferedCourse_T._meta.fields if field.name != "id"]


admin.site.register(CoOfferedCourse_T, CoOfferedCourse_TAdmin)

from django.contrib import admin

from detailapp.models import Course, Department,Student

# Register your models here.
admin.site.register(Department)
admin.site.register(Course)
admin.site.register(Student)



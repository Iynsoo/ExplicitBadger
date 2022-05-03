from django.contrib import admin
from .models import MyUser, course, discussion
# Register your models here.
admin.site.register(MyUser)
admin.site.register(course)
admin.site.register(discussion)

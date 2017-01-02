from django.contrib import admin, auth

# Register your models here.

from .models import ParentTask
from .models import ChildTask

admin.site.register(ParentTask)
admin.site.register(ChildTask)
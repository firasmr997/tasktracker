from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Task)
admin.site.register(Employeur)
admin.site.register(Penalite)
admin.site.register(EmployeurTask)
admin.site.register(User)


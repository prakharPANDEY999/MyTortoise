from django.contrib import admin
from .models import Plan 
from .models import Promotion
from .models import MyTortoiseUser
from .models import CustomerGoal
# Register your models here.

admin.site.register(Plan)
admin.site.register(Promotion)
admin.site.register(MyTortoiseUser)
admin.site.register(CustomerGoal)
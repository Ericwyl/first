from django.contrib import admin
from users.models import *
# admin.site.register()
# Register your models here.


from .models import Passport,Address
# Register your models here.
admin.site.register(Passport)
admin.site.register(Address)
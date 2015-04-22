from django.contrib import admin
from rg.models import Entry
from rg.models import Blog
from rg.models import Register
# Register your models here.
admin.site.register(Entry)
admin.site.register(Blog)
admin.site.register(Register)
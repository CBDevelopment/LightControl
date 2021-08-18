from django.contrib import admin
from .models import Effects, LightStrip

# Register your models here.

admin.site.register(Effects)
admin.site.register(LightStrip)

admin.site.site_header = "Cutter's LED Lights Administration"
admin.site.site_title = "Cutter's LED Lights Administration"
admin.site.index_title = "192.168.1.39"
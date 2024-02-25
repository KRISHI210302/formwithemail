from django.contrib import admin
from demo.models import  Detail
# Register your models here.
class DetailAdmin(admin.ModelAdmin):
    list_display=['id','username','number','password']
admin.site.register(Detail,DetailAdmin)
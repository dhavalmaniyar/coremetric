from django.contrib import admin
from .models import Comment,UserCount
# Register your models here.
admin.register(Comment,UserCount)(admin.ModelAdmin)
